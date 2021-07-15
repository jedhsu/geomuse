"""

    Key

  Model for key.

"""

from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import Callable, GenericAlias


__all__ = ["Key"]

# -- Key
#
#    Think about it as a pitch eq class.
#
# --


def format_accidental(accidental: str) -> str:
    if accidental == "s":
        return "\u266f"
    elif accidental == "f":
        return "\u266d"
    else:
        raise KeyError("Not an accidental.")


@dataclass
class _Key:
    _key: _KeyEnum


# this stuff can go fuck itself
class _Ops_(_Key):
    def __add__(self, n: int) -> _Key:
        return _Key((self._key.value + n) % 12)

    def __sub__(self, n: int) -> _Key:
        # TODO: can make interval() invoke the references... like a monad??
        return _Key((self._key.value - n) % 12)


class _Display_(_Key):
    def __repr__(self):
        keyname = self._key.name
        keyname = keyname.replace("s", format_accidental("s"))
        keyname = keyname.replace("s", format_accidental("s"))
        return keyname


# TODO: meh... metaclass is another way to do this... think about which better (vs. 2 layer indirection)
# class PitchMeta:
#     def __prepare__(meta, *args, **kwargs):
#         ...

#         return

#         return


class Key(
    _Display_,
    _Ops_,
    _Key,
):
    def __init__(self, enum: _KeyEnum):
        super().__init__(enum)

    @staticmethod
    def from_name(name: str):
        return Key(_KeyEnum(name))

    @classmethod
    def __class_getitem__(cls):
        return GenericAlias

    __getitem__: Callable


# think about cclass method dynamic


def _get_index(key: Key, name: str):
    return Key.from_name(name)


Key.__getitem__ = _get_index
