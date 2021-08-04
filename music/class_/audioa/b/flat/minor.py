"""

    *B♭ Minor*

  The key of B♭ minor.

"""

from ..._mode import MinorKey
from ....scale import Diatonic

from ._key import BfKey

__all__ = ["BfMinor"]


class BfMinor(
    BfKey,
    MinorKey,
    Diatonic,
):
    pass
