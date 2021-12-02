import unittest

from OTLClasses.Verification.DtcAdres import DtcAdres


class DtcAdresTests(unittest.TestCase):
    def test_DtcAdresInit(self):
        adres = DtcAdres()

        adres.bus = "A"
        self.assertTrue(adres.bus == "A")

        adres.gemeente.set_value_by_label("de Haan")
        self.assertTrue(adres.gemeente.value.waarde == "de-Haan")

        adres.huisnummer = "1"
        self.assertTrue(adres.huisnummer == "1")
        with self.assertRaises(ValueError):
            adres.huisnummer = 1

        adres.postcode = "2880"
        self.assertTrue(adres.postcode == "2880")
        with self.assertRaises(ValueError):
            adres.postcode = 2880
