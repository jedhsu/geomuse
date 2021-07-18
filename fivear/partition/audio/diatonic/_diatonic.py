"""

    *Diatonic*

  A type scaled with 12 elements.

"""

from dataclasses import dataclass

from .._scale import Scale

__all__ = ["Diatonic"]


@dataclass
class Diatonic(
    Scale,
):
    def __init__(
        self,
    ):
        elements = 12
        super(Diatonic, self).__init__(
            elements,
        )

    def ratio(self):
        """
        2 root 12
        """

    def __get_item__(self):
        pass
