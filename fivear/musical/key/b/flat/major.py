"""

    *B♭ Major*

  The key of B♭ major.

"""

from ..._mode import MajorKey
from ....scale import Diatonic

from ._key import BfKey

__all__ = ["BfMajor"]


class BfMajor(
    BfKey,
    MajorKey,
    Diatonic,
):
    pass
