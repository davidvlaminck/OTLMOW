import unittest
from unittest import TestCase

from Facility.AssetFactory import AssetFactory


@unittest.skip("feature request")
class AssetFactorySearchUriFromNameTests(TestCase):
    def test_AssetFactory_search_uri_from_class_name(self):
        factory = AssetFactory()
        resultLijst = factory.search_uri_from_class_name('stroom')
        expectedLijst = {
            'Stroomdalgrasland': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomdalgrasland',
            'Stroomkring': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring',
            'StroomMeetmodule': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StroomMeetmodule'
        }

        self.assertDictEqual(expectedLijst, resultLijst)

        # use regex
        # wildcard before and after
        # remove spaces
        # lower()
        # create OTLModel/ClassLijst when create_model()
