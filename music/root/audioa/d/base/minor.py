"""

    *D Minor*

  The key of D major.

"""

from ..._mode import MinorKey
from ....scale import Diatonic

from ._key import D_Key

__all__ = ["D_Minor"]


class D_Minor(
    D_Key,
    MinorKey,
    Diatonic,
):
    pass
