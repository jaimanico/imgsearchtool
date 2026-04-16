"""Classical fatigue detection pipeline.

dlib landmarks -> EAR/MAR/head pose -> HOG features -> SVM/RF classifier.
"""

from .classifier import ClassicalFatigueClassifier

__all__ = ["ClassicalFatigueClassifier"]
