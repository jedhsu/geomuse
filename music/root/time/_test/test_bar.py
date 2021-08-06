from ..bar import *
from ..beat import Beat


class Test_Bar:
    def test_getitem(self):
        bar = Bar(1)

        assert isinstance(bar[1], Beat)
        assert bar[1].index == 1


class TestDisplay:
    def __repr__(self) -> str:
        bar = Bar(1)

        return repr(bar) == "Bar 1"


class TestBar:
    def test_init(self):
        ...

    def test_bar(self):
        ...
