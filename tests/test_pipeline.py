"""Integration tests for the full end-to-end pipeline.

Tests the flow: camera frame -> gesture gate -> fatigue detection -> alert.
"""

from __future__ import annotations

import pytest

from fatigue_detection.config import SystemConfig


class TestSystemConfig:
    def test_default_config_loads(self) -> None:
        config = SystemConfig()
        assert config.fatigue.ear_threshold == 0.25
        assert config.gesture.time_window_sec == 6.0

    def test_from_yaml(self, tmp_path) -> None:
        yaml_content = "gesture:\\n  time_window_sec: 8.0\\n"
        config_file = tmp_path / "test.yaml"
        config_file.write_text(yaml_content.replace("\\n", "\n"))
        config = SystemConfig.from_yaml(config_file)
        assert config.gesture.time_window_sec == 8.0


class TestFatigueDetectionApp:
    def test_process_frame_returns_dict(self) -> None:
        # TODO: create app with default config and test process_frame
        pytest.skip("Not yet implemented")

    def test_gesture_gate_blocks_fatigue(self) -> None:
        # Before activation, fatigue detection should not run
        pytest.skip("Not yet implemented")

    def test_full_pipeline_smoke(self) -> None:
        # End-to-end smoke test with a synthetic frame
        pytest.skip("Not yet implemented")
