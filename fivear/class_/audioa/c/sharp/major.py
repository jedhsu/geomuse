"""

    *C♯ Major*

  The key of C♯ major.

"""

from ..._mode import MajorKey
from ....scale import Diatonic

from ._key import CsKey

__all__ = ["CsMajor"]


class CsMajor(
    CsKey,
    MajorKey,
    Diatonic,
):
    pass
