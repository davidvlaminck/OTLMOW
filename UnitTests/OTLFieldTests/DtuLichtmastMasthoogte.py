# coding=utf-8
from UnitTests.OTLFieldTests.AttributeInfo import AttributeInfo
from UnitTests.OTLFieldTests.KlLichtmastMasthoogte import KlLichtmastMasthoogte
from UnitTests.OTLFieldTests.KwantWrdInMeter import KwantWrdInMeter
from UnitTests.OTLFieldTests.OTLAttribuut import OTLAttribuut
from UnitTests.OTLFieldTests.UnionTypeField import UnionTypeField


class DtuLichtmastMasthoogteAttributen(AttributeInfo):
    def __init__(self):
        self._afwijkendeHoogte = OTLAttribuut(field=KwantWrdInMeter,
                                              naam="afwijkendeHoogte",
                                              label="afwijkende hoogte",
                                              objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte.afwijkendeHoogte",
                                              definition="De afwijkende hoogte van de mast in meter.")

        self._standaardHoogte = OTLAttribuut(naam="standaardHoogte",
                                             label="standaard hoogte",
                                             field=KlLichtmastMasthoogte,
                                             objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte.standaardHoogte",
                                             definition="Bepaling van de standaard hoogte van een mast.")

    @property
    def afwijkendeHoogte(self):
        """De afwijkende hoogte van de mast in meter."""
        return self._afwijkendeHoogte.waarde

    @property
    def standaardHoogte(self):
        """Bepaling van de standaard hoogte van een mast."""
        return self._standaardHoogte.waarde


class DtuLichtmastMasthoogte(UnionTypeField, AttributeInfo):
    """Union datatype om een standaard of afwijkende masthoogte te bepalen."""
    naam = "DtuLichtmastMasthoogte",
    label = "Masthoogte",
    objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte",
    definition = "Union datatype om een standaard of afwijkende masthoogte te bepalen."
    waardeObject = DtuLichtmastMasthoogteAttributen
    #_uses_waarde_object = True


