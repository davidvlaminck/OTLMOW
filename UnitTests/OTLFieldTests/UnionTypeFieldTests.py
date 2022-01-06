import unittest

from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLichtmastMasthoogte import KlLichtmastMasthoogte
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.UnionTypeField import UnionTypeField
from OTLModel.Classes.Aftakking import Aftakking
from OTLModel.Datatypes.KlAlgGemeente import KlAlgGemeente


class UnionTestClass(Aftakking):
    def __init__(self):
        super().__init__()

        field1 = KwantWrdInMeter()
        """De afwijkende hoogte van de mast in meter."""
        field1.naam = "afwijkendeHoogte"
        field1.label = "afwijkende hoogte"
        field1.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte.afwijkendeHoogte"
        field1.definition = "De afwijkende hoogte van de mast in meter."
        field1.constraints = ""
        field1.usagenote = ""
        field1.deprecated_version = ""

        field2 = KeuzelijstField(naam="standaardHoogte",
                                 label="standaard hoogte",
                                 lijst=KlLichtmastMasthoogte(),
                                 uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte.standaardHoogte",
                                 definition="Bepaling van de standaard hoogte van een mast.",
                                 constraints="",
                                 usagenote="",
                                 deprecated_version="")

        self.unionveld = UnionTypeField(naam="testUnion",
                                        label="testUnion",
                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#testUnion",
                                        definition="testUnion definitie",
                                        usagenote="",
                                        deprecated_version="",
                                        fieldsTuple=(field1, field2))


class KeuzelijstFieldTests(unittest.TestCase):
    def test_InitClassWithField(self):
        c = UnionTestClass()
        self.assertIsNotNone(c)

    def test_UseFieldInvalidFieldName(self):
        c = UnionTestClass()
        with self.assertRaises(ValueError):
            c.unionveld.use_field('badFieldName')

    def test_UseField1(self):
        c = UnionTestClass()
        c.unionveld.use_field('afwijkendeHoogte')
        self.assertEqual(c.unionveld.actiefVeld, c.unionveld.fieldsTuple[0])

    def test_AssignBeforeUseField(self):
        c = UnionTestClass()
        with self.assertRaises(RuntimeError):
            c.unionveld.waarde = KwantWrdInMeter(7.5)

    def test_AssignField1BadValue(self):
        c = UnionTestClass()
        c.unionveld.use_field('afwijkendeHoogte')

        with self.assertRaises(ValueError):
            c.unionveld.waarde = "2"

    def test_AssignField1(self):
        c = UnionTestClass()
        c.unionveld.use_field('afwijkendeHoogte')
        c.unionveld.waarde = KwantWrdInMeter(7.5)
        w = c.unionveld.waarde
        self.assertEqual(7.5, c.unionveld.waarde)

    def test_AssignField2(self):
        c = UnionTestClass()
        c.unionveld.use_field('standaardHoogte')
        c.unionveld.actiefVeld.set_value_by_invulwaarde('10.00')
        self.assertEqual("10.00", c.unionveld.waarde.invulwaarde)

    def test_AssignField2BadValue(self):
        c = UnionTestClass()
        c.unionveld.use_field('standaardHoogte')
        with self.assertRaises(ValueError):
            c.unionveld.actiefVeld.set_value_by_invulwaarde("2")



