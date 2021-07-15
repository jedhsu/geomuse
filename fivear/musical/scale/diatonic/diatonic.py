"""

    *Diatonic*

  A type scaled with 12 elements.

"""

from .._scale import Scale

__all__ = ["Diatonic"]


class Diatonic(
    Scale,
):
    def __get_item__(self):
        pass
