"""

    *mus . key . mode*

"""

from ._key import ModedKey

from .major import MajorKey
from .minor import MinorKey

__all__ = [
    "ModedKey",
    "MajorKey",
    "MinorKey",
]
