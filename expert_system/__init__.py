"""
CareerWise AI - Expert System Package
Exposes core modules for knowledge representation, inference, and explanations.
"""

from expert_system.knowledge_base import (
    CAREERS,
    SKILLS_METADATA,
    INTERESTS_METADATA,
    SUBJECTS_METADATA,
    WORK_STYLES_METADATA,
    PRODUCTION_RULES,
    PRESET_PROFILES
)
from expert_system.forward_chaining import ForwardChainingEngine
from expert_system.backward_chaining import BackwardChainingEngine
from expert_system.explanation import ExplanationFacility
from expert_system.roadmap_generator import RoadmapGenerator

__all__ = [
    "CAREERS",
    "SKILLS_METADATA",
    "INTERESTS_METADATA",
    "SUBJECTS_METADATA",
    "WORK_STYLES_METADATA",
    "PRODUCTION_RULES",
    "PRESET_PROFILES",
    "ForwardChainingEngine",
    "BackwardChainingEngine",
    "ExplanationFacility",
    "RoadmapGenerator"
]
