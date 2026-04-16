"""CNN classifier for eye state (open / closed).

Lightweight CNN (MobileNetV2 pretrained) for eye state classification.
Crop and resize the relevant ROI (48x48 or 64x64) before inference.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


class EyeStateClassifier:
    """MobileNetV2-based binary classifier for eye open/closed."""

    NUM_CLASSES = 2

    def __init__(self, input_size: int = 64, pretrained: bool = True) -> None:
        self.input_size = input_size
        self.pretrained = pretrained
        self._model = None  # lazy-init torch model

    def build_model(self) -> None:
        """Instantiate MobileNetV2 with a modified final layer for binary classification."""
        raise NotImplementedError

    def predict(self, eye_roi: np.ndarray) -> tuple[int, float]:
        """Predict eye state from a cropped eye ROI image.

        Returns:
            (class_id, confidence) where 0=open, 1=closed.
        """
        raise NotImplementedError

    def extract_features(self, eye_roi: np.ndarray) -> np.ndarray:
        """Extract the penultimate-layer features for temporal modelling."""
        raise NotImplementedError

    def save(self, path: Path) -> None:
        raise NotImplementedError

    def load(self, path: Path) -> None:
        raise NotImplementedError
