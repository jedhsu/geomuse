"""

    *C Minor*

  The key of C major.

"""

from ..._mode import MinorKey
from ....scale import Diatonic

from ._key import C_Key

__all__ = ["C_Minor"]


class C_Minor(
    C_Key,
    MinorKey,
    Diatonic,
):
    pass
