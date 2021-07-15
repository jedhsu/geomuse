"""

    *D♭ Minor*

  The key of D♭ minor.

"""

from ..._mode import MinorKey
from ....scale import Diatonic

from ._key import DfKey

__all__ = ["DfMinor"]


class DfMinor(
    DfKey,
    MinorKey,
    Diatonic,
):
    pass
