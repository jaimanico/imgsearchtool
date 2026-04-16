"""Command-line interface for the fatigue detection system.

Usage:
    fatigue-detect --mode live --pipeline classical
    fatigue-detect --mode eval --video path/to/video.mp4 --pipeline both
"""

from __future__ import annotations

import argparse
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Driver Fatigue Detection System with Gesture-Based Activation",
    )
    parser.add_argument(
        "--mode",
        choices=["live", "eval"],
        default="live",
        help="Run mode: live camera feed or evaluation on recorded video.",
    )
    parser.add_argument(
        "--pipeline",
        choices=["classical", "deep", "both"],
        default="classical",
        help="Which fatigue detection pipeline to use.",
    )
    parser.add_argument(
        "--video",
        type=Path,
        default=None,
        help="Path to video file (required for eval mode).",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("configs/default.yaml"),
        help="Path to YAML configuration file.",
    )
    parser.add_argument(
        "--no-gesture",
        action="store_true",
        help="Skip gesture activation and go directly to fatigue detection.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()

    if args.mode == "eval" and args.video is None:
        build_parser().error("--video is required when --mode is eval")

    # TODO: load config, instantiate app, run
    raise NotImplementedError(
        "CLI entrypoint not yet wired up — implement app.py first."
    )


if __name__ == "__main__":
    main()
