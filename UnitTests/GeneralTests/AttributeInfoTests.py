from unittest import TestCase

from OTLMOW.OTLModel.BaseClasses.OTLObject import OTLObjectHelper
from OTLMOW.OTLModel.Classes.Aftakking import Aftakking
from OTLMOW.OTLModel.Classes.Exoten import Exoten
from OTLMOW.OTLModel.Classes.Verkeersregelaar import Verkeersregelaar
from OTLMOW.OTLModel.Datatypes.DtcExterneReferentie import DtcExterneReferentie


class AttributeInfoTests(TestCase):
    def test_info_empty_class(self):
        infoString = Aftakking().info()
        expected = '^information about Aftakking \d{10,12}:\n$'
        self.assertRegex(infoString, expected)

    def test_info_empty_class2(self):
        infoString = Verkeersregelaar().info()
        expected = '^information about Verkeersregelaar \d{10,12}:\n$'
        self.assertRegex(infoString, expected)

    def test_attr_info_empty_class(self):
        infoString = Verkeersregelaar().info_attr()
        expected = '^Attribute information about Verkeersregelaar \d{10,12}:\n'
        expected2 = 'assetId \(type: DtcIdentificator\)\n'
        self.assertRegex(infoString, expected)
        self.assertRegex(infoString, expected2)

    def test_make_string_version_empty_class(self):
        v = Verkeersregelaar()
        string_version = OTLObjectHelper().build_string_version(v, indent=4)
        expected = ''
        self.assertEqual(string_version, expected)

    def test_make_string_version_StringField(self):
        v = Verkeersregelaar()
        v.naam = 'VR'
        string_version = OTLObjectHelper().build_string_version(v, indent=4)
        expected = '    naam : VR'
        self.assertEqual(string_version, expected)

    def test_make_string_version_DtcIdentificator(self):
        v = Verkeersregelaar()
        v.assetId.identificator = 'eigen_id'
        v.assetId.toegekendDoor = 'AWV'
        string_version = OTLObjectHelper().build_string_version(v, indent=4)
        expected = '    assetId :\n        identificator : eigen_id\n        toegekendDoor : AWV'
        self.assertEqual(string_version, expected)

    def test_create_dict_from_asset_DtcIdentificator(self):
        v = Verkeersregelaar()
        v.assetId.identificator = 'eigen_id'
        v.assetId.toegekendDoor = 'AWV'
        d = v.create_dict_from_asset()
        expected = {'assetId': {
            'identificator': 'eigen_id',
            'toegekendDoor': 'AWV'}}
        self.assertDictEqual(expected, d)

    def test_create_dict_from_asset_deprecated(self):
        e = Exoten()
        e.toestand = 'in-gebruik'
        d = e.create_dict_from_asset()
        expected = {'toestand': 'in-gebruik'}
        self.assertDictEqual(expected, d)

    def test_create_dict_from_asset_string(self):
        v = Verkeersregelaar()
        v.naam = 'VR'
        d = v.create_dict_from_asset()
        expected = {'naam': 'VR'}
        self.assertDictEqual(expected, d)

    def test_create_dict_from_asset_kwantWrd(self):
        v = Verkeersregelaar()
        v.theoretischeLevensduur.waarde = 120
        d = v.create_dict_from_asset()
        expected = {'theoretischeLevensduur': 120}
        self.assertDictEqual(expected, d)

    def test_create_dict_from_asset_keuzelijst(self):
        v = Verkeersregelaar()
        v.toestand = 'in-gebruik'
        d = v.create_dict_from_asset()
        expected = {'toestand': 'in-gebruik'}
        self.assertDictEqual(expected, d)

    def test_create_dict_from_asset_keuzelijst_kardinaliteit(self):
        v = Verkeersregelaar()
        v.coordinatiewijze = ["centraal", "pulsen"]
        d = v.create_dict_from_asset()
        expected = {'coordinatiewijze': ["centraal", "pulsen"]}
        self.assertDictEqual(expected, d)

    def test_create_dict_from_asset_complex_kardinaliteit(self):
        v = Verkeersregelaar()
        v.externeReferentie = []

        v.externeReferentie.append(DtcExterneReferentie.waardeObject())
        v.externeReferentie[0].externReferentienummer = "externe referentie 2"
        v.externeReferentie[0].externePartij = "bij externe partij 2"

        v.externeReferentie.append(DtcExterneReferentie.waardeObject())
        v.externeReferentie[1].externReferentienummer = "externe referentie 1"
        v.externeReferentie[1].externePartij = "bij externe partij 1"
        d = v.create_dict_from_asset()
        expected = {'externeReferentie': [
            {'externReferentienummer': 'externe referentie 2',
             'externePartij': 'bij externe partij 2'
             }, {'externReferentienummer': 'externe referentie 1',
                 'externePartij': 'bij externe partij 1'
                 }]
        }
        self.assertDictEqual(expected, d)
