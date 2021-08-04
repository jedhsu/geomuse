"""

    *Audio Class*

  An equivalence class of audio.

  Commonly known as pitch class.

"""

from abc import ABCMeta

from .._class import Class

__all__ = ["AudioClass"]


class AudioClass(
    Class,
):
    __metaclass__ = ABCMeta
