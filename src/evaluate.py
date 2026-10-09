"""Evaluation utilities for Heck reaction yield prediction."""

import numpy as np
import pandas as pd

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def evaluate_predictions(y_true, y_pred):
    """
    Calculate standard regression metrics.

    MAE and RMSE are in yield percentage points when yields
    are expressed on a 0–100 scale.
    """
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)

    if y_true.ndim != 1 or y_pred.ndim != 1:
        raise ValueError("Actual and predicted yields must be one-dimensional.")

    if len(y_true) != len(y_pred):
        raise ValueError("Actual and predicted yields must have equal lengths.")

    if len(y_true) < 2:
        raise ValueError("At least two observations are required.")

    if not np.isfinite(y_true).all() or not np.isfinite(y_pred).all():
        raise ValueError("Yields contain missing or infinite values.")

    return {
        "n_test": len(y_true),
        "MAE": mean_absolute_error(y_true, y_pred),
        "RMSE": np.sqrt(mean_squared_error(y_true, y_pred)),
        "R2": r2_score(y_true, y_pred),
    }


def evaluate_model(model, X_train, y_train, X_test, y_test):
    """
    Fit a scikit-learn-compatible model and evaluate its predictions.

    Returns:
        fitted_model: The trained model.
        metrics: Dictionary containing n_test, MAE, RMSE, and R2.
        predictions: Predicted yields for the test set.
    """
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    metrics = evaluate_predictions(y_test, predictions)

    return model, metrics, predictions


def save_results(results, output_path):
    """Save a list of evaluation-result dictionaries to CSV."""
    if not results:
        raise ValueError("No evaluation results were provided.")

    pd.DataFrame(results).to_csv(output_path, index=False)
