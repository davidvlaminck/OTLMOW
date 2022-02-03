# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.KlProfielhoogtemaat import KlProfielhoogtemaat
from OTLMOW.OTLModel.Datatypes.KlProfielsoort import KlProfielsoort


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcProfieltypeWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._profielhoogtemaat = OTLAttribuut(field=KlProfielhoogtemaat,
                                               naam='profielhoogtemaat',
                                               label='profielhoogtemaat',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcProfieltype.profielhoogtemaat',
                                               definition='Voorgedefinieerde hoogtemaat van een profiel.',
                                               owner=self)

        self._profielsoort = OTLAttribuut(field=KlProfielsoort,
                                          naam='profielsoort',
                                          label='profielsoort',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcProfieltype.profielsoort',
                                          definition='Het type profiel (de meest genormeerde types).',
                                          owner=self)

    @property
    def profielhoogtemaat(self):
        """Voorgedefinieerde hoogtemaat van een profiel."""
        return self._profielhoogtemaat.waarde

    @profielhoogtemaat.setter
    def profielhoogtemaat(self, value):
        self._profielhoogtemaat.set_waarde(value, owner=self._parent)

    @property
    def profielsoort(self):
        """Het type profiel (de meest genormeerde types)."""
        return self._profielsoort.waarde

    @profielsoort.setter
    def profielsoort(self, value):
        self._profielsoort.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcProfieltype(ComplexField, AttributeInfo):
    """Complex datatype om de hoogtemaat en de soort van het profiel in te geven."""
    naam = 'DtcProfieltype'
    label = 'Profieltype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcProfieltype'
    definition = 'Complex datatype om de hoogtemaat en de soort van het profiel in te geven.'
    waardeObject = DtcProfieltypeWaarden

    def __str__(self):
        return ComplexField.__str__(self)

