"""

    *Beat*

  Models a musical beat.

  Contains 4 steps.

"""

from dataclasses import dataclass
from typing import Sequence

from ._space import Space
from .step import Step

__all__ = ["Beat"]


@dataclass
class Beat(
    tuple[Step],
    Space,
):
    index: int

    def __init__(
        self,
        steps: Sequence[Step],
        index: int,
    ):
        self.index = index
        assert 1 <= index <= 4, "Not a valid index."
        assert len(steps) == 4, "Must have four steps in a beat."

        super(Beat, self).__new__(
            tuple,
            steps,
        )

    def __repr__(self) -> str:
        return f"Beat-{self.index}"
