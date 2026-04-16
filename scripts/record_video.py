"""Helper script to record video from a webcam for dataset creation.

Recording protocol: camera on dashboard, pointing at driver's face,
slight upward angle. Record in at least 3 lighting conditions.

Usage:
    python scripts/record_video.py --output data/raw/fatigue/session01.mp4 --duration 300
"""

from __future__ import annotations

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Record webcam video for dataset.")
    parser.add_argument("--output", type=Path, required=True, help="Output video file path.")
    parser.add_argument("--duration", type=int, default=120, help="Recording duration in seconds.")
    parser.add_argument("--device", type=int, default=0, help="Camera device ID.")
    parser.add_argument("--fps", type=int, default=30, help="Target FPS.")
    parser.add_argument("--width", type=int, default=640)
    parser.add_argument("--height", type=int, default=480)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    # TODO: open camera, record frames, save to output path
    raise NotImplementedError("Video recording not yet implemented.")


if __name__ == "__main__":
    main()
