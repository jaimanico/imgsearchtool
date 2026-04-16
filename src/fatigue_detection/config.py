"""Central configuration loaded from YAML with sensible defaults.

Corresponds to configs/default.yaml.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


@dataclass
class GestureConfig:
    sequence: list[str] = field(default_factory=lambda: ["open_palm", "thumbs_up"])
    time_window_sec: float = 6.0
    min_hold_sec: float = 0.5


@dataclass
class FatigueConfig:
    ear_threshold: float = 0.25
    ear_consec_frames: int = 15
    mar_threshold: float = 0.6
    mar_consec_frames: int = 10
    head_pitch_threshold: float = 20.0
    head_yaw_threshold: float = 30.0
    rolling_avg_window: int = 15
    alert_consec_frames: int = 10


@dataclass
class CameraConfig:
    device_id: int = 0
    width: int = 640
    height: int = 480
    fps: int = 30


@dataclass
class ClassicalConfig:
    face_detector: str = "dlib_hog"
    landmark_model: str = "shape_predictor_68_face_landmarks.dat"
    classifier: str = "svm"


@dataclass
class DeepConfig:
    face_detector: str = "mediapipe"
    eye_model: str = "mobilenetv2"
    mouth_model: str = "mobilenetv2"
    temporal_model: str = "lstm"
    input_size: int = 64
    sequence_length: int = 16
    batch_size: int = 32
    learning_rate: float = 0.001
    epochs: int = 30


@dataclass
class EvalConfig:
    train_ratio: float = 0.70
    val_ratio: float = 0.15
    test_ratio: float = 0.15
    split_by: str = "subject"


@dataclass
class PathsConfig:
    raw_data: Path = Path("data/raw")
    processed_data: Path = Path("data/processed")
    labels: Path = Path("data/labels")
    external_data: Path = Path("data/external")
    models: Path = Path("models")
    experiments: Path = Path("experiments")


@dataclass
class SystemConfig:
    gesture: GestureConfig = field(default_factory=GestureConfig)
    fatigue: FatigueConfig = field(default_factory=FatigueConfig)
    camera: CameraConfig = field(default_factory=CameraConfig)
    classical: ClassicalConfig = field(default_factory=ClassicalConfig)
    deep: DeepConfig = field(default_factory=DeepConfig)
    evaluation: EvalConfig = field(default_factory=EvalConfig)
    paths: PathsConfig = field(default_factory=PathsConfig)

    @classmethod
    def from_yaml(cls, path: str | Path) -> SystemConfig:
        """Load configuration from a YAML file, falling back to defaults for missing keys."""
        with open(path) as f:
            raw: dict[str, Any] = yaml.safe_load(f) or {}

        return cls(
            gesture=GestureConfig(**raw.get("gesture", {})),
            fatigue=FatigueConfig(**raw.get("fatigue", {})),
            camera=CameraConfig(**raw.get("camera", {})),
            classical=ClassicalConfig(**raw.get("classical", {})),
            deep=DeepConfig(**raw.get("deep", {})),
            evaluation=EvalConfig(**raw.get("evaluation", {})),
            paths=PathsConfig(
                **{k: Path(v) for k, v in raw.get("paths", {}).items()}
            ),
        )
