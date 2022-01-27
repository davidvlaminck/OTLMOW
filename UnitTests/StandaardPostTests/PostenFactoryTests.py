from unittest import TestCase

from src.OTLMOW.OTLModel.Classes.BeschermingWapening import BeschermingWapening
from src.OTLMOW.OTLModel.Classes.BitumineuzeLaag import BitumineuzeLaag
from src.OTLMOW.OTLModel.Classes.Geotextiel import Geotextiel
from src.OTLMOW.OTLModel.Classes.Verankeringslandhoofd import Verankeringslandhoofd
from src.OTLMOW.OTLModel.Classes.Walsbetonverharding import Walsbetonverharding
from src.OTLMOW.PostenMapping.Model.Post050100000 import Post050100000
from src.OTLMOW.PostenMapping.Model.Post050200100 import Post050200100
from src.OTLMOW.PostenMapping.Model.Post050200300 import Post050200300
from src.OTLMOW.PostenMapping.Model.Post060190001 import Post060190001
from src.OTLMOW.PostenMapping.Model.Post060215019 import Post060215019
from src.OTLMOW.PostenMapping.Model.Post060423020 import Post060423020
from src.OTLMOW.PostenMapping.StandaardPostFactory import StandaardPostFactory


class StandaardPostFactoryTests(TestCase):
    def test_create_assets_by_standaardPost_0501(self):
        post0501 = Post050100000()
        assets = StandaardPostFactory.create_assets_from_post(post0501)

        self.assertEqual(1, len(assets))
        self.assertTrue(isinstance(assets[0], Geotextiel))
        self.assertEqual('bescherming', assets[0].type)

    def test_create_assets_by_standaardPost_0602_15019(self):
        post0602 = Post060215019()
        assets = StandaardPostFactory.create_assets_from_post(post0602)

        self.assertEqual(1, len(assets))
        self.assertTrue(isinstance(assets[0], BitumineuzeLaag))
        self.assertEqual('AVS-B', assets[0].mengseltype)
        self.assertEqual('verharding', assets[0].laagRol)
        self.assertEqual('profileerlaag', assets[0].laagtype.profileerlaag.laagtype)

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

    def test_find_posten_from_asset_Walsbetonverharding(self):
        w = Walsbetonverharding()
        w.dikte.waarde = 20
        resultaat = StandaardPostFactory.find_posten_from_asset(w)
        self.assertEqual(1, len(resultaat))
        self.assertEqual(Post060423020().nummer, resultaat[0].nummer)

