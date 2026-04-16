"""Side-by-side comparison of classical and deep learning pipelines.

Runs both pipelines on the same video clips and compares them on
accuracy (per-frame labels), latency (ms/frame), and false positive/negative rate.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


class PipelineComparison:
    """Run both pipelines on the same data and collect comparative metrics."""

    def __init__(self, video_paths: list[Path] | None = None) -> None:
        self.video_paths = video_paths or []
        self.results: dict[str, dict] = {}

    def run(self) -> dict[str, dict]:
        """Execute both pipelines on all videos and gather metrics.

        Returns:
            Dict keyed by pipeline name with metric dicts as values.
        """
        raise NotImplementedError

    def summary_table(self) -> str:
        """Format comparison results as a printable table."""
        raise NotImplementedError
