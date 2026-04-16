"""Visualization helpers for the technical report.

Generates ROC curves, confusion matrices, precision-recall curves,
and latency comparison charts.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


def plot_roc_curve(
    fpr: np.ndarray,
    tpr: np.ndarray,
    auc_value: float,
    save_path: Path | None = None,
) -> None:
    """Plot and optionally save an ROC curve."""
    raise NotImplementedError


def plot_confusion_matrix(
    cm: np.ndarray,
    labels: list[str] | None = None,
    save_path: Path | None = None,
) -> None:
    """Plot and optionally save a confusion matrix heatmap."""
    raise NotImplementedError


def plot_precision_recall_curve(
    precision: np.ndarray,
    recall: np.ndarray,
    save_path: Path | None = None,
) -> None:
    """Plot and optionally save a precision-recall curve."""
    raise NotImplementedError


def plot_latency_comparison(
    classical_ms: list[float],
    deep_ms: list[float],
    save_path: Path | None = None,
) -> None:
    """Bar/box plot comparing per-frame latency of both pipelines."""
    raise NotImplementedError


def plot_ear_mar_timeline(
    ear_values: list[float],
    mar_values: list[float],
    labels: list[int] | None = None,
    save_path: Path | None = None,
) -> None:
    """Plot EAR and MAR values over time with fatigue labels overlaid."""
    raise NotImplementedError
