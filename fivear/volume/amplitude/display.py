from ._amplitude import Amplitude


class Display(
    Amplitude,
):
    unit = None  # [TODO] confirm this is no units
    symbol = "A"  # [TODO] sympy interface

    def __repr__(self) -> str:
        number = f"{self:.3f}"
        return f"{number} {self.unit}" if self.unit else number
