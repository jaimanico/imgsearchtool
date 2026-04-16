"""MediaPipe Hands wrapper for real-time hand landmark detection.

Uses MediaPipe Hands for real-time hand landmark detection (no GPU required).
"""

from __future__ import annotations

import numpy as np


class HandDetector:
    """Wraps MediaPipe Hands to detect and return 21 hand landmarks per frame."""

    def __init__(self, max_hands: int = 1, min_detection_confidence: float = 0.7) -> None:
        self.max_hands = max_hands
        self.min_detection_confidence = min_detection_confidence
        self._hands = None  # lazy-initialised MediaPipe Hands instance

    def _init_model(self) -> None:
        """Lazy-load MediaPipe to avoid import cost at module level."""
        raise NotImplementedError

    def detect(self, frame: np.ndarray) -> list[np.ndarray]:
        """Return a list of (21, 3) landmark arrays for each detected hand."""
        raise NotImplementedError

    def close(self) -> None:
        """Release MediaPipe resources."""
        raise NotImplementedError
