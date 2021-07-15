"""

    *A♭ Minor*

  The key of A♭ minor.

"""

from ..._mode import MinorKey
from ....scale import Diatonic

from ._key import AfKey

__all__ = ["AfMinor"]


class AfMinor(
    AfKey,
    MinorKey,
    Diatonic,
):
    pass
