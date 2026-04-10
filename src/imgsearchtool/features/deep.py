from pathlib import Path

import numpy as np

from .base import DescriptorExtractor

try:
    from PIL import Image
except ImportError as exc:  # pragma: no cover
    raise ImportError("Pillow is required for the tiny embedding baseline.") from exc


class TinyEmbeddingExtractor(DescriptorExtractor):
    """
    Placeholder for deep features.
    This creates a compact embedding from downsampled grayscale pixels.
    Replace later with a CNN/ViT embedding model.
    """

    name = "tiny_embed"

    def __init__(self, size: int = 32, out_dim: int = 128, seed: int = 42) -> None:
        self.size = size
        self.out_dim = out_dim
        rng = np.random.default_rng(seed)
        in_dim = size * size
        self.proj = rng.standard_normal((out_dim, in_dim)).astype(np.float32)

    def extract(self, image_path: Path) -> np.ndarray:
        img = Image.open(image_path).convert("L").resize((self.size, self.size))
        x = np.asarray(img, dtype=np.float32).reshape(-1) / 255.0
        vec = self.proj @ x
        norm = np.linalg.norm(vec)
        if norm > 0:
            vec /= norm
        return vec.astype(np.float32)
