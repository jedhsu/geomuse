"""

    *mus . key . a*

"""

from .base import BaseAKey
from .base import BaseAMajor
from .base import BaseAMinor

from .sharp import SharpAKey
from .sharp import SharpAMajor
from .sharp import SharpAMinor

from .flat import FlatAKey
from .flat import FlatAMajor
from .flat import FlatAMinor

__all__ = [
    "BaseAKey",
    "BaseAMajor",
    "BaseAMinor",
    "SharpAKey",
    "SharpAMajor",
    "SharpAMinor",
    "FlatAKey",
    "FlatAMajor",
    "FlatAMinor",
]
