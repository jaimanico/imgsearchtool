"""Eye Aspect Ratio (EAR) computation.

EAR = (|p2 - p6| + |p3 - p5|) / (2 * |p1 - p4|)
where p1..p6 are the 6 eye landmarks.
EAR < 0.25 sustained over 15+ frames = drowsy.
"""

from __future__ import annotations

from collections import deque

import numpy as np

DEFAULT_EAR_THRESHOLD = 0.25
DEFAULT_CONSEC_FRAMES = 15


def compute_ear(eye_landmarks: np.ndarray) -> float:
    """Compute EAR for a single eye given 6 landmark points (6, 2).

    Args:
        eye_landmarks: Array of shape (6, 2) with the six eye landmarks
                       ordered [p1, p2, p3, p4, p5, p6].

    Returns:
        The Eye Aspect Ratio as a float.
    """
    raise NotImplementedError


class EARTracker:
    """Track EAR values over time with rolling average for noise reduction."""

    def __init__(
        self,
        threshold: float = DEFAULT_EAR_THRESHOLD,
        consec_frames: int = DEFAULT_CONSEC_FRAMES,
        rolling_window: int = 15,
    ) -> None:
        self.threshold = threshold
        self.consec_frames = consec_frames
        self._history: deque[float] = deque(maxlen=rolling_window)
        self._below_count = 0

    def update(self, left_eye: np.ndarray, right_eye: np.ndarray) -> tuple[float, bool]:
        """Compute average EAR for both eyes and check for drowsiness.

        Returns:
            (ear_value, is_drowsy) tuple.
        """
        raise NotImplementedError

    def reset(self) -> None:
        self._history.clear()
        self._below_count = 0
