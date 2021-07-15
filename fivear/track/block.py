"""

    *Block*

  Models a musical measure.

"""

from dataclasses import dataclass
from typing import Sequence

from .bar import Bar

__all__ = ["Bar"]


@dataclass
class Block(
    tuple[Bar],
):
    index: int

    def __init__(
        self,
        bars: Sequence[Bar],
        index: int,
    ):
        self.index = index
        assert 1 <= index <= 4, "Not a valid index."
        assert len(bars) == 4, "Must have four bars in a block."

        super(Block, self).__new__(
            tuple,
            bars,
        )

    def __repr__(self) -> str:
        return f"Block {self.index}"
