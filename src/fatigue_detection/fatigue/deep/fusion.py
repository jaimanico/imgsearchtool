"""Multi-cue fatigue fusion — combines eye, mouth, and head pose signals.

Combines eye, mouth, and head pose signals into a single fatigue score
using a small MLP or simple voting logic.
"""

from __future__ import annotations

import numpy as np


class DeepFatiguePipeline:
    """Orchestrates the deep learning fatigue detection sub-models."""

    def __init__(self, fusion_mode: str = "voting") -> None:
        """
        Args:
            fusion_mode: "voting" for majority vote, "mlp" for learned fusion.
        """
        self.fusion_mode = fusion_mode
        self._eye_model = None
        self._mouth_model = None
        self._temporal_model = None

    def init_models(self) -> None:
        """Instantiate all sub-models (eye CNN, mouth CNN, temporal LSTM)."""
        raise NotImplementedError

    def predict_frame(
        self,
        eye_roi: np.ndarray,
        mouth_roi: np.ndarray,
        head_angles: tuple[float, float, float],
    ) -> tuple[float, dict]:
        """Run all sub-models on a single frame's data and fuse results.

        Returns:
            (fatigue_score, details_dict) where fatigue_score is in [0, 1].
        """
        raise NotImplementedError

    def fuse_scores(
        self,
        eye_score: float,
        mouth_score: float,
        head_score: float,
    ) -> float:
        """Combine individual cue scores into a single fatigue probability."""
        raise NotImplementedError
