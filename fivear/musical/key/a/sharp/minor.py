"""

    *A♯ Minor*

  The key of A♯ minor.

"""

from ..._mode import MinorKey
from ....scale import Diatonic

from ._key import AsKey

__all__ = ["AsMinor"]


class AsMinor(
    AsKey,
    MinorKey,
    Diatonic,
):
    pass
