# Driver Fatigue Detection System

A computer vision system that detects driver fatigue using a gesture-based activation gate.
The system remains inactive by default and activates only when the driver performs a predefined
gesture sequence (open palm followed by thumbs up within a time window). Once active, it
continuously monitors for signs of fatigue — eye closure, yawning, head drooping — using both
classical (EAR/MAR + SVM) and deep learning (MobileNetV2 + LSTM) pipelines.

## Project Structure

```text
├── pyproject.toml              # Package metadata and dependencies
├── requirements.txt            # Pinned dependencies for reproducibility
├── configs/
│   └── default.yaml            # Default thresholds and parameters
├── data/
│   ├── raw/gestures/           # Gesture sequence recordings
│   ├── raw/fatigue/            # Fatigue session recordings
│   ├── processed/              # Extracted frames, cropped ROIs
│   ├── labels/                 # CSV annotations (frame_id, EAR, MAR, ...)
│   └── external/               # External pre-training datasets
├── models/
│   ├── classical/              # Serialized SVM / Random Forest models
│   └── deep/                   # CNN/LSTM checkpoints, ONNX exports
├── experiments/                # MLflow runs / CSV experiment logs
├── notebooks/                  # Jupyter notebooks for EDA / prototyping
├── scripts/                    # Standalone utility scripts
├── tests/                      # Unit and integration tests
└── src/fatigue_detection/      # Main package
    ├── gesture/                # Module 1: gesture-based activation gate
    ├── fatigue/                # Module 2: fatigue detection
    │   ├── classical/          #   Classical pipeline (EAR/MAR/HOG + SVM)
    │   └── deep/               #   Deep learning pipeline (MobileNet + LSTM)
    ├── evaluation/             # Metrics, comparison, visualization
    ├── data/                   # Dataset loading, preprocessing, augmentation
    └── utils/                  # Video capture, drawing overlays, timing
```

## Quick Start

1. Install in editable mode:

```bash
pip install -e .
```

2. Run the live detection system:

```bash
fatigue-detect --mode live --pipeline classical
```

3. Evaluate on recorded video:

```bash
fatigue-detect --mode eval --video data/raw/fatigue/session01.mp4 --pipeline both
```

## System Flow

```
CAMERA → [Gesture Gate] → (activated?) → [Fatigue Detection] → ALERT / LOG
```

- **Gesture Gate**: MediaPipe Hands → finger-angle rules → state machine (WAITING → G1 → G2 → ACTIVATED)
- **Classical Pipeline**: dlib 68-landmarks → EAR/MAR/head pose → HOG + SVM
- **Deep Pipeline**: MediaPipe Face Mesh → eye/mouth ROI CNNs → LSTM temporal model → fusion
