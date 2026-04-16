"""Deep learning fatigue detection pipeline.

MediaPipe Face Mesh -> eye/mouth ROI CNNs -> LSTM temporal model -> fusion.
"""

from .fusion import DeepFatiguePipeline

__all__ = ["DeepFatiguePipeline"]
