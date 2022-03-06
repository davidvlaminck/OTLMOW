from unittest import TestCase

from OTLMOW.Facility.Exceptions.HasNoDotNotatieException import HasNoDotNotatieException
from OTLMOW.OTLModel.Classes.Lichtmast import Lichtmast
from OTLMOW.OTLModel.Classes.Verkeersregelaar import Verkeersregelaar


class DotnotatieOnAttributeTests(TestCase):
    def test_create_dotnotatie_on_attribute_level(self):
        vr = Verkeersregelaar()

        with self.subTest('complex attribute'):
            self.assertEqual('assetId.identificator', vr.assetId._identificator.dotnotatie)
            with self.assertRaises(HasNoDotNotatieException):
                self.assertEqual('assetId', vr._assetId.dotnotatie)

        with self.subTest('non-complex attributes'):
            self.assertEqual('naam', vr._naam.dotnotatie)
            self.assertEqual('merk', vr._merk.dotnotatie)

        with self.subTest('kwant waarde attribute'):
            self.assertEqual('theoretischeLevensduur.waarde', vr.theoretischeLevensduur._waarde.dotnotatie)  # TODO incorrect test

        with self.subTest('complex attribute with kard'):
            self.assertEqual('externeReferentie[].externReferentienummer',
                             vr.externeReferentie._externReferentienummer.dotnotatie)

        with self.subTest('non-complex attribute with kard'):
            self.assertEqual('coordinatiewijze[]', vr._coordinatiewijze.dotnotatie)

        lichtmast = Lichtmast()
        with self.subTest('union attribuut'):
            self.assertEqual('masthoogte.afwijkendeHoogte.waarde', lichtmast.masthoogte.afwijkendeHoogte._waarde.dotnotatie)  # TODO incorrect test
            self.assertEqual('masthoogte.standaardHoogte', lichtmast.masthoogte._standaardHoogte.dotnotatie)
