"""Semi-automated frame annotation helper.

Reads a video, computes EAR/MAR values per frame using the classical pipeline,
and writes a CSV with columns: frame_id, EAR, MAR, head_yaw, head_pitch, fatigue_label.
The fatigue_label column is pre-filled based on thresholds but should be manually reviewed.

Usage:
    python scripts/annotate_frames.py --video data/raw/fatigue/session01.mp4 --output data/labels/session01.csv
"""

from __future__ import annotations

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Semi-automated frame annotator.")
    parser.add_argument("--video", type=Path, required=True, help="Input video path.")
    parser.add_argument("--output", type=Path, required=True, help="Output CSV path.")
    parser.add_argument("--ear-threshold", type=float, default=0.25)
    parser.add_argument("--mar-threshold", type=float, default=0.6)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    # TODO: iterate frames, compute EAR/MAR/head pose, write CSV
    raise NotImplementedError("Frame annotation not yet implemented.")


if __name__ == "__main__":
    main()
