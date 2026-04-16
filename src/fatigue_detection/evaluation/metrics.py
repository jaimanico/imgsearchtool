"""Fatigue detection evaluation metrics.

Metrics:
    - Frame-level accuracy, precision, recall, F1 for alert vs. fatigue.
    - PERCLOS: percentage of frames where eyes are >80% closed in a 1-min window.
    - ROC curve and AUC for overall fatigue score.
    - Confusion matrix for both pipelines.
    - Inference time per frame (ms) and total pipeline FPS.
"""

from __future__ import annotations

import numpy as np


def accuracy(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Frame-level classification accuracy."""
    raise NotImplementedError


def precision_recall_f1(
    y_true: np.ndarray, y_pred: np.ndarray
) -> tuple[float, float, float]:
    """Compute precision, recall, and F1 for the drowsy class."""
    raise NotImplementedError


def confusion_matrix(y_true: np.ndarray, y_pred: np.ndarray) -> np.ndarray:
    """Return 2x2 confusion matrix [[TN, FP], [FN, TP]]."""
    raise NotImplementedError


def roc_auc(y_true: np.ndarray, y_scores: np.ndarray) -> tuple[np.ndarray, np.ndarray, float]:
    """Compute ROC curve (fpr, tpr) and AUC.

    Returns:
        (fpr_array, tpr_array, auc_value)
    """
    raise NotImplementedError


def perclos(ear_values: np.ndarray, threshold: float = 0.25, fps: int = 30) -> float:
    """Compute PERCLOS — percentage of frames with eyes >80% closed in a 1-minute window.

    This is the industry-standard drowsiness metric.
    """
    raise NotImplementedError


def compute_all_metrics(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    y_scores: np.ndarray | None = None,
) -> dict[str, float]:
    """Compute all evaluation metrics and return as a dictionary."""
    raise NotImplementedError
