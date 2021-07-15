"""

    *B♯ Major*

  The key of B♯ major.

"""

from ..._mode import MajorKey
from ....scale import Diatonic

from ._key import BsKey

__all__ = ["BsMajor"]


class BsMajor(
    BsKey,
    MajorKey,
    Diatonic,
):
    pass
