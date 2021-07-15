"""

    *mus . key . g*

"""

from .base import G_Key
from .base import G_Major
from .base import G_Minor

from .sharp import GsKey
from .sharp import GsMajor
from .sharp import GsMinor

from .flat import GfKey
from .flat import GfMajor
from .flat import GfMinor

__all__ = [
    "G_Key",
    "G_Major",
    "G_Minor",
    "GsKey",
    "GsMajor",
    "GsMinor",
    "GfKey",
    "GfMajor",
    "GfMinor",
]
