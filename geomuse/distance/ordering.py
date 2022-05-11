"""

    *[Ordering] Distance*

  Defines a total ordering on distance.

"""

from ._distance import Distance

__all__ = ["DistancelOrdering"]


class DistancelOrdering(
    Distance,
):
    def __lt__(
        self,
        it: Distance,
    ):
        return self.steps < it.steps

    def __le__(
        self,
        it: Distance,
    ):
        return self.steps <= it.steps

    def __gt__(
        self,
        it: Distance,
    ):
        return self.steps > it.steps

    def __ge__(
        self,
        it: Distancel,
    ):
        return self.steps >= it.steps
