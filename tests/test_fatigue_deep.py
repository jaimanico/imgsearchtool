"""Tests for the deep learning fatigue detection pipeline.

Covers: eye CNN, mouth CNN, temporal LSTM, and fusion logic.
"""

from __future__ import annotations

import pytest


class TestEyeCNN:
    def test_predict_returns_class_and_confidence(self) -> None:
        pytest.skip("Not yet implemented")

    def test_extract_features_shape(self) -> None:
        pytest.skip("Not yet implemented")


class TestMouthCNN:
    def test_predict_returns_class_and_confidence(self) -> None:
        pytest.skip("Not yet implemented")


class TestTemporalModel:
    def test_predict_from_sequence(self) -> None:
        pytest.skip("Not yet implemented")


class TestFusion:
    def test_fuse_scores_range(self) -> None:
        # fatigue score should be in [0, 1]
        pytest.skip("Not yet implemented")
