"""Finite state machine for gesture sequence activation.

State machine: WAITING -> GESTURE_1_DETECTED -> GESTURE_2_DETECTED -> ACTIVATED.
Tracks a timestamp at each state transition; if delta exceeds the window, resets to WAITING.
"""

from __future__ import annotations

import time
from enum import Enum, auto

from .gesture_classifier import Gesture


class GateState(Enum):
    WAITING = auto()
    GESTURE_1_DETECTED = auto()
    GESTURE_2_DETECTED = auto()
    ACTIVATED = auto()


class GestureGate:
    """Manages the gesture activation sequence with time-window enforcement."""

    def __init__(
        self,
        sequence: list[str] | None = None,
        time_window_sec: float = 6.0,
        min_hold_sec: float = 0.5,
    ) -> None:
        self.sequence = sequence or ["open_palm", "thumbs_up"]
        self.time_window_sec = time_window_sec
        self.min_hold_sec = min_hold_sec
        self._state = GateState.WAITING
        self._transition_time: float | None = None
        self._hold_start: float | None = None

    @property
    def state(self) -> GateState:
        return self._state

    @property
    def is_activated(self) -> bool:
        return self._state == GateState.ACTIVATED

    def update(self, gesture: Gesture) -> GateState:
        """Feed a classified gesture and advance the state machine.

        Returns the new state after processing.
        """
        raise NotImplementedError

    def reset(self) -> None:
        """Reset the gate to WAITING state."""
        self._state = GateState.WAITING
        self._transition_time = None
        self._hold_start = None
