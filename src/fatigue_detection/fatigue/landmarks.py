"""Facial landmark extraction wrappers.

Classical: dlib 68-point shape predictor.
Deep: MediaPipe Face Mesh (468 landmarks).
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

import numpy as np

# Landmark index constants for dlib 68-point model
LEFT_EYE_INDICES = list(range(36, 42))
RIGHT_EYE_INDICES = list(range(42, 48))
MOUTH_INDICES = list(range(48, 68))
NOSE_TIP_INDEX = 30
CHIN_INDEX = 8


class LandmarkExtractor(ABC):
    """Abstract base class for facial landmark extraction."""

    @abstractmethod
    def extract(
        self, frame: np.ndarray, face_bbox: tuple[int, int, int, int]
    ) -> np.ndarray | None:
        """Return (N, 2) or (N, 3) landmark coordinates, or None if detection fails."""


class DlibLandmarkExtractor(LandmarkExtractor):
    """dlib shape_predictor_68_face_landmarks wrapper."""

    def __init__(self, model_path: str | Path | None = None) -> None:
        self.model_path = model_path
        self._predictor = None  # lazy-load

    def extract(
        self, frame: np.ndarray, face_bbox: tuple[int, int, int, int]
    ) -> np.ndarray | None:
        raise NotImplementedError


class MediaPipeFaceMesh(LandmarkExtractor):
    """MediaPipe Face Mesh — returns 468 3D landmarks."""

    def __init__(self, max_faces: int = 1) -> None:
        self.max_faces = max_faces

    def extract(
        self, frame: np.ndarray, face_bbox: tuple[int, int, int, int]
    ) -> np.ndarray | None:
        raise NotImplementedError
