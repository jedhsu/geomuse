"""

    *Pitch, Display*

  The display interface for pitch.

"""

from ._pitch import Pitch

__all__ = ["Display"]


class Display(
    Pitch,
):
    def __repr__(self):
        return f"{self.key}{self.level}"
