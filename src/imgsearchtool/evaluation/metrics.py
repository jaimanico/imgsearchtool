from collections import defaultdict


def top_k_accuracy(ground_truth: list[str], predictions: list[list[str]], k: int = 1) -> float:
    if not ground_truth:
        return 0.0
    hits = 0
    for gt, pred in zip(ground_truth, predictions):
        if gt in pred[:k]:
            hits += 1
    return hits / len(ground_truth)


def precision_at_k(ground_truth: list[str], predictions: list[list[str]], k: int = 5) -> float:
    if not ground_truth:
        return 0.0
    total = 0.0
    for gt, pred in zip(ground_truth, predictions):
        top = pred[:k]
        if not top:
            continue
        relevant = sum(1 for p in top if p == gt)
        total += relevant / len(top)
    return total / len(ground_truth)


def mean_average_precision(ground_truth: list[str], predictions: list[list[str]]) -> float:
    if not ground_truth:
        return 0.0
    ap_values = []
    for gt, pred in zip(ground_truth, predictions):
        num_hits = 0
        precision_sum = 0.0
        for rank, label in enumerate(pred, start=1):
            if label == gt:
                num_hits += 1
                precision_sum += num_hits / rank
        ap_values.append((precision_sum / num_hits) if num_hits else 0.0)
    return sum(ap_values) / len(ap_values)


def per_class_counts(labels: list[str]) -> dict[str, int]:
    counts = defaultdict(int)
    for label in labels:
        counts[label] += 1
    return dict(counts)
