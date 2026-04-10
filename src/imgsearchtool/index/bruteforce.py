from dataclasses import dataclass
from pathlib import Path

import numpy as np


@dataclass(slots=True)
class SearchResult:
    path: Path
    label: str
    score: float


class BruteForceIndex:
    def __init__(self) -> None:
        self._vectors: np.ndarray | None = None
        self._paths: list[Path] = []
        self._labels: list[str] = []

    def build(self, vectors: np.ndarray, paths: list[Path], labels: list[str]) -> None:
        if len(vectors) != len(paths) or len(paths) != len(labels):
            raise ValueError("Vectors, paths, and labels must have the same length.")
        self._vectors = vectors.astype(np.float32)
        self._paths = paths
        self._labels = labels

    def query(self, query_vector: np.ndarray, top_k: int = 5) -> list[SearchResult]:
        if self._vectors is None:
            raise RuntimeError("Index has not been built yet.")
        q = query_vector.astype(np.float32)
        diff = self._vectors - q[None, :]
        dists = np.linalg.norm(diff, axis=1)
        ids = np.argsort(dists)[:top_k]
        return [
            SearchResult(path=self._paths[i], label=self._labels[i], score=float(dists[i]))
            for i in ids
        ]
