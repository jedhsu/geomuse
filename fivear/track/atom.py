"""

    *Atom*

  Models the atomic unit for user parametrization.

"""


from dataclasses import dataclass
from typing import Sequence

from .frame import Frame

__all__ = ["Atom"]


@dataclass
class Atom(
    tuple[Frame],
):
    index: int

    def __init__(
        self,
        beats: Sequence[Frame],
        index: int,
    ):
        assert index > 0, "Index must be positive"
        self.index = index

        super(Atom, self).__new__(
            tuple,
            beats,
        )

    def __repr__(self) -> str:
        return f"Bar {self.index}"
