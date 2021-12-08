import unittest

from OTLClasses.Verification.DtcAdres import DtcAdres


class DtcAdresTests(unittest.TestCase):
    def test_DtcAdresInit(self):
        adres = DtcAdres()

        adres.bus.waarde = "A"
        self.assertTrue(adres.bus.waarde == "A")

        adres.gemeente.set_value_by_label("de Haan")
        self.assertTrue(adres.gemeente.value.waarde == "de-Haan")

        adres.huisnummer.waarde = "1"
        self.assertTrue(adres.huisnummer.waarde == "1")
        with self.assertRaises(ValueError):
            adres.huisnummer.waarde = 1

        adres.postcode.waarde = "2880"
        self.assertTrue(adres.postcode.waarde == "2880")
        with self.assertRaises(ValueError):
            adres.postcode.waarde = 2880
