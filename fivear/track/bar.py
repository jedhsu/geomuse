"""

    *Bar*

  Models a musical bar.

"""

from dataclasses import dataclass
from typing import Sequence

from .beat import Beat

__all__ = ["Bar"]


@dataclass
class Bar(
    tuple[Beat],
):
    index: int

    def __init__(
        self,
        beats: Sequence[Beat],
        index: int,
    ):
        self.index = index
        assert 1 <= index <= 4, "Not a valid index."
        assert len(beats) == 4, "Must have four beats in a bar."

        super(Bar, self).__new__(
            tuple,
            beats,
        )

    def __repr__(self) -> str:
        return f"Bar {self.index}"
