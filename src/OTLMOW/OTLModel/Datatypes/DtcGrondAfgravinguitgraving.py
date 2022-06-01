# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.KlGrondbestemming import KlGrondbestemming
from OTLMOW.OTLModel.Datatypes.KlGrondwerksoorten import KlGrondwerksoorten


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcGrondAfgravinguitgravingWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._grondbestemming = OTLAttribuut(field=KlGrondbestemming,
                                             naam='grondbestemming',
                                             label='grondbestemming',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGrondAfgravinguitgraving.grondbestemming',
                                             definition='Bepaalt de bestemming van de grond.',
                                             owner=self)

        self._soortGrondwerk = OTLAttribuut(field=KlGrondwerksoorten,
                                            naam='soortGrondwerk',
                                            label='soort grondwerk',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGrondAfgravinguitgraving.soortGrondwerk',
                                            definition='Het soort werk waar de grond van afkomstig is of voor dient.',
                                            owner=self)

    @property
    def grondbestemming(self):
        """Bepaalt de bestemming van de grond."""
        return self._grondbestemming.get_waarde()

    @grondbestemming.setter
    def grondbestemming(self, value):
        self._grondbestemming.set_waarde(value, owner=self._parent)

    @property
    def soortGrondwerk(self):
        """Het soort werk waar de grond van afkomstig is of voor dient."""
        return self._soortGrondwerk.get_waarde()

    @soortGrondwerk.setter
    def soortGrondwerk(self, value):
        self._soortGrondwerk.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcGrondAfgravinguitgraving(ComplexField, AttributeInfo):
    """Complex datatype voor de afgraving of uitgraving van grond."""
    naam = 'DtcGrondAfgravinguitgraving'
    label = 'Grondafgraving en gronduitgraving'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGrondAfgravinguitgraving'
    definition = 'Complex datatype voor de afgraving of uitgraving van grond.'
    waardeObject = DtcGrondAfgravinguitgravingWaarden

    def __str__(self):
        return ComplexField.__str__(self)

