"""

    *Interval*

  A difference of pitch between two sounds.

"""

from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from fractions import Fraction

from ._ratio import FrequencyRatio

__all__ = ["Interval"]


class Interval(
    FrequencyRatio,
):
    pass


# class _IntervalEnum(
#     Enum,
# ):
#     O = 0
#     m2 = 1
#     M2 = 2
#     m3 = 3
#     M3 = 4
#     P4 = 5
#     m5 = 6
#     P5 = 7
#     m6 = 8
#     M6 = 9
#     m7 = 10
#     M7 = 11


# @dataclass
# class _Interval:
#     # TODO: switch to semitone repr
#     interval: _IntervalEnum
#     octaves: int


# class _Interval_(
#     _Interval,
# ):
#     def semitones(self) -> int:
#         """ Number of semitones. """
#         return 12 * self.octaves + self.interval.value

#     # TODO: make perfect
#     def ratio(self) -> float:
#         """
#         Ratio of the interval's frequency??

#         """
#         return 2 ** Fraction(self.semitones(), 12)

#     def purity(self) -> int:
#         ...


# class Interval(NamedTuple):
#     bot: Frequency
#     top: Frequency

#     @property
#     def consonance(self):
#         raise NotImplementedError

#     @staticmethod
#     def just_intonation():
#         raise NotImplementedError


# class Interval(
#     _Display_,
#     _Interval_,
#     _Interval,
# ):
#     def __init__(
#         self,
#         interval: _IntervalEnum,
#         octaves: int,
#     ):
#         super().__init__(interval, octaves)

#     @staticmethod
#     def from_semitones(semitones: int):
#         octaves, step = divmod(semitones, 12)
#         return Interval(_IntervalEnum(step), octaves)

#     def __add__(self, i: Interval) -> Interval:
#         return add(self, i)


# def add(i1: Interval, i2: Interval) -> Interval:
#     semitones = i1.semitones() + i2.semitones()
#     return Interval.from_semitones(semitones)


# m2 = Interval.from_semitones(1)
# M2 = Interval.from_semitones(2)
# m3 = Interval.from_semitones(3)
# M3 = Interval.from_semitones(4)
# P4 = Interval.from_semitones(5)
# m5 = Interval.from_semitones(6)
# P5 = Interval.from_semitones(7)
