"""

    *A♯ Major*

  The key of A♯ major.

"""

from ..._mode import MajorKey
from ....scale import Diatonic

from ._key import AsKey

__all__ = ["AsMajor"]


class AsMajor(
    AsKey,
    MajorKey,
    Diatonic,
):
    pass
