import unittest

from OTLModel.Datatypes.DtcIdentificator import DtcIdentificator
from OTLModel.Datatypes.DtcRechtspersoon import DtcRechtspersoon
from Facility.Exceptions.UnionTypeError import UnionTypeError
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Datatypes.DtcVegetatieSoortnaam import DtcVegetatieSoortnaam
from OTLModel.Datatypes.DtuLichtmastMasthoogte import DtuLichtmastMasthoogte
from OTLModel.Datatypes.KlAIMToestand import KlAIMToestand
from OTLModel.Datatypes.KlRioleringsbuisMateriaal import KlRioleringsbuisMateriaal
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.StringField import StringField


class TestInstance2(AttributeInfo):
    def __init__(self):
        super().__init__()

        self._notitie = OTLAttribuut(field=StringField,
                                     naam="notitie",
                                     label="notitie",
                                     objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.notitie",
                                     definition="Extra notitie voor het object.")

        self._assetId = OTLAttribuut(field=DtcIdentificator,
                                     naam="DtcIdentificator",
                                     label="Identificator",
                                     objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator",
                                     definition="Complex datatype voor de identificator van een AIM object volgens de bron van de identificator.")

        self._toestand = OTLAttribuut(field=KlAIMToestand,
                                      naam="toestand",
                                      label="toestand",
                                      objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMToestand.toestand",
                                      definition="Geeft de actuele stand in de levenscyclus van het object.",
                                      deprecated_version="")

        self._kleur = OTLAttribuut(field=StringField,
                                   naam="kleur",
                                   label="kleur",
                                   objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis.kleur",
                                   definition="De kleur van de coating.",
                                   kardinaliteit_min='1',
                                   kardinaliteit_max='*')

        self._materiaal = OTLAttribuut(naam="materiaal",
                                       label="materiaal",
                                       field=KlRioleringsbuisMateriaal,
                                       objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Mantelbuis.materiaal",
                                       definition="Bepaalt het materiaal van de mantelbuis.",
                                       kardinaliteit_min='1',
                                       kardinaliteit_max='*')

        self._soort = OTLAttribuut(naam="soort",
                                   label="soort",
                                   field=DtcVegetatieSoortnaam,
                                   objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen.soort",
                                   definition="Met deze eigenschap worden de Nederlandse soortnaam, wetenschappelijke soortnaam en de soortcode van de meest voorkomende soorten binnen het begroeid oppervlak weergegeven.",
                                   kardinaliteit_min='1',
                                   kardinaliteit_max='*')

        self._masthoogte = OTLAttribuut(field=DtuLichtmastMasthoogte,
                                        naam="masthoogte",
                                        label="masthoogte",
                                        objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.masthoogte",
                                        definition="Hoogte (in meter) van de lichtmast.")

        self._hoogte = OTLAttribuut(field=KwantWrdInMeter,
                                  naam="Hoogte",
                                  label="hoogte",
                                  objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#.Hoogte",
                                  definition="De hoogte in meter.")

        self._persoon = OTLAttribuut(field=DtcRechtspersoon,
                                   naam='persoon',
                                   label='persoon',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcRechtspersoon',
                                   definition='persoon.')

    @property
    def persoon(self):
        """De hoogte in meter."""
        return self._persoon.waarde

    @persoon.setter
    def persoon(self, value):
        self._persoon.set_waarde(value, owner=self)

    @property
    def hoogte(self):
        """De hoogte in meter."""
        return self._hoogte.waarde

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self)

    @property
    def masthoogte(self):
        """Hoogte (in meter) van de lichtmast."""
        return self._masthoogte.waarde

    @masthoogte.setter
    def masthoogte(self, value):
        self._masthoogte.set_waarde(value, owner=self)

    @property
    def soort(self):
        """Met deze eigenschap worden de Nederlandse soortnaam, wetenschappelijke soortnaam en de soortcode van de meest voorkomende soorten binnen het begroeid oppervlak weergegeven."""
        return self._soort.waarde

    @soort.setter
    def soort(self, value):
        self._soort.set_waarde(value, owner=self)

    @property
    def materiaal(self):
        """Bepaalt het materiaal van de mantelbuis."""
        return self._materiaal.waarde

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def kleur(self):
        """De kleur van de coating."""
        return self._kleur.waarde

    @kleur.setter
    def kleur(self, value):
        self._kleur.set_waarde(value, owner=self)

    @property
    def toestand(self):
        """Geeft de actuele stand in de levenscyclus van het object."""
        return self._toestand.waarde

    @toestand.setter
    def toestand(self, value):
        self._toestand.set_waarde(value, owner=self)

    @property
    def assetId(self):
        """Complex datatype voor de identificator van een AIM object volgens de bron van de identificator."""
        return self._assetId.waarde

    @assetId.setter
    def assetId(self, value):
        self._assetId.set_waarde(value)

    @property
    def notitie(self):
        """Extra notitie voor het object."""
        return self._notitie.waarde

    @notitie.setter
    def notitie(self, value):
        self._notitie.set_waarde(value)


