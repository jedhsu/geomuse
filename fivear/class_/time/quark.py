"""

    *Quark*

  An irreducible sample frame.

  # [TODO] is this Unit Quark?

"""

from dataclasses import dataclass

from ._space import Space

__all__ = ["Quark"]


@dataclass
class Quark(
    Space,
):
    index: int

    def __init__(
        self,
        index: int,
    ):
        self.index = index
        assert index >= 0, "Index must be positive."

    def __repr__(self) -> str:
        return f"Quark-{self.index}"
