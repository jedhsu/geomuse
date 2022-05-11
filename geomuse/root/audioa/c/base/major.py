"""

    *C Major*

  The key of C major.

"""

from ..._mode import MajorKey
from ....scale import Diatonic

from ._key import C_Key

__all__ = ["C_Major"]


class C_Major(
    C_Key,
    MajorKey,
    Diatonic,
):
    pass
