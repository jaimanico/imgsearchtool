from .base import DescriptorExtractor
from .classical import ColorHistogramExtractor
from .deep import TinyEmbeddingExtractor


def build_extractor(method: str) -> DescriptorExtractor:
    method = method.lower().strip()
    if method == "color_hist":
        return ColorHistogramExtractor()
    if method == "tiny_embed":
        return TinyEmbeddingExtractor()
    raise ValueError(f"Unknown method: {method}")
