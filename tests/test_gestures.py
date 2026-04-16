"""Tests for the gesture recognition module (Module 1).

Covers: hand detection, gesture classification, state machine transitions,
timeout reset, and false acceptance scenarios.
"""

from __future__ import annotations

import pytest

from fatigue_detection.gesture.gesture_classifier import Gesture, GestureClassifier
from fatigue_detection.gesture.state_machine import GateState, GestureGate


class TestGestureClassifier:
    def test_classify_returns_gesture_enum(self) -> None:
        # TODO: provide sample landmarks and check return type
        pytest.skip("Not yet implemented")

    def test_open_palm_detection(self) -> None:
        pytest.skip("Not yet implemented")

    def test_thumbs_up_detection(self) -> None:
        pytest.skip("Not yet implemented")


class TestGestureGate:
    def test_initial_state_is_waiting(self) -> None:
        gate = GestureGate()
        assert gate.state == GateState.WAITING

    def test_reset_returns_to_waiting(self) -> None:
        gate = GestureGate()
        gate.reset()
        assert gate.state == GateState.WAITING
        assert not gate.is_activated

    def test_correct_sequence_activates(self) -> None:
        # TODO: feed correct gestures and assert ACTIVATED
        pytest.skip("Not yet implemented")

    def test_wrong_order_resets(self) -> None:
        # TODO: feed gestures in wrong order and assert WAITING
        pytest.skip("Not yet implemented")

    def test_timeout_resets(self) -> None:
        # TODO: simulate timeout between gestures
        pytest.skip("Not yet implemented")
