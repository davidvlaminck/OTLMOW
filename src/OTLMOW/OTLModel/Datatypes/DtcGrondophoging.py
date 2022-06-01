# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.KlGrondbestemming import KlGrondbestemming
from OTLMOW.OTLModel.Datatypes.KlGrondtoevoegsel import KlGrondtoevoegsel
from OTLMOW.OTLModel.Datatypes.KlGrondwerksoorten import KlGrondwerksoorten


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcGrondophogingWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._grondtoevoegsel = OTLAttribuut(field=KlGrondtoevoegsel,
                                             naam='grondtoevoegsel',
                                             label='grondtoevoegsel',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGrondophoging.grondtoevoegsel',
                                             definition='Aanduiding of er evenuteel een toevoeging aan de grond is gebeurd.',
                                             owner=self)

        self._herkomst = OTLAttribuut(field=KlGrondbestemming,
                                      naam='herkomst',
                                      label='herkomst',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGrondophoging.herkomst',
                                      definition='Bepaalt de origine van de grond.',
                                      owner=self)

        self._soortGrondwerk = OTLAttribuut(field=KlGrondwerksoorten,
                                            naam='soortGrondwerk',
                                            label='soort grondwerk',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGrondophoging.soortGrondwerk',
                                            definition='Het soort werk waar de grond van afkomstig is of voor dient.',
                                            owner=self)

    @property
    def grondtoevoegsel(self):
        """Aanduiding of er evenuteel een toevoeging aan de grond is gebeurd."""
        return self._grondtoevoegsel.get_waarde()

    @grondtoevoegsel.setter
    def grondtoevoegsel(self, value):
        self._grondtoevoegsel.set_waarde(value, owner=self._parent)

    @property
    def herkomst(self):
        """Bepaalt de origine van de grond."""
        return self._herkomst.get_waarde()

    @herkomst.setter
    def herkomst(self, value):
        self._herkomst.set_waarde(value, owner=self._parent)

    @property
    def soortGrondwerk(self):
        """Het soort werk waar de grond van afkomstig is of voor dient."""
        return self._soortGrondwerk.get_waarde()

    @soortGrondwerk.setter
    def soortGrondwerk(self, value):
        self._soortGrondwerk.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcGrondophoging(ComplexField, AttributeInfo):
    """Complex datatype om extra informatie van ophoging van grond te capteren."""
    naam = 'DtcGrondophoging'
    label = 'Grondophoging'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGrondophoging'
    definition = 'Complex datatype om extra informatie van ophoging van grond te capteren.'
    waardeObject = DtcGrondophogingWaarden

    def __str__(self):
        return ComplexField.__str__(self)

