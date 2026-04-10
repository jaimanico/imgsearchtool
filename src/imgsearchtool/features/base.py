from abc import ABC, abstractmethod
from pathlib import Path

import numpy as np


class DescriptorExtractor(ABC):
    name: str

    @abstractmethod
    def extract(self, image_path: Path) -> np.ndarray:
        """Return a 1D float descriptor for the given image."""
