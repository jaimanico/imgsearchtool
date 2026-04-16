"""Rule-based gesture classification from hand landmarks.

Defines gestures via finger-angle or landmark distance rules.

Suggested gesture pair:
  - Gesture 1: Open palm (all 5 fingers extended)
  - Gesture 2: Thumbs up (thumb extended, all others curled)
"""

from __future__ import annotations

from enum import Enum

import numpy as np


class Gesture(Enum):
    UNKNOWN = "unknown"
    OPEN_PALM = "open_palm"
    THUMBS_UP = "thumbs_up"
    FIST = "fist"


class GestureClassifier:
    """Classify a gesture from a (21, 3) hand landmark array."""

    def classify(self, landmarks: np.ndarray) -> Gesture:
        """Determine which gesture the hand landmarks represent.

        Uses finger-tip vs. MCP joint distances and angles to decide.
        """
        raise NotImplementedError

    def _fingers_extended(self, landmarks: np.ndarray) -> list[bool]:
        """Return a boolean per finger indicating if it is extended."""
        raise NotImplementedError
