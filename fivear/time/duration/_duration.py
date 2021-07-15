"""

    *Duration*

"""


class _Duration(
    float,
):
    def __init__(
        self,
        seconds: float,
    ):
        super(_Duration, self).__new__(
            float,
            seconds,
        )

    # class _Mutate_(_Duration):
    def update_seconds(self, val: float):
        self._set_seconds(val)
