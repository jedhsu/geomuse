"""

    *E♯ Major*

  The key of E♯ major.

"""

from ..._mode import MajorKey
from ....scale import Diatonic

from ._key import EsKey

__all__ = ["EsMajor"]


class EsMajor(
    EsKey,
    MajorKey,
    Diatonic,
):
    pass
