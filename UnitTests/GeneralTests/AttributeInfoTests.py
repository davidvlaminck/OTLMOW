﻿from unittest import TestCase

from OTLMOW.OTLModel.BaseClasses.OTLObject import OTLObjectHelper
from OTLMOW.OTLModel.Classes.Onderdeel.Aftakking import Aftakking
from OTLMOW.OTLModel.Classes.Onderdeel.Verkeersregelaar import Verkeersregelaar


class AttributeInfoTests(TestCase):
    def test_info_empty_class(self):
        infoString = Aftakking().info()
        expected = '^information about Aftakking \d{10,13}:\n$'
        self.assertRegex(infoString, expected)

    def test_info_empty_class2(self):
        infoString = Verkeersregelaar().info()
        expected = '^information about Verkeersregelaar \d{10,13}:\n$'
        self.assertRegex(infoString, expected)

    def test_make_string_version_empty_class(self):
        v = Verkeersregelaar()
        string_version = OTLObjectHelper().build_string_version(v, indent=4)
        expected = ''
        self.assertEqual(string_version, expected)

    def test_make_string_version_StringField(self):
        v = Verkeersregelaar()
        v.naam = 'VR'
        string_version = OTLObjectHelper().build_string_version(v, indent=4)
        expected = 'naam : VR'
        self.assertEqual(string_version, expected)

    def test_make_string_version_DtcIdentificator(self):
        v = Verkeersregelaar()
        v.assetId.identificator = 'eigen_id'
        v.assetId.toegekendDoor = 'AWV'
        string_version = OTLObjectHelper().build_string_version(v, indent=4)
        expected = 'assetId.identificator : eigen_id\nassetId.toegekendDoor : AWV'
        self.assertEqual(string_version, expected)

