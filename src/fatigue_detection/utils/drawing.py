"""Drawing overlays on frames — landmarks, bounding boxes, status text, alerts."""

from __future__ import annotations

import numpy as np


def draw_landmarks(
    frame: np.ndarray,
    landmarks: np.ndarray,
    color: tuple[int, int, int] = (0, 255, 0),
    radius: int = 1,
) -> np.ndarray:
    """Draw facial landmarks as small circles on the frame."""
    raise NotImplementedError


def draw_bounding_box(
    frame: np.ndarray,
    bbox: tuple[int, int, int, int],
    label: str = "",
    color: tuple[int, int, int] = (0, 255, 0),
) -> np.ndarray:
    """Draw a labelled bounding box on the frame."""
    raise NotImplementedError


def draw_status_bar(
    frame: np.ndarray,
    ear: float | None = None,
    mar: float | None = None,
    fps: float | None = None,
    state: str = "",
) -> np.ndarray:
    """Draw a status bar with EAR, MAR, FPS, and system state at the top of the frame."""
    raise NotImplementedError


def draw_alert_overlay(frame: np.ndarray, message: str = "FATIGUE ALERT") -> np.ndarray:
    """Draw a prominent red alert banner across the frame."""
    raise NotImplementedError
