"""

    Phon

  Measures loudness.

"""

__all__ = ["Phon"]


class Phon(float):
    def __init__(self, value: float):
        """Wraps immutable float."""
        super(Phon, self).__new__(float, value)
