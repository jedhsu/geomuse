"""

    *C♯ Minor*

  The key of C♯ minor.

"""

from ..._mode import MinorKey
from ....scale import Diatonic

from ._key import CsKey

__all__ = ["CsMinor"]


class CsMinor(
    CsKey,
    MinorKey,
    Diatonic,
):
    pass
