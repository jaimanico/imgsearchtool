"""CNN classifier for mouth state (normal / yawning).

Lightweight CNN (MobileNetV2 pretrained) for mouth state classification.
Crop and resize the relevant ROI before inference.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


class MouthStateClassifier:
    """MobileNetV2-based binary classifier for normal/yawning."""

    NUM_CLASSES = 2

    def __init__(self, input_size: int = 64, pretrained: bool = True) -> None:
        self.input_size = input_size
        self.pretrained = pretrained
        self._model = None

    def build_model(self) -> None:
        """Instantiate MobileNetV2 with modified head for binary classification."""
        raise NotImplementedError

    def predict(self, mouth_roi: np.ndarray) -> tuple[int, float]:
        """Predict mouth state from a cropped mouth ROI.

        Returns:
            (class_id, confidence) where 0=normal, 1=yawning.
        """
        raise NotImplementedError

    def extract_features(self, mouth_roi: np.ndarray) -> np.ndarray:
        """Extract penultimate-layer features for temporal modelling."""
        raise NotImplementedError

    def save(self, path: Path) -> None:
        raise NotImplementedError

    def load(self, path: Path) -> None:
        raise NotImplementedError
