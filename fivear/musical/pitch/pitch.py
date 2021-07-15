"""

    *Pitch*

  Reference Model for pitch.

  # [TODO] clarify theory?

"""

from dataclasses import dataclass

from .key import Key

__all__ = ["Pitch"]


@dataclass
class _Pitch(
    AudioFrequency,
):
    key: Key
    level: int
    cents: int


class _Display_(
    _Pitch,
):
    def __repr__(self):
        return f"{self.key}{self.level}"


class Pitch(
    _Display_,
    _Pitch,
):
    ...
