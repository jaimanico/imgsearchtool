from pathlib import Path

import numpy as np

from .base import DescriptorExtractor

try:
    from PIL import Image
except ImportError as exc:  # pragma: no cover
    raise ImportError("Pillow is required for the color histogram baseline.") from exc


class ColorHistogramExtractor(DescriptorExtractor):
    """
    Very fast and simple baseline:
    - convert to RGB
    - compute 3D color histogram
    - L1 normalize
    """

    name = "color_hist"

    def __init__(self, bins_per_channel: int = 8) -> None:
        self.bins_per_channel = bins_per_channel

    def extract(self, image_path: Path) -> np.ndarray:
        img = Image.open(image_path).convert("RGB")
        arr = np.asarray(img, dtype=np.uint8)
        hist, _ = np.histogramdd(
            arr.reshape(-1, 3),
            bins=(self.bins_per_channel, self.bins_per_channel, self.bins_per_channel),
            range=((0, 256), (0, 256), (0, 256)),
        )
        vec = hist.astype(np.float32).reshape(-1)
        norm = np.sum(vec)
        if norm > 0:
            vec /= norm
        return vec
