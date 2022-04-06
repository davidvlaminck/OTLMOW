# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.KlGrondbestemming import KlGrondbestemming
from OTLMOW.OTLModel.Datatypes.KlGrondwerksoorten import KlGrondwerksoorten


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcGrondafdekkingWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._herkomst = OTLAttribuut(field=KlGrondbestemming,
                                      naam='herkomst',
                                      label='herkomst',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGrondafdekking.herkomst',
                                      definition='Bepaalt de origine van de grond.',
                                      owner=self)

        self._soortGrondwerk = OTLAttribuut(field=KlGrondwerksoorten,
                                            naam='soortGrondwerk',
                                            label='soort grondwerk',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGrondafdekking.soortGrondwerk',
                                            definition='Het soort werk waar de grond van afkomstig is of voor dient.',
                                            owner=self)

    @property
    def herkomst(self):
        """Bepaalt de origine van de grond."""
        return self._herkomst.waarde

    @herkomst.setter
    def herkomst(self, value):
        self._herkomst.set_waarde(value, owner=self._parent)

    @property
    def soortGrondwerk(self):
        """Het soort werk waar de grond van afkomstig is of voor dient."""
        return self._soortGrondwerk.waarde

    @soortGrondwerk.setter
    def soortGrondwerk(self, value):
        self._soortGrondwerk.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcGrondafdekking(ComplexField, AttributeInfo):
    """Complex datatype om extra informatie van de afdekking van grond te capteren."""
    naam = 'DtcGrondafdekking'
    label = 'Grondafdekking'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGrondafdekking'
    definition = 'Complex datatype om extra informatie van de afdekking van grond te capteren.'
    waardeObject = DtcGrondafdekkingWaarden

    def __str__(self):
        return ComplexField.__str__(self)

