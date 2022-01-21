from unittest import TestCase

from OTLModel.Classes.Aftakking import Aftakking
from OTLModel.Classes.Verkeersregelaar import Verkeersregelaar


class AttributeInfoTests(TestCase):
    def test_info_empty_class(self):
        infoString = Aftakking().info()
        expected = '^information about Aftakking \d{12}:\n$'
        self.assertRegex(infoString, expected)

    def test_info_empty_class2(self):
        infoString = Verkeersregelaar().info()
        expected = '^information about Verkeersregelaar \d{12}:\n$'
        self.assertRegex(infoString, expected)

    def test_make_string_version_empty_class(self):
        v = Verkeersregelaar()
        string_version = v.build_string_version(indent=4)
        expected = ''
        print(string_version)
        self.assertEqual(string_version, expected)

    def test_make_string_version_StringField(self):
        v = Verkeersregelaar()
        v.naam = 'VR'
        string_version = v.build_string_version(indent=4)
        expected = '    naam : VR'
        print(string_version)
        self.assertEqual(string_version, expected)

    def test_make_string_version_DtcIdentificator(self):
        v = Verkeersregelaar()
        v.assetId.identificator = 'eigen_id'
        v.assetId.toegekendDoor = 'AWV'
        string_version = v.build_string_version(indent=4)
        expected = '    assetId :\n        identificator : eigen_id        \ntoegekendDoor : AWV\n'
        print(string_version)
        self.assertEqual(string_version, expected)
