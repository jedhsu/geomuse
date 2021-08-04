from ._decibel import Decibel


class Display(
    Decibel,
):
    unit = "db"

    def __repr__(self) -> str:
        number = f"{self:.2f}"
        return f"{number} {self.unit}" if self.unit is not None else number
