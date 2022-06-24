from unittest import TestCase, mock

from OTLMOW.Facility.DotnotationHelper import DotnotationHelper
from OTLMOW.OTLModel.Classes.Onderdeel.BitumineuzeLaag import BitumineuzeLaag
from OTLMOW.PostenMapping.PostenCollector import PostenCollector
from OTLMOW.PostenMapping.PostenCreator import PostenCreator
from OTLMOW.PostenMapping.StandaardPost import StandaardPost
from OTLMOW.PostenMapping.StandaardPostMapping import StandaardPostMapping


class StandaardPostCollection:
    def __init__(self):
        mappings0501 = [StandaardPostMapping(typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geotextiel',
                                             attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geotextiel.type',
                                             dotnotation='type',
                                             defaultWaarde='bescherming',
                                             range='',
                                             usagenote='',
                                             isMeetstaatAttr=0,
                                             isAltijdInTeVullen=0,
                                             isBasisMapping=1,
                                             mappingStatus='gemapt 2.0',
                                             mappingOpmerking='',
                                             standaardpostnummer='0501.00000')
            , StandaardPostMapping(
                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geotextiel',
                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag.oppervlakte',
                dotnotation='oppervlakte',
                defaultWaarde='',
                range='',
                usagenote='m2^^cdt:ucumunit',
                isMeetstaatAttr=1,
                isAltijdInTeVullen=1,
                isBasisMapping=1,
                mappingStatus='gemapt 2.0',
                mappingOpmerking='',
                standaardpostnummer='0501.00000')]
        standaardposten = [StandaardPost(nummer='0501.00000',
                                         beschrijving='Beschermen van de onderfundering of fundering volgens 5-1, met geotextiel',
                                         meetstaateenheid='M2',
                                         mappings=mappings0501)]

        mappings060215019 = [
            StandaardPostMapping(typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag',
                                 attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcProfileerlaag.laagtype',
                                 dotnotation='laagtype.profileerlaag.laagtype',
                                 defaultWaarde='profileerlaag',
                                 range='',
                                 usagenote='',
                                 isMeetstaatAttr=0,
                                 isAltijdInTeVullen=0,
                                 isBasisMapping=1,
                                 mappingStatus='gemapt 2.0',
                                 mappingOpmerking='',
                                 standaardpostnummer='0602.15019'),
            StandaardPostMapping(typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag',
                                 attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag.laagRol',
                                 dotnotation='laagRol',
                                 defaultWaarde='verharding',
                                 range='',
                                 usagenote='',
                                 isMeetstaatAttr=0,
                                 isAltijdInTeVullen=0,
                                 isBasisMapping=1,
                                 mappingStatus='gemapt 2.0',
                                 mappingOpmerking='',
                                 standaardpostnummer='0602.15019'),
            StandaardPostMapping(typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag',
                                 attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LaagBouwklasse.bouwklasse',
                                 dotnotation='bouwklasse',
                                 defaultWaarde='',
                                 range='B1|B2|B3',
                                 usagenote='',
                                 isMeetstaatAttr=0,
                                 isAltijdInTeVullen=1,
                                 isBasisMapping=1,
                                 mappingStatus='gemapt 2.0',
                                 mappingOpmerking='',
                                 standaardpostnummer='0602.15019'),
            StandaardPostMapping(typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag',
                                 attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag.mengseltype',
                                 dotnotation='mengseltype',
                                 defaultWaarde='AVS-B',
                                 range='',
                                 usagenote='',
                                 isMeetstaatAttr=0,
                                 isAltijdInTeVullen=0,
                                 isBasisMapping=1,
                                 mappingStatus='gemapt 2.0',
                                 mappingOpmerking='',
                                 standaardpostnummer='0602.15019'),
            StandaardPostMapping(typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag',
                                 attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LaagDikte.dikte',
                                 dotnotation='dikte',
                                 defaultWaarde='',
                                 range='8 <= x <= 10',
                                 usagenote='cm^^cdt:ucumunit',
                                 isMeetstaatAttr=0,
                                 isAltijdInTeVullen=1,
                                 isBasisMapping=1,
                                 mappingStatus='gemapt 2.0',
                                 mappingOpmerking='',
                                 standaardpostnummer='0602.15019'),
            StandaardPostMapping(typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag',
                                 attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcProfileerlaag.gewicht',
                                 dotnotation='laagtype.profileerlaag.gewicht',
                                 defaultWaarde='',
                                 range='',
                                 usagenote='t^^cdt:ucumunit',
                                 isMeetstaatAttr=1,
                                 isAltijdInTeVullen=1,
                                 isBasisMapping=1,
                                 mappingStatus='gemapt 2.0',
                                 mappingOpmerking='',
                                 standaardpostnummer='0602.15019')]

        standaardposten.append(StandaardPost(nummer='0602.15019',
                                             beschrijving='Profileerlaag, bouwklassegroep B1-B3 volgens 6-2, type AVS-B, dikte E = 8 à 10 cm',
                                             meetstaateenheid='TON',
                                             mappings=mappings060215019))

        self.lijst = standaardposten

    def get_by_nummer(self, nummer: str) -> StandaardPost:
        return next(post for post in self.lijst if post.nummer == nummer)


