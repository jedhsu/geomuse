"""

    *D♯ Major*

  The key of D♯ major.

"""

from ..._mode import MajorKey
from ....scale import Diatonic

from ._key import DsKey

__all__ = ["DsMajor"]


class DsMajor(
    DsKey,
    MajorKey,
    Diatonic,
):
    pass
