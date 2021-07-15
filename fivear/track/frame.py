"""

    *Frame*

  Models the atomic unit of a frame.

  These can be "considered particles".

"""

from dataclasses import dataclass

__all__ = ["Frame"]


@dataclass
class Frame:
    index: int

    def __init__(
        self,
        index: int,
    ):
        self.index = index
        assert index >= 0, "Index must be positive."

    def __repr__(self) -> str:
        return f"Frame {self.index}"
