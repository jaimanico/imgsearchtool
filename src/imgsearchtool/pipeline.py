from pathlib import Path
from time import perf_counter

import numpy as np

from .dataset import scan_dataset
from .features.factory import build_extractor
from .index.bruteforce import BruteForceIndex, SearchResult


class ImageSearchEngine:
    def __init__(self, method: str = "color_hist") -> None:
        self.method = method
        self.extractor = build_extractor(method)
        self.index = BruteForceIndex()

    def build_index(self, dataset_root: Path) -> int:
        items = scan_dataset(dataset_root)
        if not items:
            raise ValueError(f"No images found under {dataset_root}")

        vectors: list[np.ndarray] = []
        paths: list[Path] = []
        labels: list[str] = []
        for item in items:
            vectors.append(self.extractor.extract(item.path))
            paths.append(item.path)
            labels.append(item.label)

        matrix = np.stack(vectors, axis=0)
        self.index.build(matrix, paths, labels)
        return len(items)

    def query(self, image_path: Path, top_k: int = 5) -> tuple[list[SearchResult], float]:
        start = perf_counter()
        qvec = self.extractor.extract(image_path)
        results = self.index.query(qvec, top_k=top_k)
        elapsed_ms = (perf_counter() - start) * 1000.0
        return results, elapsed_ms
