"""

    *mus . key . f*

"""

from .base import F_Key
from .base import F_Major
from .base import F_Minor

from .sharp import FsKey
from .sharp import FsMajor
from .sharp import FsMinor

from .flat import FfKey
from .flat import FfMajor
from .flat import FfMinor

__all__ = [
    "F_Key",
    "F_Major",
    "F_Minor",
    "FsKey",
    "FsMajor",
    "FsMinor",
    "FfKey",
    "FfMajor",
    "FfMinor",
]
