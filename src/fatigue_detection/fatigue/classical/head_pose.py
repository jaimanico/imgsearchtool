"""Head pose estimation via solvePnP.

Uses cv2.solvePnP() with a 3D face model and 2D landmark detections
to estimate pitch/roll/yaw angles.
"""

from __future__ import annotations

import numpy as np

# Approximate 3D coordinates of key facial landmarks (nose tip, chin, etc.)
# used as the reference model for solvePnP.
MODEL_POINTS_68 = np.array([
    (0.0, 0.0, 0.0),             # Nose tip (landmark 30)
    (0.0, -330.0, -65.0),        # Chin (landmark 8)
    (-225.0, 170.0, -135.0),     # Left eye left corner (landmark 36)
    (225.0, 170.0, -135.0),      # Right eye right corner (landmark 45)
    (-150.0, -150.0, -125.0),    # Left mouth corner (landmark 48)
    (150.0, -150.0, -125.0),     # Right mouth corner (landmark 54)
], dtype=np.float64)


class HeadPoseEstimator:
    """Estimate head yaw, pitch, roll from 2D facial landmarks."""

    def __init__(self, frame_width: int = 640, frame_height: int = 480) -> None:
        self.frame_width = frame_width
        self.frame_height = frame_height
        self._camera_matrix: np.ndarray | None = None
        self._dist_coeffs = np.zeros((4, 1), dtype=np.float64)

    def _build_camera_matrix(self) -> np.ndarray:
        """Construct an approximate camera intrinsic matrix."""
        raise NotImplementedError

    def estimate(self, landmarks_2d: np.ndarray) -> tuple[float, float, float]:
        """Estimate head pose from 2D landmarks.

        Args:
            landmarks_2d: Key 2D landmarks matching MODEL_POINTS_68 ordering.

        Returns:
            (yaw, pitch, roll) angles in degrees.
        """
        raise NotImplementedError
