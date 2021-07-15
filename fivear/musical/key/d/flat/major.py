"""

    *D♭ Major*

  The key of D♭ major.

"""

from ..._mode import MajorKey
from ....scale import Diatonic

from ._key import DfKey

__all__ = ["DfMajor"]


class DfMajor(
    DfKey,
    MajorKey,
    Diatonic,
):
    pass
