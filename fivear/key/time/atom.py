"""

    *Atom*

  Smallest controllable unit of space.

"""


from dataclasses import dataclass
from typing import Sequence

from ._space import Space
from .quark import Quark

__all__ = ["Atom"]


@dataclass
class Atom(
    tuple[Quark],
    Space,
):
    index: int

    def __init__(
        self,
        beats: Sequence[Quark],
        index: int,
    ):
        assert index > 0, "Index must be positive"
        self.index = index

        super(Atom, self).__new__(
            tuple,
            beats,
        )

    def __repr__(self) -> str:
        return f"Atom-{self.index}"
