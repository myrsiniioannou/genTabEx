from dataclasses import dataclass, field
from typing import Optional
from enum import Enum


@dataclass
class EvolutionType(int, Enum):
    stringAscending = 1
    stringDescending = 2
    stringDescendingAndLastStringDoubling = 3
    stringMultiplying = 4


@dataclass
class Evolution:
    type: EvolutionType
    fingeringNotNote: bool
    chordNumber: int = field(default_factory=list)
    string: int = field(default_factory=list)
    stringStep: Optional[int] = 1


@dataclass
class ArrowEvolution:
    chordNumber: int = field(default_factory=list)


@dataclass
class CustomEvolution:
    evolutions: int = field(default_factory=list)
    arrowEvolutions: ArrowEvolution = field(default_factory=list)