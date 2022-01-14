import unittest

from UnitTests.OTLFieldTests.AttributeInfo import AttributeInfo
from UnitTests.OTLFieldTests.DtcIdentificator import DtcIdentificator
from UnitTests.OTLFieldTests.KlAIMToestand import KlAIMToestand
from UnitTests.OTLFieldTests.OTLAttribuut import OTLAttribuut
from UnitTests.OTLFieldTests.StringField import StringField


class TestInstance2(AttributeInfo):
    def __init__(self):
        super().__init__()

        self._notitie = OTLAttribuut(field=StringField(),
                                     naam="notitie", label="notitie",
                                     objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.notitie",
                                     definition="Extra notitie voor het object.", constraints="", usagenote="",
                                     deprecated_version="")

        self._assetId = OTLAttribuut(field=DtcIdentificator(),
                                     naam="DtcIdentificator",
                                     label="Identificator",
                                     objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator",
                                     definition="Complex datatype voor de identificator van een AIM object volgens de bron van de identificator.",
                                     usagenote="",
                                     deprecated_version="")

        self._toestand = OTLAttribuut(field=KlAIMToestand(),
                                      naam="toestand",
                                      label="toestand",
                                      objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMToestand.toestand",
                                      definition="Geeft de actuele stand in de levenscyclus van het object.",
                                      constraints="",
                                      usagenote="",
                                      deprecated_version="")

        self._kleur = OTLAttribuut(field=StringField(),
                                   naam="kleur",
                                   label="kleur",
                                   objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis.kleur",
                                   definition="De kleur van de coating.",
                                   constraints="",
                                   usagenote="",
                                   deprecated_version="",
                                   kardinaliteit_min='1',
                                   kardinaliteit_max='*')

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
    def test_requirements(self):
        instance = TestInstance2()
        instance.notitie = "a"
        print(instance.notitie)
        self.assertEqual("a", instance.notitie)
        with self.assertRaises(TypeError):
            instance.notitie = 2
        self.assertEqual("naam: notitie; definitie: Extra notitie voor het object.",
                         instance.attr_info("notitie"))  # evt  instance.attr_info(instance.notitie) ?
        self.assertEqual(
            "naam: StringField; definitie: Beschrijft een tekstregel volgens http://www.w3.org/2001/XMLSchema#string.",
            instance.attr_type_info("notitie"))
        instance2 = TestInstance2()
        self.assertEqual(None, instance2.notitie)
        instance2.notitie = "b"
        self.assertEqual("a", instance.notitie)
        self.assertEqual("b", instance2.notitie)

        instance.assetId.identificator = 'id'
        instance.assetId.toegekendDoor = 'AWV'
        instance2.assetId.identificator = 'id2'
        instance2.assetId.toegekendDoor = 'extern'
        self.assertEqual("id", instance.assetId.identificator)
        self.assertEqual("AWV", instance.assetId.toegekendDoor)
        self.assertEqual("id2", instance2.assetId.identificator)
        self.assertEqual("extern", instance2.assetId.toegekendDoor)
        self.assertEqual(
            'naam: identificator; definitie: Een groep van tekens om een AIM object te identificeren of te benoemen.',
            instance.assetId.attr_info('identificator'))
        self.assertEqual(
            'naam: identificator; definitie: Een groep van tekens om een AIM object te identificeren of te benoemen.',
            instance.attr_info('assetId.identificator'))
        with self.assertRaises(TypeError):
            instance.assetId.toegekendDoor = 2
        with self.assertRaises(TypeError):
            instance.assetId = 2

        instance.toestand = 'in-gebruik'
        self.assertEqual('in-gebruik', instance.toestand)
        with self.assertRaises(ValueError):
            instance.toestand = 'in gebruik'
        with self.assertRaises(TypeError):
            instance.toestand = 2
        instance2.toestand = 'in-opbouw'
        self.assertEqual('in-gebruik', instance.toestand)
        self.assertEqual('in-opbouw', instance2.toestand)
        self.assertEqual("naam: toestand; definitie: Geeft de actuele stand in de levenscyclus van het object.",
                         instance.attr_info("toestand"))
        self.assertEqual(
            "naam: KlAIMToestand; definitie: Keuzelijst met fasen uit de levenscyclus van een object om de toestand op een moment mee vast te leggen. mogelijke waardes:\n"
            "geannuleerd\ngepland\nin-gebruik\nin-ontwerp\nin-opbouw\novergedragen\nuit-gebruik\nverwijderd",
            instance.attr_type_info("toestand"))

        self.assertEqual(None, instance.kleur)
        with self.assertRaises(ValueError):
            instance.kleur = []
        instance.kleur = ['geel']
        self.assertEqual(['geel'], instance.kleur)
        instance.kleur = ['geel', 'rood']
        self.assertEqual(['geel', 'rood'], instance.kleur)
        with self.assertRaises(TypeError):
            instance.kleur = ("geel")
        with self.assertRaises(TypeError):
            instance.kleur = ["geel", 2]

    # use setattr and getattr on class/attribuut
    # .attr_info('name attribute') returns info about attribute
    # .attr_type_info('name attribute') returns info about type of attribute
    # attributeType = field of the attribuut and contains validate() to validate input
