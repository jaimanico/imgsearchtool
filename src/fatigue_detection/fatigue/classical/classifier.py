"""Classical fatigue classifier — SVM or Random Forest on aggregated features.

Aggregates EAR, MAR, head angle, and HOG features from the face ROI into
a feature vector. Trains an SVM or Random Forest on labelled segments.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


class ClassicalFatigueClassifier:
    """Train and run inference with a traditional ML classifier for fatigue detection."""

    def __init__(self, classifier_type: str = "svm") -> None:
        self.classifier_type = classifier_type
        self._model = None

    def build_feature_vector(
        self,
        ear: float,
        mar: float,
        yaw: float,
        pitch: float,
        roll: float,
        hog_features: np.ndarray,
    ) -> np.ndarray:
        """Concatenate all cues into a single feature vector."""
        raise NotImplementedError

    def train(self, features: np.ndarray, labels: np.ndarray) -> None:
        """Train the classifier on the given feature matrix and label array."""
        raise NotImplementedError

    def predict(self, feature_vector: np.ndarray) -> int:
        """Predict fatigue label (0 = alert, 1 = drowsy) for a single sample."""
        raise NotImplementedError

    def predict_proba(self, feature_vector: np.ndarray) -> float:
        """Return the probability of the drowsy class."""
        raise NotImplementedError

    def save(self, path: Path) -> None:
        """Serialize the trained model to disk."""
        raise NotImplementedError

    def load(self, path: Path) -> None:
        """Load a previously trained model from disk."""
        raise NotImplementedError
