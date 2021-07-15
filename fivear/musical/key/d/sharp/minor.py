"""

    *D♯ Minor*

  The key of D♯ minor.

"""

from ..._mode import MinorKey
from ....scale import Diatonic

from ._key import DsKey

__all__ = ["DsMinor"]


class DsMinor(
    DsKey,
    MinorKey,
    Diatonic,
):
    pass
