"""

    *C♭ Major*

  The key of C♭ major.

"""

from ..._mode import MajorKey
from ....scale import Diatonic

from ._key import CfKey

__all__ = ["CfMajor"]


class CfMajor(
    CfKey,
    MajorKey,
    Diatonic,
):
    pass
