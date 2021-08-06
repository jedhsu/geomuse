"""

    *B♯ Minor*

  The key of B♯ minor.

"""

from ..._mode import MinorKey
from ....scale import Diatonic

from ._key import BsKey

__all__ = ["BsMinor"]


class BsMinor(
    BsKey,
    MinorKey,
    Diatonic,
):
    pass
