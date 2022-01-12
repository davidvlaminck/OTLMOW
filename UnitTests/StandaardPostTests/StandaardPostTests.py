import dataclasses
from unittest import TestCase

from OTLModel.ClassLoader import ClassLoader
from OTLModel.Classes.BitumineuzeLaag import BitumineuzeLaag
from OTLModel.Classes.Geotextiel import Geotextiel
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.UnionTypeField import UnionTypeField


@dataclasses.dataclass
class StandaardPostMapping:
    typeURI: str
    attribuutURI: str
    dotnotatie: str
    defaultWaarde: str
    range: str
    usagenote: str
    isMeetstaatAttr: int
    isAltijdInTeVullen: int
    isBasisMapping: int
    mappingStatus: str
    mappingOpmerking: str


def set_value_by_dotnotatie(assetOrAttribuut, dotnotatie, defaultWaarde):
    if not '.' in dotnotatie:
        attribuut = getattr(assetOrAttribuut, dotnotatie)
        if isinstance(attribuut, KeuzelijstField):
            attribuut.set_value_by_invulwaarde(defaultWaarde)
        else:
            attribuut.waarde = defaultWaarde
        return

    attributen = dotnotatie.split('.')

    if isinstance(assetOrAttribuut, UnionTypeField):
        assetOrAttribuut.gebruik_veld(attributen[0])
        attribuut = assetOrAttribuut.actiefVeld
    else:
        attribuut = getattr(assetOrAttribuut, attributen[0])
    set_value_by_dotnotatie(attribuut, dotnotatie.split(".", 1)[1], defaultWaarde)

@dataclasses.dataclass
class StandaardPost:
    nummer: str
    beschrijving: str
    meetstaateenheid: str
    mappings: list

    def get_assets_from_post(self):
        class_loader = ClassLoader()
        lijst = []
        for mapping in self.mappings:
            asset = next((c for c in lijst if c.typeURI == mapping.typeURI), None)
            if asset is None:
                asset = class_loader.dynamic_create_instance_from_uri(mapping.typeURI)
                lijst.append(asset)
            if mapping.defaultWaarde != '':
                set_value_by_dotnotatie(asset, mapping.dotnotatie, mapping.defaultWaarde)
        return lijst


class StandaardPostCollection:
    def __init__(self):
        mappings0501 = [StandaardPostMapping(typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geotextiel',
                                             attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geotextiel.type',
                                             dotnotatie='type',
                                             defaultWaarde='bescherming',
                                             range='',
                                             usagenote='',
                                             isMeetstaatAttr=0,
                                             isAltijdInTeVullen=0,
                                             isBasisMapping=1,
                                             mappingStatus='gemapt 2.0',
                                             mappingOpmerking='')]
        standaardposten = [StandaardPost(nummer='0501.00000',
                                         beschrijving='Beschermen van de onderfundering of fundering volgens 5-1, met geotextiel',
                                         meetstaateenheid='M2',
                                         mappings=mappings0501)]

        mappings060215019 = [
            StandaardPostMapping(typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag',
                                 attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcProfileerlaag.laagtype',
                                 dotnotatie='laagtype.profileerlaag.laagtype',
                                 defaultWaarde='profileerlaag',
                                 range='',
                                 usagenote='',
                                 isMeetstaatAttr=0,
                                 isAltijdInTeVullen=0,
                                 isBasisMapping=1,
                                 mappingStatus='gemapt 2.0',
                                 mappingOpmerking=''),
            StandaardPostMapping(typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag',
                                 attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag.laagRol',
                                 dotnotatie='laagRol',
                                 defaultWaarde='verharding',
                                 range='',
                                 usagenote='',
                                 isMeetstaatAttr=0,
                                 isAltijdInTeVullen=0,
                                 isBasisMapping=1,
                                 mappingStatus='gemapt 2.0',
                                 mappingOpmerking=''),
            StandaardPostMapping(typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag',
                                 attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LaagBouwklasse.bouwklasse',
                                 dotnotatie='bouwklasse',
                                 defaultWaarde='',
                                 range='B1|B2|B3',
                                 usagenote='',
                                 isMeetstaatAttr=0,
                                 isAltijdInTeVullen=1,
                                 isBasisMapping=1,
                                 mappingStatus='gemapt 2.0',
                                 mappingOpmerking=''),
            StandaardPostMapping(typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag',
                                 attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag.mengseltype',
                                 dotnotatie='mengseltype',
                                 defaultWaarde='AVS-B',
                                 range='',
                                 usagenote='',
                                 isMeetstaatAttr=0,
                                 isAltijdInTeVullen=0,
                                 isBasisMapping=1,
                                 mappingStatus='gemapt 2.0',
                                 mappingOpmerking=''),
            StandaardPostMapping(typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag',
                                 attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LaagDikte.dikte',
                                 dotnotatie='dikte',
                                 defaultWaarde='',
                                 range='8 <= x <= 10',
                                 usagenote='cm^^cdt:ucumunit',
                                 isMeetstaatAttr=0,
                                 isAltijdInTeVullen=1,
                                 isBasisMapping=1,
                                 mappingStatus='gemapt 2.0',
                                 mappingOpmerking=''),
            StandaardPostMapping(typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag',
                                 attribuutURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcProfileerlaag.gewicht',
                                 dotnotatie='laagtype.profileerlaag.gewicht',
                                 defaultWaarde='',
                                 range='',
                                 usagenote='t^^cdt:ucumunit',
                                 isMeetstaatAttr=1,
                                 isAltijdInTeVullen=1,
                                 isBasisMapping=1,
                                 mappingStatus='gemapt 2.0',
                                 mappingOpmerking='')]

        standaardposten.append(StandaardPost(nummer='0602.15019',
                                             beschrijving='Profileerlaag, bouwklassegroep B1-B3 volgens 6-2, type AVS-B, dikte E = 8 à 10 cm',
                                             meetstaateenheid='TON',
                                             mappings=mappings060215019))

        self.lijst = standaardposten

    def get_by_nummer(self, nummer: str) -> StandaardPost:
        return next(post for post in self.lijst if post.nummer == nummer)


class StandaardPostTests(TestCase):
    def test_create_assets_by_standaardPost_0501(self):
        posten = StandaardPostCollection()
        post0501 = posten.get_by_nummer('0501.00000')
        assets = post0501.get_assets_from_post()

        self.assertEqual(1, len(assets))
        self.assertTrue(isinstance(assets[0], Geotextiel))
        self.assertEqual('bescherming', assets[0].type.waarde.invulwaarde)

    def test_create_assets_by_standaardPost_0602_15019(self):
        posten = StandaardPostCollection()
        post0602 = posten.get_by_nummer('0602.15019')
        assets = post0602.get_assets_from_post()

        self.assertEqual(1, len(assets))
        self.assertTrue(isinstance(assets[0], BitumineuzeLaag))
        self.assertEqual('AVS-B', assets[0].mengseltype.waarde.invulwaarde)
        self.assertEqual('verharding', assets[0].laagRol.waarde.invulwaarde)
        self.assertEqual('profileerlaag', assets[0].laagtype.waarde.laagtype.waarde.invulwaarde)
