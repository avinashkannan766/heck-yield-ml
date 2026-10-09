
"""
Feature generation for Heck reaction yield prediction.

Converts reactant SMILES into Morgan fingerprints.
Only reactants are used as molecular features.
Products and experimental yields are not included.
"""

import numpy as np
import pandas as pd

from rdkit import Chem, DataStructs
from rdkit.Chem import rdFingerprintGenerator


MISSING_VALUES = {
    "",
    "undefined",
    "nan",
    "none",
    "null",
    "na",
    "n/a",
}


def get_reactant_columns(df):
    """Find reactant SMILES columns in the dataset."""
    return [
        column
        for column in df.columns
        if column.startswith("reactants ")
    ]


def is_missing_smiles(smiles):
    """Return True when a value represents a missing reactant."""
    if not isinstance(smiles, str):
        return True

    return smiles.strip().lower() in MISSING_VALUES


def morgan_fingerprint(smiles, radius=2, n_bits=2048):
    """
    Convert one SMILES string into a Morgan fingerprint.

    Missing values produce an all-zero fingerprint.
    Invalid, non-empty SMILES raise a ValueError.
    """
    if is_missing_smiles(smiles):
        return np.zeros(n_bits, dtype=np.uint8)

    smiles = smiles.strip()
    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        raise ValueError(f"Invalid SMILES: {smiles!r}")

    generator = rdFingerprintGenerator.GetMorganGenerator(
        radius=radius,
        fpSize=n_bits,
    )

    fingerprint = generator.GetFingerprint(mol)

    array = np.zeros(n_bits, dtype=np.uint8)
    DataStructs.ConvertToNumpyArray(fingerprint, array)

    return array


def build_morgan_features(
    df,
    reactant_columns=None,
    radius=2,
    n_bits=2048,
):
    """
    Build one Morgan fingerprint per reaction.

    Fingerprints from all available reactant columns are combined
    using bitwise OR. Missing reactant values are skipped.

    Returns an array with shape (number of reactions, n_bits).
    """
    if reactant_columns is None:
        reactant_columns = get_reactant_columns(df)

    if not reactant_columns:
        raise ValueError("No reactant SMILES columns were found.")

    missing_columns = [
        column
        for column in reactant_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing reactant columns: {missing_columns}"
        )

    features = []

    for row_index, (_, row) in enumerate(df.iterrows()):
        reaction_fp = np.zeros(n_bits, dtype=np.uint8)
        found_reactant = False

        for column in reactant_columns:
            smiles = row[column]

            if is_missing_smiles(smiles):
                continue

            fingerprint = morgan_fingerprint(
                smiles,
                radius=radius,
                n_bits=n_bits,
            )

            reaction_fp = np.bitwise_or(
                reaction_fp,
                fingerprint,
            )

            found_reactant = True

        if not found_reactant:
            raise ValueError(
                f"No usable reactant SMILES in dataset row "
                f"{row_index} (DataFrame index {df.index[row_index]})."
            )

        features.append(reaction_fp)

    return np.asarray(features, dtype=np.uint8)
