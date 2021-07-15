"""

    *E♭ Minor*

  The key of E♭ minor.

"""

from ..._mode import MinorKey
from ....scale import Diatonic

from ._key import EfKey

__all__ = ["EfMinor"]


class EfMinor(
    EfKey,
    MinorKey,
    Diatonic,
):
    pass
