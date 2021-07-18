class TestPower:
    def test_init(self):
        pow = Power(-10)

        assert isinstance(pow, Power)
        assert isinstance(pow, float)
