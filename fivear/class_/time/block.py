"""

    *Block*

  A measure.

"""

from dataclasses import dataclass
from typing import Sequence

from ._space import Space
from .bar import Bar

__all__ = ["Block"]


@dataclass
class Block(
    tuple[Bar],
    Space,
):
    index: int

    def __init__(
        self,
        bars: Sequence[Bar],
        index: int,
    ):
        self.index = index

        super(Block, self).__new__(
            tuple,
            bars,
        )

    def __repr__(self) -> str:
        return f"Block-{self.index}"
