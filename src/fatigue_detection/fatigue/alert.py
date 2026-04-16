"""Alert triggering logic — visual and optional audio warnings.

Triggers an on-screen warning and optionally a sound alert when fatigue
is detected for N consecutive frames.
"""

from __future__ import annotations

import numpy as np


class AlertManager:
    """Tracks consecutive fatigue frames and triggers alerts."""

    def __init__(self, consec_threshold: int = 10) -> None:
        self.consec_threshold = consec_threshold
        self._consec_count = 0
        self._alert_active = False

    @property
    def is_alerting(self) -> bool:
        return self._alert_active

    def update(self, fatigue_detected: bool) -> bool:
        """Update the alert state with the latest frame's fatigue prediction.

        Returns True if an alert should be displayed.
        """
        raise NotImplementedError

    def draw_alert(self, frame: np.ndarray) -> np.ndarray:
        """Overlay a visual alert on the frame if alerting."""
        raise NotImplementedError

    def play_sound(self) -> None:
        """Play an audio alert (optional)."""
        raise NotImplementedError

    def reset(self) -> None:
        self._consec_count = 0
        self._alert_active = False
