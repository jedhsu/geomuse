"""

    *G♭ Major*

  The key of G♭ major.

"""

from ..._mode import MajorKey
from ....scale import Diatonic

from ._key import GfKey

__all__ = ["GfMajor"]


class GfMajor(
    GfKey,
    MajorKey,
    Diatonic,
):
    pass
