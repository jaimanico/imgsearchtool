"""Frame preprocessing utilities.

Applies CLAHE (histogram equalisation) preprocessing for poor lighting conditions.
"""

from __future__ import annotations

import numpy as np


def apply_clahe(
    frame: np.ndarray,
    clip_limit: float = 2.0,
    grid_size: tuple[int, int] = (8, 8),
) -> np.ndarray:
    """Apply CLAHE to the luminance channel for contrast enhancement in low light."""
    raise NotImplementedError


def resize_frame(frame: np.ndarray, width: int, height: int) -> np.ndarray:
    """Resize a frame to the target dimensions."""
    raise NotImplementedError


def to_grayscale(frame: np.ndarray) -> np.ndarray:
    """Convert a BGR frame to grayscale."""
    raise NotImplementedError


def normalize_for_model(frame: np.ndarray, mean: tuple = (0.485, 0.456, 0.406), std: tuple = (0.229, 0.224, 0.225)) -> np.ndarray:
    """ImageNet-style normalization for deep learning models."""
    raise NotImplementedError


def crop_roi(frame: np.ndarray, bbox: tuple[int, int, int, int]) -> np.ndarray:
    """Crop a region of interest from a frame given (x, y, w, h)."""
    raise NotImplementedError
