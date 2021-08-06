"""

    *Amplitude - Display*

"""

from ._amplitude import Amplitude

__all__ = ["Display"]


class Display(
    Amplitude,
):
    unit = None  # [TODO] confirm this is no units

    def __repr__(self) -> str:
        number = f"{self:.3f}"
        return f"{number} {self.unit}" if self.unit else number
