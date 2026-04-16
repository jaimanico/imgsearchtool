"""LSTM temporal model over CNN feature sequences.

Feeds a sequence of CNN-extracted features into a 1-layer LSTM to
capture the temporal pattern of sustained closure vs. a normal blink.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


class TemporalFatigueModel:
    """1-layer LSTM that processes a window of CNN features to detect sustained fatigue."""

    def __init__(
        self,
        input_dim: int = 256,
        hidden_dim: int = 128,
        num_layers: int = 1,
        sequence_length: int = 16,
    ) -> None:
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.num_layers = num_layers
        self.sequence_length = sequence_length
        self._model = None

    def build_model(self) -> None:
        """Instantiate the LSTM + classification head."""
        raise NotImplementedError

    def predict(self, feature_sequence: np.ndarray) -> tuple[int, float]:
        """Predict fatigue from a sequence of feature vectors.

        Args:
            feature_sequence: (sequence_length, input_dim) array.

        Returns:
            (class_id, confidence) where 0=alert, 1=drowsy.
        """
        raise NotImplementedError

    def save(self, path: Path) -> None:
        raise NotImplementedError

    def load(self, path: Path) -> None:
        raise NotImplementedError
