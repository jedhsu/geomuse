"""

    *Block*

"""

from dataclasses import dataclass
from typing import Sequence

from .bar import Bar

__all__ = ["Block"]


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

        super(Block, self).__new__(
            tuple,
            bars,
        )

    def __repr__(self) -> str:
        return f"Block {self.index}"
