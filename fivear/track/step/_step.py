"""

    *Step*

  Models a musical step.

  Contains n atoms.

"""

from dataclasses import dataclass
from typing import Sequence

from .atom import Atom

__all__ = ["Step"]


@dataclass
class Step(
    tuple[Atom],
):
    index: int

    def __init__(
        self,
        bars: Sequence[Atom],
        index: int,
    ):
        self.index = index
        assert 1 <= index <= 4, "Not a valid index."

        super(Step, self).__new__(
            tuple,
            bars,
        )

    def __repr__(self) -> str:
        return f"Step {self.index}"
