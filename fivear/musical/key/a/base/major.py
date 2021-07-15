"""

    *A Major*

  The key of A major.

"""

from ..._mode import MajorKey
from ....scale import Diatonic

from ._key import A_Key

__all__ = ["A_Major"]


class A_Major(
    A_Key,
    MajorKey,
    Diatonic,
):
    pass
