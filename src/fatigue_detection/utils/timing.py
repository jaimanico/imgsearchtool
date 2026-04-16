"""FPS counter and per-frame latency measurement.

Tracks inference time per frame (ms) and total pipeline FPS.
"""

from __future__ import annotations

import time
from collections import deque


class FPSCounter:
    """Rolling FPS counter over a sliding window of frame timestamps."""

    def __init__(self, window_size: int = 30) -> None:
        self._timestamps: deque[float] = deque(maxlen=window_size)

    def tick(self) -> None:
        """Record the current timestamp."""
        self._timestamps.append(time.perf_counter())

    @property
    def fps(self) -> float:
        """Current frames per second."""
        if len(self._timestamps) < 2:
            return 0.0
        elapsed = self._timestamps[-1] - self._timestamps[0]
        if elapsed <= 0:
            return 0.0
        return (len(self._timestamps) - 1) / elapsed


class Timer:
    """Context manager for measuring elapsed time in milliseconds."""

    def __init__(self) -> None:
        self.elapsed_ms: float = 0.0
        self._start: float = 0.0

    def __enter__(self) -> Timer:
        self._start = time.perf_counter()
        return self

    def __exit__(self, *args: object) -> None:
        self.elapsed_ms = (time.perf_counter() - self._start) * 1000.0
