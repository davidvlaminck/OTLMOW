# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.SoftwareToegang import SoftwareToegang
from OTLMOW.OTLModel.Datatypes.DtcSoftwarePoortconfiguratie import DtcSoftwarePoortconfiguratie


# Generated with OTLClassCreator. To modify: extend, do not edit
class LogischePoort(SoftwareToegang):
    """Een 'logische' connectie waaraan een nummer tussen 0 en 65536 wordt toegewezen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LogischePoort'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._poortconfiguratie = OTLAttribuut(field=DtcSoftwarePoortconfiguratie,
                                               naam='poortconfiguratie',
                                               label='poortconfiguratie',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LogischePoort.poortconfiguratie',
                                               definition='Type TCP of UDP service.',
                                               owner=self)

    @property
    def poortconfiguratie(self):
        """Type TCP of UDP service."""
        return self._poortconfiguratie.get_waarde()

    @poortconfiguratie.setter
    def poortconfiguratie(self, value):
        self._poortconfiguratie.set_waarde(value, owner=self)
