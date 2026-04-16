"""Video and frame dataset classes.

Split by subject, not by frame, to avoid data leakage.

Label CSV format: frame_id, EAR, MAR, head_yaw, head_pitch, fatigue_label
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


class FatigueDataset:
    """Load labelled fatigue video frames for training or evaluation."""

    def __init__(
        self,
        video_dir: Path,
        labels_dir: Path,
        split: str = "train",
        subjects: list[str] | None = None,
    ) -> None:
        self.video_dir = video_dir
        self.labels_dir = labels_dir
        self.split = split
        self.subjects = subjects or []
        self._frames: list[np.ndarray] = []
        self._labels: list[int] = []

    def load(self) -> None:
        """Scan video files and corresponding CSV labels."""
        raise NotImplementedError

    def __len__(self) -> int:
        return len(self._frames)

    def __getitem__(self, idx: int) -> tuple[np.ndarray, int]:
        raise NotImplementedError

    @staticmethod
    def split_by_subject(
        subjects: list[str],
        train_ratio: float = 0.70,
        val_ratio: float = 0.15,
    ) -> tuple[list[str], list[str], list[str]]:
        """Split subject list into train/val/test sets.

        Ensures no subject appears in multiple splits (prevents data leakage).
        """
        raise NotImplementedError


class GestureDataset:
    """Load gesture sequence recordings for testing the activation gate."""

    def __init__(self, gesture_dir: Path) -> None:
        self.gesture_dir = gesture_dir

    def load(self) -> None:
        raise NotImplementedError
