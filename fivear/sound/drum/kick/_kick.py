"""

    *Kick*

  The kick sound.

"""
from dataclasses import dataclass
from typing import TypeVar

__all__ = ["Kick"]


@dataclass
class Kick(
    Sound,
):
    Transient = TypeVar("Transient")
    Roll = TypeVar("Roll")
    Body = TypeVar("Body")
