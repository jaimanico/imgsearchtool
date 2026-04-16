"""Main application loop: camera capture -> gesture gate -> fatigue detection -> alert.

This is the top-level orchestrator: camera capture -> gesture gate -> fatigue detection -> alert.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np

from .config import SystemConfig


class FatigueDetectionApp:
    """End-to-end application that ties together gesture activation and fatigue detection."""

    def __init__(self, config: SystemConfig, pipeline: str = "classical") -> None:
        self.config = config
        self.pipeline = pipeline
        self._activated = False
        # TODO: instantiate gesture module, fatigue modules, alert manager

    def run_live(self) -> None:
        """Run on a live camera feed until the user quits."""
        raise NotImplementedError

    def run_eval(self, video_path: Path) -> dict[str, float]:
        """Run evaluation on a recorded video and return metric results."""
        raise NotImplementedError

    def process_frame(self, frame: np.ndarray) -> dict:
        """Process a single frame through the full pipeline.

        Returns a dict with keys like 'gesture_state', 'fatigue_score',
        'ear', 'mar', 'alert', etc.
        """
        raise NotImplementedError
