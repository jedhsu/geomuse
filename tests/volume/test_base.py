# from import Ampl, Amplitude, Decibel, Phon, Power


# class TestAmpl:
#     def test_type_hierarchy(self):
#         assert issubclass(Amplitude, Ampl)
#         assert issubclass(Decibel, Ampl)
#         assert issubclass(Power, Ampl)
#         assert issubclass(Phon, Ampl)

#     def test_decibel(self):
#         db = Decibel(-10)

#         assert isinstance(db, Decibel)
#         assert isinstance(db, float)

#     def test_phon(self):
#         phon = Phon(3)

#         assert isinstance(phon, Phon)
#         assert isinstance(phon, float)

#     def test_hooks(self):
#         assert Ampl.Amplitude == Amplitude
#         assert Ampl.Decibel == Decibel
#         assert Ampl.Power == Power
#         assert Ampl.Phon == Phon

#         assert issubclass(Ampl.Amplitude, Ampl)
#         assert issubclass(Ampl.Decibel, Ampl)
#         assert issubclass(Ampl.Power, Ampl)
#         assert issubclass(Ampl.Phon, Ampl)
