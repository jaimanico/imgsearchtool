"""Training loop for deep learning fatigue models.

Handles training of eye CNN, mouth CNN, and temporal LSTM models
with checkpointing and logging. Supports pretraining on external datasets
and fine-tuning on in-car recordings.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


class Trainer:
    """Generic training loop for PyTorch fatigue models."""

    def __init__(
        self,
        model_name: str,
        learning_rate: float = 0.001,
        batch_size: int = 32,
        epochs: int = 30,
        checkpoint_dir: Path = Path("models/deep"),
    ) -> None:
        self.model_name = model_name
        self.learning_rate = learning_rate
        self.batch_size = batch_size
        self.epochs = epochs
        self.checkpoint_dir = checkpoint_dir

    def train(
        self,
        train_data: np.ndarray,
        train_labels: np.ndarray,
        val_data: np.ndarray | None = None,
        val_labels: np.ndarray | None = None,
    ) -> dict[str, list[float]]:
        """Run the full training loop.

        Returns:
            Dict with 'train_loss', 'val_loss', 'val_accuracy' histories.
        """
        raise NotImplementedError

    def save_checkpoint(self, epoch: int, metrics: dict) -> Path:
        """Save model checkpoint with metadata."""
        raise NotImplementedError

    def load_checkpoint(self, path: Path) -> None:
        """Resume training from a checkpoint."""
        raise NotImplementedError
