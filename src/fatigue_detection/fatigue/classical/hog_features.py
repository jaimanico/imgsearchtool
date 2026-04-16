"""HOG (Histogram of Oriented Gradients) feature extraction from face ROI.

Extracts HOG features from the cropped face region for the SVM classifier.
"""

from __future__ import annotations

import numpy as np


class HOGExtractor:
    """Extract HOG descriptor from a face region of interest."""

    def __init__(
        self,
        win_size: tuple[int, int] = (64, 128),
        block_size: tuple[int, int] = (16, 16),
        block_stride: tuple[int, int] = (8, 8),
        cell_size: tuple[int, int] = (8, 8),
        n_bins: int = 9,
    ) -> None:
        self.win_size = win_size
        self.block_size = block_size
        self.block_stride = block_stride
        self.cell_size = cell_size
        self.n_bins = n_bins
        self._hog = None  # lazy-init cv2.HOGDescriptor

    def extract(self, face_roi: np.ndarray) -> np.ndarray:
        """Compute HOG descriptor for a cropped, grayscale face image.

        Args:
            face_roi: Grayscale face image, resized to win_size.

        Returns:
            1D float32 HOG feature vector.
        """
        raise NotImplementedError
