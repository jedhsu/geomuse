"""

    *Step*

  Models a musical step.

"""

from dataclasses import dataclass
from typing import Sequence

from .block import Block
from .frames import Frames

__all__ = ["Step"]


@dataclass
class _Step:
    index: int

    frames: Frames
    blocks: Sequence[Block]


class _Step_(_Step):
    ...


class _Display_(_Step):
    def __getitem__(self):
        ...


class Step(
    _Display_,
    _Step_,
    _Step,
):
    def __init__(self, index: int, blocks_per_step: int):
        assert 1 <= index <= 4, "Not a valid step index."

        blocks = tuple([Block(i) for i in range(1, blocks_per_step)])
        super().__init__(index, blocks)
