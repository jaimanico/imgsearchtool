"""Video capture and frame iteration helpers."""

from __future__ import annotations

from pathlib import Path
from typing import Iterator

import numpy as np


class VideoCapture:
    """Wrapper around cv2.VideoCapture with context manager support."""

    def __init__(self, source: int | str | Path = 0, fps_limit: int | None = None) -> None:
        """
        Args:
            source: Camera device ID (int) or path to video file.
            fps_limit: If set, limit playback to this FPS.
        """
        self.source = source
        self.fps_limit = fps_limit
        self._cap = None

    def open(self) -> None:
        """Open the video source."""
        raise NotImplementedError

    def read(self) -> tuple[bool, np.ndarray | None]:
        """Read a single frame. Returns (success, frame)."""
        raise NotImplementedError

    def frames(self) -> Iterator[np.ndarray]:
        """Yield frames one at a time until the source is exhausted."""
        raise NotImplementedError

    def release(self) -> None:
        """Release the underlying capture resource."""
        raise NotImplementedError

    def __enter__(self) -> VideoCapture:
        self.open()
        return self

    def __exit__(self, *args: object) -> None:
        self.release()

    @property
    def frame_width(self) -> int:
        raise NotImplementedError

    @property
    def frame_height(self) -> int:
        raise NotImplementedError

    @property
    def fps(self) -> float:
        raise NotImplementedError
