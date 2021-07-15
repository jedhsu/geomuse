"""

    Transient

  Models the transient of the kick.

"""

from dataclasses import dataclass

from ear4.base import Wave

from .base import Kick

__all__ = ["Transient"]


# @dataclass
# class _Transient:
#     base: Noise


class _Build_:
    pass


class Transient(Build, Kick, Wave):
    ...


class _Dark_:
    pass
