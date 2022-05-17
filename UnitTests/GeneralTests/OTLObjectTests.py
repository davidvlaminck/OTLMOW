from unittest import TestCase

from OTLMOW.OTLModel.BaseClasses.OTLObject import OTLObjectHelper
from OTLMOW.OTLModel.Classes.Aftakking import Aftakking
from OTLMOW.OTLModel.Classes.Exoten import Exoten
from OTLMOW.OTLModel.Classes.Verkeersregelaar import Verkeersregelaar
from OTLMOW.OTLModel.Datatypes.DtcExterneReferentie import DtcExterneReferentie


class OTLObjectsTests(TestCase):
    def test_build_string_version_dotnotatie_empty_class(self):
        infoString = Aftakking().__str__(use_dotnotatie=True)
        expected = '^information about Aftakking \d{10,12}:\n$'
        self.assertRegex(infoString, expected)

    def test_build_string_version_dotnotatie_empty_class2(self):
        infoString = Verkeersregelaar().__str__(use_dotnotatie=True)
        expected = '^information about Verkeersregelaar \d{10,12}:\n$'
        self.assertRegex(infoString, expected)

    def test_make_string_version_dotnotatie_empty_class(self):
        v = Verkeersregelaar()
        string_version = OTLObjectHelper().build_string_version(v, indent=4)
        expected = ''
        self.assertEqual(string_version, expected)

    def test_make_string_version_dotnotatie_StringField(self):
        v = Verkeersregelaar()
        v.naam = 'VR'
        string_version = OTLObjectHelper().build_string_version(v, indent=4)
        expected = 'naam : VR'
        self.assertEqual(string_version, expected)

    def test_make_string_version_dotnotatie_DtcIdentificator(self):
        v = Verkeersregelaar()
        v._assetId.add_empty_value()
        v.assetId.identificator = 'eigen_id'
        v.assetId.toegekendDoor = 'AWV'
        string_version = OTLObjectHelper().build_string_version(v, indent=4)
        expected = 'assetId.identificator : eigen_id\nassetId.toegekendDoor : AWV'
        self.assertEqual(string_version, expected)

    def test_make_string_version_dotnotatie_complex_kardinaliteit(self):
        v = Verkeersregelaar()
        v._externeReferentie.add_empty_value()
        v.externeReferentie[0].externReferentienummer = "externe referentie 2"
        v.externeReferentie[0].externePartij = "bij externe partij 2"

        v._externeReferentie.add_empty_value()
        v.externeReferentie[1].externReferentienummer = "externe referentie 1"
        v.externeReferentie[1].externePartij = "bij externe partij 1"
        string_version = OTLObjectHelper().build_string_version(v, indent=4)
        expected = "externeReferentie[].externReferentienummer : ['externe referentie 2', 'externe referentie 1']\n"\
                   "externeReferentie[].externePartij : ['bij externe partij 2', 'bij externe partij 1']"
        self.assertEqual(string_version, expected)
