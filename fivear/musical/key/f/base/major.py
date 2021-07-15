"""

    *F Major*

  The key of F major.

"""

from ..._mode import MajorKey
from ....scale import Diatonic

from ._key import F_Key

__all__ = ["F_Major"]


class F_Major(
    F_Key,
    MajorKey,
    Diatonic,
):
    pass
