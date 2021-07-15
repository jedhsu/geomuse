"""

    *G♯ Minor*

  The key of G♯ minor.

"""

from ..._mode import MinorKey
from ....scale import Diatonic

from ._key import GsKey

__all__ = ["GsMinor"]


class GsMinor(
    GsKey,
    MinorKey,
    Diatonic,
):
    pass
