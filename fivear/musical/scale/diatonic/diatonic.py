"""

    *Diatonic*

  A type scaled with 12 elements.

"""

from .._scale import Scale

__all__ = ["Diatonic"]


class Diatonic(
    Scale,
):
    notes = 12

    def ratio(self):
        """
        2 root 12
        """

    def __get_item__(self):
        pass
