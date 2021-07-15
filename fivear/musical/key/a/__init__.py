"""

    *mus . key . a*

"""

from .base import A_Key
from .base import A_Major
from .base import A_Minor

from .sharp import AsKey
from .sharp import AsMajor
from .sharp import AsMinor

from .flat import AfKey
from .flat import AfMajor
from .flat import AfMinor

__all__ = [
    "A_Key",
    "A_Major",
    "A_Minor",
    "AsKey",
    "AsMajor",
    "AsMinor",
    "AfKey",
    "AfMajor",
    "AfMinor",
]
