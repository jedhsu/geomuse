"""

    *G Major*

  The key of G major.

"""

from ..._mode import MajorKey
from ....scale import Diatonic

from ._key import G_Key

__all__ = ["G_Major"]


class G_Major(
    G_Key,
    MajorKey,
    Diatonic,
):
    pass
