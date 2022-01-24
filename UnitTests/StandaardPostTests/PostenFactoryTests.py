from unittest import TestCase

from OTLModel.Classes.BeschermingWapening import BeschermingWapening
from OTLModel.Classes.Verankeringslandhoofd import Verankeringslandhoofd
from PostenMapping.Model.Post050200100 import Post050200100
from PostenMapping.Model.Post050200300 import Post050200300
from PostenMapping.Model.Post060190001 import Post060190001
from PostenMapping.StandaardPostFactory import StandaardPostFactory


class StandaardPostFactoryTests(TestCase):
    def test_find_posten_from_asset_by_typeURI_Verankeringslandhoofd(self):
        v = Verankeringslandhoofd()
        resultaat = StandaardPostFactory.find_posten_from_asset_by_typeURI(v)
        self.assertEqual(1, len(resultaat))
        self.assertEqual(Post060190001().nummer, resultaat[0].nummer)

    def test_find_posten_from_asset_by_typeURI_BeschermingWapening(self):
        b = BeschermingWapening()
        resultaat = StandaardPostFactory.find_posten_from_asset_by_typeURI(b)
        self.assertEqual(2, len(resultaat))
        self.assertEqual(Post050200100().nummer, resultaat[0].nummer)
        self.assertEqual(Post050200300().nummer, resultaat[1].nummer)

    def test_find_posten_from_asset_BeschermingWapening(self):
        b = BeschermingWapening()
        b.type = 'geogrids'
        resultaat = StandaardPostFactory.find_posten_from_asset(b)
        self.assertEqual(1, len(resultaat))
        self.assertEqual(Post050200300().nummer, resultaat[0].nummer)
