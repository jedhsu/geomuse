from ._interval import Interval

repr = {
    _IntervalEnum.m2: "minor 2nd",
    _IntervalEnum.M2: "Major 2nd",
    _IntervalEnum.m3: "minor 3rd",
    _IntervalEnum.M3: "Major 3rd",
    _IntervalEnum.P4: "Perfect 4th",
    _IntervalEnum.m5: "Tritone",
    _IntervalEnum.P5: "Perfect 5th",
    _IntervalEnum.m6: "minor 6th",
    _IntervalEnum.M6: "Major 6th",
    _IntervalEnum.m7: "minor 7th",
    _IntervalEnum.M7: "Major 7th",
}


class Display(
    Interval,
):
    def __repr__(self) -> str:
        interval = self.repr.get(self.interval)
        assert interval is not None
        return f"{interval}, {self.octaves} octaves"
