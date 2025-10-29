"""
Tests for wordle_yq2397 package.
"""

import pytest
from wordle_yq2397 import validate_guess, check_guess, is_valid_word, calculate_game_score


def test_validate_guess():
    """
    Test the validate_guess function with various inputs.
    
    Tests:
    - Valid guesses (correct length, lowercase, alphabetic)
    - Invalid guesses (wrong length, uppercase, non-alphabetic)
    - Edge cases (empty string, None, non-string inputs)
    """
    # Valid guesses
    assert validate_guess("crane") == True
    assert validate_guess("apple") == True
    assert validate_guess("hello") == True

    # Invalid - wrong length
    assert validate_guess("cat") == False
    assert validate_guess("cranes") == False

    # Invalid - uppercase letters
    assert validate_guess("CRANE") == False
    assert validate_guess("Crane") == False

    # Invalid - non-alphabetic characters
    assert validate_guess("cra12") == False
    assert validate_guess("cr@ne") == False
    assert validate_guess("cran ") == False

    # Edge cases
    assert validate_guess("") == False
    assert validate_guess(None) == False
    assert validate_guess(12345) == False


@pytest.mark.parametrize("secret_word,guess,expected", [
    # Perfect match (all green)
    ("crane", "crane", [('c', 'green'), ('r', 'green'), ('a', 'green'), ('n', 'green'), ('e', 'green')]),
    
    # No matches (all gray)
    ("crane", "light", [('l', 'gray'), ('i', 'gray'), ('g', 'gray'), ('h', 'gray'), ('t', 'gray')]),
    
    # Mixed results
    ("crane", "react", [('r', 'yellow'), ('e', 'yellow'), ('a', 'green'), ('c', 'yellow'), ('t', 'gray')]),
    
    # Duplicate letters - "apple" vs "paper"
    ("apple", "paper", [('p', 'yellow'), ('a', 'yellow'), ('p', 'green'), ('e', 'yellow'), ('r', 'gray')]),
    
    # Duplicate letters - "crane" vs "green"
    ("crane", "green", [('g', 'gray'), ('r', 'green'), ('e', 'yellow'), ('e', 'gray'), ('n', 'yellow')]),
])
def test_check_guess_comprehensive(secret_word, guess, expected):
    """
    Test check_guess with multiple scenarios using parametrize.
    
    Covers:
    - Perfect matches (all green)
    - No matches (all gray)
    - Mixed results (combination of green, yellow, gray)
    - Duplicate letter handling
    """
    result = check_guess(secret_word, guess)
    assert result == expected, f"Failed for {secret_word} vs {guess}. Expected {expected}, got {result}"