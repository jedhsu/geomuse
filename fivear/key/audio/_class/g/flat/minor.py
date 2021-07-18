"""

    *G♭ Minor*

  The key of G♭ minor.

"""

from ..._mode import MinorKey
from ....scale import Diatonic

from ._key import GfKey

__all__ = ["GfMinor"]


class GfMinor(
    GfKey,
    MinorKey,
    Diatonic,
):
    pass
