"""

    *Decibel - Convert - From*

"""

__all__ = ["From"]


class From:
    @staticmethod
    def from_amplitude(ampl: Amplitude):
        return _Decibel(20 * log(ampl, 10))

    @staticmethod
    def from_power(power: Power):
        return _Decibel(10 * log(power, 10))

    # def from_phon(self, f: Frequency):
    #     pass
