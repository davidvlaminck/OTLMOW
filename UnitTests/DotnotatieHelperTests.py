from unittest import TestCase

from Facility.DotnotatieHelper import DotnotatieHelper
from OTLModel.BaseClasses.CouldNotConvertToCorrectType import CouldNotConvertToCorrectType
from OTLModel.Classes.BestratingVanKassei import BestratingVanKassei


class DotnotatieHelperTests(TestCase):
    def test_set_attribute_by_dotnotatie_decimal_value(self):
        b = BestratingVanKassei()

        with self.subTest("correctly typed and convert=True"):
            DotnotatieHelper.set_attribute_by_dotnotatie(b, 'afmetingVanBestratingselementBxl.breedte', 9.0, convert=True)
            self.assertEqual(9.0, b.afmetingVanBestratingselementBxl.breedte.waarde)

        with self.subTest("correctly typed and convert=False"):
            DotnotatieHelper.set_attribute_by_dotnotatie(b, 'afmetingVanBestratingselementBxl.breedte', 8.0, convert=False)
            self.assertEqual(8.0, b.afmetingVanBestratingselementBxl.breedte.waarde)

        with self.subTest("incorrectly typed and convert=True"):
            DotnotatieHelper.set_attribute_by_dotnotatie(b, 'afmetingVanBestratingselementBxl.breedte', "7.0", convert=True)
            self.assertEqual(7.0, b.afmetingVanBestratingselementBxl.breedte.waarde)

        with self.subTest("incorrectly typed and convert=False (converted by set_waarde method on attribute itself)"):
            DotnotatieHelper.set_attribute_by_dotnotatie(b, 'afmetingVanBestratingselementBxl.breedte', "6.0", convert=False)
            self.assertEqual(6.0, b.afmetingVanBestratingselementBxl.breedte.waarde)
