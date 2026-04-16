"""Tests for the classical fatigue detection pipeline.

Covers: EAR computation, MAR computation, head pose estimation,
HOG feature extraction, and the SVM/RF classifier.
"""

from __future__ import annotations

import numpy as np
import pytest

from fatigue_detection.fatigue.classical.ear import DEFAULT_EAR_THRESHOLD, compute_ear
from fatigue_detection.fatigue.classical.mar import DEFAULT_MAR_THRESHOLD, compute_mar


class TestEAR:
    def test_compute_ear_shape(self) -> None:
        # TODO: provide 6 landmark points and verify scalar output
        pytest.skip("Not yet implemented")

    def test_open_eye_above_threshold(self) -> None:
        pytest.skip("Not yet implemented")

    def test_closed_eye_below_threshold(self) -> None:
        pytest.skip("Not yet implemented")


class TestMAR:
    def test_compute_mar_shape(self) -> None:
        pytest.skip("Not yet implemented")

    def test_normal_mouth_below_threshold(self) -> None:
        pytest.skip("Not yet implemented")

    def test_yawning_above_threshold(self) -> None:
        pytest.skip("Not yet implemented")


class TestHeadPose:
    def test_estimate_returns_three_angles(self) -> None:
        pytest.skip("Not yet implemented")


class TestClassicalClassifier:
    def test_build_feature_vector_length(self) -> None:
        pytest.skip("Not yet implemented")

    def test_predict_returns_valid_label(self) -> None:
        pytest.skip("Not yet implemented")
