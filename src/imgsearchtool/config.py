from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class EngineConfig:
    dataset_root: Path
    method: str = "color_hist"
    top_k: int = 5

    @classmethod
    def from_strings(cls, dataset_root: str, method: str = "color_hist", top_k: int = 5) -> "EngineConfig":
        return cls(dataset_root=Path(dataset_root), method=method, top_k=top_k)
