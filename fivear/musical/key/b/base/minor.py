"""

    *B Minor*

  The key of B major.

"""

from ..._mode import MinorKey
from ....scale import Diatonic

from ._key import B_Key

__all__ = ["B_Minor"]


class B_Minor(
    B_Key,
    MinorKey,
    Diatonic,
):
    pass
