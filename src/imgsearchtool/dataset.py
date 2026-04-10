from dataclasses import dataclass
from pathlib import Path


SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}


@dataclass(slots=True)
class ImageItem:
    path: Path
    label: str


def scan_dataset(root: Path) -> list[ImageItem]:
    """
    Expected layout:
    root/
      place_a/
        img1.jpg
      place_b/
        img2.jpg
    """
    if not root.exists():
        raise FileNotFoundError(f"Dataset root not found: {root}")

    items: list[ImageItem] = []
    for class_dir in sorted(p for p in root.iterdir() if p.is_dir()):
        label = class_dir.name
        for file in sorted(class_dir.rglob("*")):
            if file.is_file() and file.suffix.lower() in SUPPORTED_EXTENSIONS:
                items.append(ImageItem(path=file, label=label))
    return items
