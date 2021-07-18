"""

    *F♯ Major*

  The key of F♯ major.

"""

from ..._mode import MajorKey
from ....scale import Diatonic

from ._key import FsKey

__all__ = ["FsMajor"]


class FsMajor(
    FsKey,
    MajorKey,
    Diatonic,
):
    pass
