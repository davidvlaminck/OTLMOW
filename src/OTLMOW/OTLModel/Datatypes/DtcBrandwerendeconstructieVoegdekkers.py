# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.DtcAfmetingBxlxhInCm import DtcAfmetingBxlxhInCm
from OTLMOW.OTLModel.Datatypes.KlBrandwerendeconstructieVoegdekkerstype import KlBrandwerendeconstructieVoegdekkerstype


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcBrandwerendeconstructieVoegdekkersWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._afmeting = OTLAttribuut(field=DtcAfmetingBxlxhInCm,
                                      naam='afmeting',
                                      label='afmeting',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcBrandwerendeconstructieVoegdekkers.afmeting',
                                      definition='De breedte,lengte,hoogte in centimeter voor voegdekkers.',
                                      owner=self)

        self._type = OTLAttribuut(field=KlBrandwerendeconstructieVoegdekkerstype,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcBrandwerendeconstructieVoegdekkers.type',
                                  definition='De mogelijke voegdekkerstypes.',
                                  owner=self)

    @property
    def afmeting(self):
        """De breedte,lengte,hoogte in centimeter voor voegdekkers."""
        return self._afmeting.get_waarde()

    @afmeting.setter
    def afmeting(self, value):
        self._afmeting.set_waarde(value, owner=self._parent)

    @property
    def type(self):
        """De mogelijke voegdekkerstypes."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcBrandwerendeconstructieVoegdekkers(ComplexField, AttributeInfo):
    """Complex datatype voor de eigenschappen van de voegdekkers in een brandwerende constructie."""
    naam = 'DtcBrandwerendeconstructieVoegdekkers'
    label = 'Brandwerendeconstructie voegdekkers'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcBrandwerendeconstructieVoegdekkers'
    definition = 'Complex datatype voor de eigenschappen van de voegdekkers in een brandwerende constructie.'
    waardeObject = DtcBrandwerendeconstructieVoegdekkersWaarden

    def __str__(self):
        return ComplexField.__str__(self)

