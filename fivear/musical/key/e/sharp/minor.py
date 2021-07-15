"""

    *E♯ Minor*

  The key of E♯ minor.

"""

from ..._mode import MinorKey
from ....scale import Diatonic

from ._key import EsKey

__all__ = ["EsMinor"]


class EsMinor(
    EsKey,
    MinorKey,
    Diatonic,
):
    pass
