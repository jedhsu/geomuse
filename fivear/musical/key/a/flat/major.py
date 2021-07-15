"""

    *A♭ Major*

  The key of A♭ major.

"""

from ..._mode import MajorKey
from ....scale import Diatonic

from ._key import AfKey

__all__ = ["AfMajor"]


class AfMajor(
    AfKey,
    MajorKey,
    Diatonic,
):
    pass
