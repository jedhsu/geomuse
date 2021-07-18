"""

    *Transform*

"""

from typing import Callable

__all__ = ["Transform"]


class Transform(
    Callable[[Time], Measure],
):
    pass
