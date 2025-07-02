"""Practice writing recursive functions."""

__author__ = "730736689"


def f(n: int, k: int) -> int:  # recursive function definition
    """Returns n multiplied by k."""
    if n == 0:  # base case
        return 0
    else:  # recursive rule
        return k + f(n - 1, k)
