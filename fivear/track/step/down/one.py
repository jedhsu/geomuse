# [TODO] hmm interesting design

from dataclasses import dataclass

from ..bar import Bar


@dataclass
class One(
    Bar,
    Beat,
    Step,
):
    pass
