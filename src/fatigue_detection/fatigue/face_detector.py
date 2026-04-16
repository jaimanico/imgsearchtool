"""Face detection abstraction supporting multiple backends.

Classical: OpenCV Haar cascades or dlib HOG.
Deep: MediaPipe Face Detection or RetinaFace.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

import numpy as np


class FaceDetector(ABC):
    """Abstract base for face detectors returning bounding boxes."""

    @abstractmethod
    def detect(self, frame: np.ndarray) -> list[tuple[int, int, int, int]]:
        """Return list of (x, y, w, h) bounding boxes for detected faces."""


class DlibHOGFaceDetector(FaceDetector):
    """dlib's HOG-based frontal face detector."""

    def __init__(self) -> None:
        self._detector = None  # lazy-load dlib

    def detect(self, frame: np.ndarray) -> list[tuple[int, int, int, int]]:
        raise NotImplementedError


class HaarCascadeFaceDetector(FaceDetector):
    """OpenCV Haar cascade face detector."""

    def __init__(self, cascade_path: str | None = None) -> None:
        self.cascade_path = cascade_path

    def detect(self, frame: np.ndarray) -> list[tuple[int, int, int, int]]:
        raise NotImplementedError


class MediaPipeFaceDetector(FaceDetector):
    """MediaPipe face detector for the deep learning pipeline."""

    def __init__(self, min_detection_confidence: float = 0.5) -> None:
        self.min_detection_confidence = min_detection_confidence

    def detect(self, frame: np.ndarray) -> list[tuple[int, int, int, int]]:
        raise NotImplementedError
