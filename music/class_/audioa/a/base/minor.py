"""

    *A Minor*

  The key of A major.

"""

from ..._mode import MinorKey
from ....scale import Diatonic

from ._key import A_Key

__all__ = ["A_Minor"]


class A_Minor(
    A_Key,
    MinorKey,
    Diatonic,
):
    pass
