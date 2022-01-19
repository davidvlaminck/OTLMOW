# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Datatypes.KlLichtmastMasthoogte import KlLichtmastMasthoogte
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.UnionTypeField import UnionTypeField
from OTLModel.Datatypes.UnionWaarden import UnionWaarden


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuLichtmastMasthoogteWaarden(AttributeInfo, UnionWaarden):
    def __init__(self):
        self._afwijkendeHoogte = OTLAttribuut(field=KwantWrdInMeter,
                                              naam='afwijkendeHoogte',
                                              label='afwijkende hoogte',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte.afwijkendeHoogte',
                                              kardinaliteit_min='0',
                                              definition='De afwijkende hoogte van de mast in meter.')

        self._standaardHoogte = OTLAttribuut(field=KlLichtmastMasthoogte,
                                             naam='standaardHoogte',
                                             label='standaard hoogte',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte.standaardHoogte',
                                             kardinaliteit_min='0',
                                             definition='Bepaling van de standaard hoogte van een mast.')

    @property
    def afwijkendeHoogte(self):
        """De afwijkende hoogte van de mast in meter."""
        return self._afwijkendeHoogte.waarde

    @afwijkendeHoogte.setter
    def afwijkendeHoogte(self, value):
        self._afwijkendeHoogte.set_waarde(value)
        if value is not None:
            self.clear_other_props('_afwijkendeHoogte')

    @property
    def standaardHoogte(self):
        """Bepaling van de standaard hoogte van een mast."""
        return self._standaardHoogte.waarde

    @standaardHoogte.setter
    def standaardHoogte(self, value):
        self._standaardHoogte.set_waarde(value)
        if value is not None:
            self.clear_other_props('_standaardHoogte')


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuLichtmastMasthoogte(UnionTypeField, AttributeInfo):
    """Union datatype om een standaard of afwijkende masthoogte te bepalen."""
    naam = 'DtuLichtmastMasthoogte'
    label = 'Masthoogte'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte'
    definition = 'Union datatype om een standaard of afwijkende masthoogte te bepalen.'
    waardeObject = DtuLichtmastMasthoogteWaarden

    def __str__(self):
        return UnionTypeField.__str__(self)