class StandaardPostTests(TestCase):
    def test_set_value_by_dotnotation_simple(self):
        b = BitumineuzeLaag()
        b.notitie = 'a'
        self.assertEqual('a', b.notitie)
        DotnotationHelper.set_attribute_by_dotnotation(b, 'notitie', 'c')
        self.assertEqual('c', b.notitie)

    def test_set_value_by_dotnotation_invalid_attribute(self):
        b = BitumineuzeLaag()
        b.notitie = 'a'
        self.assertEqual('a', b.notitie)
        with self.assertRaises(AttributeError) as dotnotationerror:
            DotnotationHelper.set_attribute_by_dotnotation(b, 'notitie_invalid', 'c')

    def test_set_value_by_dotnotation_complex(self):
        b = BitumineuzeLaag()
        b.assetId.identificator = 'a'
        self.assertEqual('a', b.assetId.identificator)
        DotnotationHelper.set_attribute_by_dotnotation(b, 'assetId.identificator', 'c')
        self.assertEqual('c', b.assetId.identificator)

    def test_create_datablock_standaardPost_0501(self):
        posten = StandaardPostCollection()
        post0501 = posten.get_by_nummer('0501.00000')
        creator = PostenCreator(postenCollector=PostenCollector(mock))

        datablock = creator.create_datablock_from_post(post0501)
        expected = ['# coding=utf-8',
                    "from OTLMOW.PostenMapping.StandaardPost import StandaardPost",
                    "from OTLMOW.PostenMapping.StandaardPostMapping import StandaardPostMapping",
                    "",
                    "",
                    '# Generated with PostenCreator. To modify: extend, do not edit',
                    "class Post050100000(StandaardPost):",
                    "    def __init__(self):",
                    "        super().__init__(",
                    "            nummer='0501.00000',",
                    "            beschrijving='Beschermen van de onderfundering of fundering volgens 5-1, met geotextiel',",
                    "            meetstaateenheid='M2',",
                    "            mappings=[StandaardPostMapping(",
                    "                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geotextiel',",
                    "                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geotextiel.type',",
                    "                dotnotation='type',",
                    "                defaultWaarde='bescherming',",
                    "                range='',",
                    "                usagenote='',",
                    "                isMeetstaatAttr=0,",
                    "                isAltijdInTeVullen=0,",
                    "                isBasisMapping=1,",
                    "                mappingStatus='gemapt 2.0',",
                    "                mappingOpmerking='',",
                    "                standaardpostnummer='0501.00000')",
                    '                , StandaardPostMapping(',
                    "                typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geotextiel',",
                    "                attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag.oppervlakte',",
                    "                dotnotation='oppervlakte',",
                    "                defaultWaarde='',",
                    "                range='',",
                    "                usagenote='m2^^cdt:ucumunit',",
                    '                isMeetstaatAttr=1,',
                    '                isAltijdInTeVullen=1,',
                    '                isBasisMapping=1,',
                    "                mappingStatus='gemapt 2.0',",
                    "                mappingOpmerking='',",
                    "                standaardpostnummer='0501.00000')])"]
        self.assertEqual(expected, datablock)
