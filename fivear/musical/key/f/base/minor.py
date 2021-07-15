"""

    *F Minor*

  The key of F minor.

"""

from ..._mode import MinorKey
from ....scale import Diatonic

from ._key import F_Key

__all__ = ["F_Minor"]


class F_Minor(
    F_Key,
    MinorKey,
    Diatonic,
):
    pass
