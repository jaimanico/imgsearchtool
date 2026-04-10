# imgsearchtool

Baseline project for visual place recognition (IE Tower area) with a focus on:
- retrieval accuracy
- query speed / latency
- reproducible comparison between methods

## Project Structure

```text
imgsearchtool/
  data/
    raw/                  # captured images from IE Tower area
    processed/            # optional resized/cleaned versions
  experiments/            # logs, result tables, plots
  src/imgsearchtool/
    dataset.py            # dataset scanning and labels
    pipeline.py           # index + query orchestration
    cli.py                # minimal command-line interface
    features/
      classical.py        # color histogram baseline
      deep.py             # tiny embedding placeholder baseline
    index/
      bruteforce.py       # brute-force nearest-neighbor search
    evaluation/
      metrics.py          # top-k, precision@k, mAP
  pyproject.toml
  README.md
```

## Dataset Layout

Organize images by place label:

```text
data/raw/
  place_entrance/
    img_001.jpg
    img_002.jpg
  place_stairs/
    img_101.jpg
```

Each folder name is treated as a class/place label.

## Quick Start

1) Install package in editable mode:

```bash
pip install -e .
```

2) Run a query with the baseline method:

```bash
imgsearch --dataset data/raw --query data/raw/place_entrance/img_001.jpg --method color_hist --top-k 5
```

3) Try the second baseline for comparison:

```bash
imgsearch --dataset data/raw --query data/raw/place_entrance/img_001.jpg --method tiny_embed --top-k 5
```

## What Is Already Implemented

- End-to-end pipeline: dataset scan -> feature extraction -> indexing -> retrieval
- Two basic methods for fair method-vs-method experiments:
  - `color_hist` (classical handcrafted descriptor)
  - `tiny_embed` (placeholder embedding-style descriptor)
- Retrieval metrics ready for experiments:
  - Top-K accuracy
  - Precision@K
  - mAP

## Next Steps (to amplify later)

- Add a real deep embedding model (e.g., pretrained CNN/ViT)
- Add train/val/test splits and experiment protocol scripts
- Replace brute-force search with an approximate nearest-neighbor index
- Add robust evaluation scripts and plotting
- Add memory/time profiling and ablation studies