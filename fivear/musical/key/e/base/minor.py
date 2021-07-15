"""

    *E Minor*

  The key of E major.

"""

from ..._mode import MinorKey
from ....scale import Diatonic

from ._key import E_Key

__all__ = ["E_Minor"]


class E_Minor(
    E_Key,
    MinorKey,
    Diatonic,
):
    pass