class RefactoringTests(unittest.TestCase):
    @unittest.skip("not implemented yet")
    def test_AttrInfoOfClass(self):
        instance = TestInstance2()
        result = instance.attr_info()  # displays info about itself
        self.assertTrue(False)

    def test_StringField(self):
        instance = TestInstance2()
        instance.notitie = "a"
        self.assertEqual("a", instance.notitie)
        with self.assertRaises(TypeError):
            instance.notitie = 2
        self.assertEqual("""information about notitie:
naam: notitie
uri: https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.notitie
definition: Extra notitie voor het object.
label: notitie
usagenote: 
constraints: 
readonly: False
kardinaliteit_min: 1
kardinaliteit_max: 1
deprecated_version: """,
                         instance.attr_info("notitie"))
        self.assertEqual(
            """information about String:
naam: String
uri: http://www.w3.org/2001/XMLSchema#string
definition: Beschrijft een tekstregel volgens http://www.w3.org/2001/XMLSchema#string.
label: String
usagenote: https://www.w3.org/TR/xmlschema-2/#string
deprecated_version: """,
            instance.attr_type_info("notitie"))
        instance2 = TestInstance2()
        self.assertEqual(None, instance2.notitie)
        instance2.notitie = "b"
        self.assertEqual("a", instance.notitie)
        self.assertEqual("b", instance2.notitie)
        instance.notitie = None
        self.assertEqual(None, instance.notitie)
        instance.notitie = "b"
        self.assertEqual("b", instance.notitie)

    def test_ComplexField(self):
        instance = TestInstance2()
        instance2 = TestInstance2()
        instance.assetId.identificator = 'id'
        instance.assetId.toegekendDoor = 'AWV'
        instance2.assetId.identificator = 'id2'
        instance2.assetId.toegekendDoor = 'extern'
        self.assertEqual("id", instance.assetId.identificator)
        self.assertEqual("AWV", instance.assetId.toegekendDoor)
        self.assertEqual("id2", instance2.assetId.identificator)
        self.assertEqual("extern", instance2.assetId.toegekendDoor)
        expectedIdentificatorInfo = """information about identificator:
naam: identificator
uri: https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator
definition: Een groep van tekens om een AIM object te identificeren of te benoemen.
label: identificator
usagenote: 
constraints: 
readonly: False
kardinaliteit_min: 1
kardinaliteit_max: 1
deprecated_version: """
        self.assertEqual(expectedIdentificatorInfo,
            instance.assetId.attr_info('identificator'))
        self.assertEqual(
            expectedIdentificatorInfo,
            instance.attr_info('assetId.identificator'))
        self.assertEqual(
            """information about String:
naam: String
uri: http://www.w3.org/2001/XMLSchema#string
definition: Beschrijft een tekstregel volgens http://www.w3.org/2001/XMLSchema#string.
label: String
usagenote: https://www.w3.org/TR/xmlschema-2/#string
deprecated_version: """,
            instance.attr_type_info('assetId.identificator'))
        with self.assertRaises(TypeError):
            instance.assetId.toegekendDoor = 2
        with self.assertRaises(ValueError):
            instance.assetId = 2

    def test_KeuzelijstField(self):
        instance = TestInstance2()
        instance2 = TestInstance2()
        instance.toestand = 'in-gebruik'
        self.assertEqual('in-gebruik', instance.toestand)
        with self.assertRaises(ValueError):
            instance.toestand = 'in gebruik'
        with self.assertRaises(TypeError):
            instance.toestand = 2
        instance2.toestand = 'in-opbouw'
        self.assertEqual('in-gebruik', instance.toestand)
        self.assertEqual('in-opbouw', instance2.toestand)
        self.assertEqual("""information about toestand:
naam: toestand
uri: https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMToestand.toestand
definition: Geeft de actuele stand in de levenscyclus van het object.
label: toestand
usagenote: 
constraints: 
readonly: False
kardinaliteit_min: 1
kardinaliteit_max: 1
deprecated_version: """,
                         instance.attr_info("toestand"))
        self.assertEqual(
            """information about KlAIMToestand:
naam: KlAIMToestand
uri: https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAIMToestand
definition: Keuzelijst met fasen uit de levenscyclus van een object om de toestand op een moment mee vast te leggen.
label: AIM toestand
usagenote: 
deprecated_version: 
possible values:
    geannuleerd
    gepland
    in-gebruik
    in-ontwerp
    in-opbouw
    overgedragen
    uit-gebruik
    verwijderd""",
            instance.attr_type_info("toestand"))

    def test_StringFieldMetKardinaliteit(self):
        instance = TestInstance2()
        instance2 = TestInstance2()
        self.assertEqual(None, instance.kleur)
        with self.assertRaises(ValueError):
            instance.kleur = []
        instance.kleur = ['geel']
        self.assertEqual(['geel'], instance.kleur)
        instance.kleur = ['geel', 'rood']
        self.assertEqual(['geel', 'rood'], instance.kleur)
        with self.assertRaises(TypeError):
            instance.kleur = ("geel")
        with self.assertRaises(ValueError):
            instance.kleur = ["geel", 2]

    def test_KeuzelijstFieldMetKardinaliteit(self):
        instance = TestInstance2()
        instance2 = TestInstance2()
        self.assertEqual(None, instance.materiaal)
        with self.assertRaises(ValueError):
            instance.materiaal = []
        instance.materiaal = ['PP-buizen']
        self.assertEqual(['PP-buizen'], instance.materiaal)
        instance.materiaal = ['PP-buizen', 'PVC-buizen']
        self.assertEqual(['PP-buizen', 'PVC-buizen'], instance.materiaal)
        with self.assertRaises(TypeError):
            instance.materiaal = tuple("PP-buizen")
        with self.assertRaises(ValueError):
            instance.materiaal = ["PP-buizen", 2]

    @unittest.skip("not implemented yet")
    def test_ComplexFieldMetKardinaliteit(self):
        self.assertFalse(True)

    def test_ComplexFieldInComplexField(self):
        instance = TestInstance2()
        instance2 = TestInstance2()
        with self.assertRaises(ValueError):
            instance.persoon = []
        instance.persoon.adres.straatnaam = 'straat'
        instance.persoon.organisatie = 'organisatie'
        instance.persoon.adres.postcode = '2900'
        instance.persoon.adres.gemeente = 'schoten'

        self.assertEqual('straat', instance.persoon.adres.straatnaam)
        self.assertEqual('organisatie', instance.persoon.organisatie)
        self.assertEqual('2900', instance.persoon.adres.postcode)
        self.assertEqual('schoten', instance.persoon.adres.gemeente)


    @unittest.skip("not implemented yet")
    def test_BooleanField(self):
        self.assertFalse(True)

    def test_UnionTypeField(self):
        instance = TestInstance2()
        instance2 = TestInstance2()
        self.assertEqual(None, instance.masthoogte)
        with self.assertRaises(UnionTypeError):
            instance.masthoogte = '10'
        instance.masthoogte = "10.00"
        self.assertEqual("10.00", instance.masthoogte)
        instance.masthoogte = 11.00
        self.assertEqual(11.00, instance.masthoogte)


    def test_KwantWaardeField(self):
        instance = TestInstance2()
        instance2 = TestInstance2()
        self.assertEqual(None, instance.hoogte)
        with self.assertRaises(TypeError):
            instance.hoogte = '10.00'
        instance.hoogte = 10.00
        self.assertEqual(10.00, instance.hoogte)
        instance.hoogte = 10
        self.assertEqual(10, instance.hoogte)
        with self.assertRaises(TypeError):
            instance.hoogte = True
        self.assertEqual("""information about KwantWrdInMeter:
naam: KwantWrdInMeter
uri: https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMeter
definition: Een kwantitatieve waarde die een getal in meter uitdrukt.
label: Kwantitatieve waarde in meter
usagenote: https://www.w3.org/TR/xmlschema-2/#decimal
deprecated_version: 

information about standaardEenheid:
    naam: standaardEenheid
    uri: https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMeter.standaardEenheid
    definition: De standaard eenheid bij dit datatype is uitgedrukt in meter.
    label: standaard eenheid
    usagenote: "m"^^cdt:ucumunit
    constraints: "m"^^cdt:ucumunit
    deprecated_version: """, instance.attr_type_info('hoogte'))


    # use setattr and getattr on class/attribuut
    # .attr_info('name attribute') returns info about attribute
    # .attr_type_info('name attribute') returns info about type of attribute
    # attributeType = field of the attribuut and contains validate() to validate input
