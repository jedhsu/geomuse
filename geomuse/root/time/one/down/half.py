"""

    *One-Down-Half*

  A half note on the downbeat of one.

"""

from dataclasses import dataclass

__all__ = ["OneDownHalf"]


@dataclass
class OneDownHalf(
    OneDown,
    HalfNote,
):
    pass
