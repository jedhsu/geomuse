"""

    *G♯ Major*

  The key of G♯ major.

"""

from ..._mode import MajorKey
from ....scale import Diatonic

from ._key import GsKey

__all__ = ["GsMajor"]


class GsMajor(
    GsKey,
    MajorKey,
    Diatonic,
):
    pass
