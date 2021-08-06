"""

    *E Major*

  The key of E major.

"""

from ..._mode import MajorKey
from ....scale import Diatonic

from ._key import E_Key

__all__ = ["E_Major"]


class E_Major(
    E_Key,
    MajorKey,
    Diatonic,
):
    pass
