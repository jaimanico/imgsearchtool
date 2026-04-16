"""Export a trained PyTorch model to ONNX format for fast CPU inference.

Exports the trained model to ONNX for fast CPU inference via cv2.dnn.
Target: <30ms inference per frame.

Usage:
    python scripts/export_onnx.py --checkpoint models/deep/eye_cnn_best.pt --output models/deep/eye_cnn.onnx
"""

from __future__ import annotations

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export PyTorch model to ONNX.")
    parser.add_argument("--checkpoint", type=Path, required=True, help="Path to .pt checkpoint.")
    parser.add_argument("--output", type=Path, required=True, help="Output .onnx file path.")
    parser.add_argument("--input-size", type=int, default=64, help="Model input image size.")
    parser.add_argument("--model-type", choices=["eye_cnn", "mouth_cnn", "temporal"], required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    # TODO: load model, create dummy input, torch.onnx.export
    raise NotImplementedError("ONNX export not yet implemented.")


if __name__ == "__main__":
    main()
