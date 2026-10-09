"""
Train/test splitting utilities for Heck reaction yield prediction.

Provides:
1. Random split
2. Reactant-grouped split to reduce overlap in reactant combinations
"""

import numpy as np
import pandas as pd

from sklearn.model_selection import GroupShuffleSplit, train_test_split


REACTANT_COLUMNS = [
    "reactants 1",
    "reactants 2",
    "reactants 3",
    "reactants 4",
    "reactants 5",
]


def validate_dataset(df):
    """Check that the required target and reactant columns exist."""
    required = ["Yield"] + REACTANT_COLUMNS
    missing = [column for column in required if column not in df.columns]

    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    if df["Yield"].isna().any():
        raise ValueError("Yield contains missing values.")

    if len(df) < 2:
        raise ValueError("At least two reactions are required.")


def random_split(df, test_size=0.2, random_state=42):
    """Split reactions randomly into training and test sets."""
    validate_dataset(df)

    indices = np.arange(len(df))
    train_idx, test_idx = train_test_split(
        indices,
        test_size=test_size,
        random_state=random_state,
        shuffle=True,
    )

    return train_idx, test_idx


def _reactant_group_keys(df):
    """
    Build a group key from the available reactant SMILES.

    Reactant order is sorted so the same set of reactants produces
    the same key even if their columns appear in a different order.
    """
    keys = []

    for _, row in df[REACTANT_COLUMNS].iterrows():
        reactants = [
            value.strip()
            for value in row
            if isinstance(value, str) and value.strip()
        ]
        keys.append(" || ".join(sorted(reactants)))

    return np.asarray(keys, dtype=object)


def grouped_reactant_split(df, test_size=0.2, random_state=42):
    """
    Split by reactant-group key so identical reactant sets do not
    appear in both training and test sets.

    Note: this is a grouped split, not a guarantee of fully novel
    chemistry. Individual reactants can still occur across groups.
    """
    validate_dataset(df)

    groups = _reactant_group_keys(df)
    indices = np.arange(len(df))

    splitter = GroupShuffleSplit(
        n_splits=1,
        test_size=test_size,
        random_state=random_state,
    )

    train_idx, test_idx = next(
        splitter.split(indices, df["Yield"].to_numpy(), groups=groups)
    )

    return train_idx, test_idx


def check_group_overlap(df, train_idx, test_idx):
    """Return the number of reactant-group keys shared across splits."""
    groups = _reactant_group_keys(df)

    train_groups = set(groups[train_idx])
    test_groups = set(groups[test_idx])

    return len(train_groups.intersection(test_groups))
