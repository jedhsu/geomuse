"""

    *B Major*

  The key of B major.

"""

from ..._mode import MajorKey
from ....scale import Diatonic

from ._key import B_Key

__all__ = ["B_Major"]


class B_Major(
    B_Key,
    MajorKey,
    Diatonic,
):
    pass
