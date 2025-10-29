"""
Wordle game package.

A package for playing Wordle with validation, checking, and scoring functions.
"""

# read version from installed package
from importlib.metadata import version
__version__ = version("wordle_yq2397")

from wordle_yq2397.wordle_yq2397 import (
    validate_guess,
    check_guess,
    is_valid_word,
    calculate_game_score,
)

__all__ = [
    "validate_guess",
    "check_guess",
    "is_valid_word",
    "calculate_game_score",
]