"""

Duration base type.

"""

__all__ = ["Duration"]

# [TODO] since subclassing float is immutable, can no longer set - push this up one level?
# class _Set_:
#     def _set_seconds(self, val: float):
#         self.seconds = val


class _Duration(float):
    def __init__(self, seconds: float):
        super(_Duration, self).__new__(float, seconds)

    # class _Mutate_(_Duration):
    def update_seconds(self, val: float):
        self._set_seconds(val)


class _Unit_:
    unit = "seconds"


class _Display_(_Unit_, _Duration):
    def __repr__(self) -> str:
        return f"{self:.3f} {self.unit}"


class Duration(
    _Display_,
    _Duration,
):
    pass
