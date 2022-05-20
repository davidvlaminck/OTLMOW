# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcKrimpvoegWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._krimpvoegFrequentie = OTLAttribuut(field=KwantWrdInMeter,
                                                 naam='krimpvoegFrequentie',
                                                 label='krimpvoeg frequentie',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcKrimpvoeg.krimpvoegFrequentie',
                                                 definition='De afstand tussen de krimpvoegen in meter.',
                                                 owner=self)

        self._totaleLengte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='totaleLengte',
                                          label='lengte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcKrimpvoeg.totaleLengte',
                                          definition='De totale lengte in meter.',
                                          owner=self)

    @property
    def krimpvoegFrequentie(self):
        """De afstand tussen de krimpvoegen in meter."""
        return self._krimpvoegFrequentie.get_waarde()

    @krimpvoegFrequentie.setter
    def krimpvoegFrequentie(self, value):
        self._krimpvoegFrequentie.set_waarde(value, owner=self._parent)

    @property
    def totaleLengte(self):
        """De totale lengte in meter."""
        return self._totaleLengte.get_waarde()

    @totaleLengte.setter
    def totaleLengte(self, value):
        self._totaleLengte.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcKrimpvoeg(ComplexField, AttributeInfo):
    """Complex datatype voor de informatie van de krimpvoegen."""
    naam = 'DtcKrimpvoeg'
    label = 'Krimpvoeg'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcKrimpvoeg'
    definition = 'Complex datatype voor de informatie van de krimpvoegen.'
    waardeObject = DtcKrimpvoegWaarden

    def __str__(self):
        return ComplexField.__str__(self)

