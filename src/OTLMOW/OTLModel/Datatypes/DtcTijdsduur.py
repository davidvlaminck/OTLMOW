# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.KwantWrdInMinuut import KwantWrdInMinuut
from OTLMOW.OTLModel.Datatypes.KwantWrdInSeconde import KwantWrdInSeconde
from OTLMOW.OTLModel.Datatypes.KwantWrdInUur import KwantWrdInUur


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcTijdsduurWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._minuten = OTLAttribuut(field=KwantWrdInMinuut,
                                     naam='minuten',
                                     label='minuten',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTijdsduur.minuten',
                                     definition='Het aantal minuten.',
                                     owner=self)

        self._seconden = OTLAttribuut(field=KwantWrdInSeconde,
                                      naam='seconden',
                                      label='seconden',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTijdsduur.seconden',
                                      definition='Het aantal seconden.',
                                      owner=self)

        self._uren = OTLAttribuut(field=KwantWrdInUur,
                                  naam='uren',
                                  label='uren',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTijdsduur.uren',
                                  definition='Het aantal uren.',
                                  owner=self)

    @property
    def minuten(self):
        """Het aantal minuten."""
        return self._minuten.get_waarde()

    @minuten.setter
    def minuten(self, value):
        self._minuten.set_waarde(value, owner=self._parent)

    @property
    def seconden(self):
        """Het aantal seconden."""
        return self._seconden.get_waarde()

    @seconden.setter
    def seconden(self, value):
        self._seconden.set_waarde(value, owner=self._parent)

    @property
    def uren(self):
        """Het aantal uren."""
        return self._uren.get_waarde()

    @uren.setter
    def uren(self, value):
        self._uren.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcTijdsduur(ComplexField, AttributeInfo):
    """Complex datatype voor de instelling van een tijdsbepaling."""
    naam = 'DtcTijdsduur'
    label = 'Tijdsduur'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTijdsduur'
    definition = 'Complex datatype voor de instelling van een tijdsbepaling.'
    waardeObject = DtcTijdsduurWaarden

    def __str__(self):
        return ComplexField.__str__(self)

