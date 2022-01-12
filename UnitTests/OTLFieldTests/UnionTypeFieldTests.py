import unittest

from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLichtmastMasthoogte import KlLichtmastMasthoogte
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.UnionTypeField import UnionTypeField


class DtuLichtmastMasthoogte(UnionTypeField):
    """Union datatype om een standaard of afwijkende masthoogte te bepalen."""

    def __init__(self):
        super().__init__(
            naam='DtuLichtmastMasthoogte',
            label='Masthoogte',
            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte',
            definition='Union datatype om een standaard of afwijkende masthoogte te bepalen.',
            usagenote="",
            deprecated_version="")

        field_afwijkendeHoogte = KwantWrdInMeter()
        """De afwijkende hoogte van de mast in meter."""
        field_afwijkendeHoogte.naam = "afwijkendeHoogte"
        field_afwijkendeHoogte.label = "afwijkende hoogte"
        field_afwijkendeHoogte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte.afwijkendeHoogte"
        field_afwijkendeHoogte.definition = "De afwijkende hoogte van de mast in meter."
        field_afwijkendeHoogte.constraints = ""
        field_afwijkendeHoogte.usagenote = ""
        field_afwijkendeHoogte.deprecated_version = ""

        field_standaardHoogte = KeuzelijstField(naam="standaardHoogte",
                                                label="standaard hoogte",
                                                lijst=KlLichtmastMasthoogte(),
                                                objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte.standaardHoogte",
                                                definition="Bepaling van de standaard hoogte van een mast.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        """Bepaling van de standaard hoogte van een mast."""

        self.fieldsTuple = (field_afwijkendeHoogte, field_standaardHoogte)


class UnionTestClass(AIMObject):
    def __init__(self):
        super().__init__()

        self.unionveld = DtuLichtmastMasthoogte()
        self.unionveld.naam = "testUnion"
        self.unionveld.label = "testUnion"
        self.unionveld.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#testUnion"
        self.unionveld.definition = "testUnion definitie"
        self.unionveld.constraints = ""
        self.unionveld.usagenote = ""
        self.unionveld.deprecated_version = ""
        self.unionveld.readonly = 0


class UnionTypeFieldTests(unittest.TestCase):
    def test_InitClassWithField(self):
        c = UnionTestClass()
        self.assertIsNotNone(c)

    def test_GebruikVeldInvalidFieldName(self):
        c = UnionTestClass()
        with self.assertRaises(ValueError):
            c.unionveld.gebruik_veld('badFieldName')

    def test_GebruikVeld1(self):
        c = UnionTestClass()
        c.unionveld.gebruik_veld('afwijkendeHoogte')
        self.assertEqual(c.unionveld.actiefVeld, c.unionveld.fieldsTuple[0])

    def test_AssignBeforGebruikVeld(self):
        c = UnionTestClass()
        with self.assertRaises(RuntimeError):
            c.unionveld.waarde = KwantWrdInMeter(7.5)

    def test_AssignField1BadValue(self):
        c = UnionTestClass()
        c.unionveld.gebruik_veld('afwijkendeHoogte')

        with self.assertRaises(ValueError):
            c.unionveld.waarde = "2"

    def test_AssignField1(self):
        c = UnionTestClass()
        c.unionveld.gebruik_veld('afwijkendeHoogte')
        c.unionveld.waarde = KwantWrdInMeter(7.5)
        w = c.unionveld.waarde
        self.assertEqual(7.5, c.unionveld.waarde)

    def test_AssignField2(self):
        c = UnionTestClass()
        c.unionveld.gebruik_veld('standaardHoogte')
        c.unionveld.actiefVeld.set_value_by_invulwaarde('10.00')
        self.assertEqual("10.00", c.unionveld.waarde.invulwaarde)

    def test_AssignField2BadValue(self):
        c = UnionTestClass()
        c.unionveld.gebruik_veld('standaardHoogte')
        with self.assertRaises(ValueError):
            c.unionveld.actiefVeld.set_value_by_invulwaarde("2")
