"""

    *G Minor*

  The key of G minor.

"""

from ..._mode import MinorKey
from ....scale import Diatonic

from ._key import G_Key

__all__ = ["G_Minor"]


class G_Minor(
    G_Key,
    MinorKey,
    Diatonic,
):
    pass
