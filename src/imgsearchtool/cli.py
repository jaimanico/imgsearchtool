import argparse
from pathlib import Path

from .pipeline import ImageSearchEngine


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Image search tool baseline CLI")
    parser.add_argument("--dataset", type=Path, required=True, help="Dataset root (class folders).")
    parser.add_argument("--method", type=str, default="color_hist", choices=["color_hist", "tiny_embed"])
    parser.add_argument("--query", type=Path, required=True, help="Query image path.")
    parser.add_argument("--top-k", type=int, default=5)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    engine = ImageSearchEngine(method=args.method)
    total = engine.build_index(args.dataset)
    results, query_ms = engine.query(args.query, top_k=args.top_k)

    print(f"Indexed images: {total}")
    print(f"Method: {args.method}")
    print(f"Query latency: {query_ms:.2f} ms")
    print("Top results:")
    for rank, r in enumerate(results, start=1):
        print(f"  {rank:>2}. label={r.label:<20} score={r.score:.5f} path={r.path}")


if __name__ == "__main__":
    main()
