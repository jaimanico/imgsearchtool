"""Mouth Aspect Ratio (MAR) computation for yawn detection.

Same principle as EAR but on mouth landmarks.
MAR > 0.6 sustained = yawning.
"""

from __future__ import annotations

from collections import deque

import numpy as np

DEFAULT_MAR_THRESHOLD = 0.6
DEFAULT_CONSEC_FRAMES = 10


def compute_mar(mouth_landmarks: np.ndarray) -> float:
    """Compute the Mouth Aspect Ratio from mouth landmark points.

    Args:
        mouth_landmarks: Array of mouth landmarks (inner lip points).

    Returns:
        The Mouth Aspect Ratio as a float.
    """
    raise NotImplementedError


class MARTracker:
    """Track MAR values over time to detect sustained yawning."""

    def __init__(
        self,
        threshold: float = DEFAULT_MAR_THRESHOLD,
        consec_frames: int = DEFAULT_CONSEC_FRAMES,
        rolling_window: int = 15,
    ) -> None:
        self.threshold = threshold
        self.consec_frames = consec_frames
        self._history: deque[float] = deque(maxlen=rolling_window)
        self._above_count = 0

    def update(self, mouth_landmarks: np.ndarray) -> tuple[float, bool]:
        """Compute MAR and check for yawning.

        Returns:
            (mar_value, is_yawning) tuple.
        """
        raise NotImplementedError

    def reset(self) -> None:
        self._history.clear()
        self._above_count = 0
