"""

    *F♯ Minor*

  The key of F♯ minor.

"""

from ..._mode import MinorKey
from ....scale import Diatonic

from ._key import FsKey

__all__ = ["FsMinor"]


class FsMinor(
    FsKey,
    MinorKey,
    Diatonic,
):
    pass
