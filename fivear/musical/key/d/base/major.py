"""

    *D Major*

  The key of D major.

"""

from ..._mode import MajorKey
from ....scale import Diatonic

from ._key import D_Key

__all__ = ["D_Major"]


class D_Major(
    D_Key,
    MajorKey,
    Diatonic,
):
    pass
