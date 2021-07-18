"""

    *C♭ Minor*

  The key of C♭ minor.

"""

from ..._mode import MinorKey
from ....scale import Diatonic

from ._key import CfKey

__all__ = ["CfMinor"]


class CfMinor(
    CfKey,
    MinorKey,
    Diatonic,
):
    pass
