"""

    *E♭ Major*

  The key of E♭ major.

"""

from ..._mode import MajorKey
from ....scale import Diatonic

from ._key import EfKey

__all__ = ["EfMajor"]


class EfMajor(
    EfKey,
    MajorKey,
    Diatonic,
):
    pass
