# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Appurtenance import Appurtenance
from OTLMOW.OTLModel.Datatypes.KlTelecommunicationsAppurtenanceType import KlTelecommunicationsAppurtenanceType


# Generated with OTLClassCreator. To modify: extend, do not edit
class TelecommunicationsAppurtenance(Appurtenance):
    """Appurtenance-objecten zijn “toebehoren” of accessoires, dus allerlei apparaten, toestellen en dergelijke,kortom diverse soorten leidingelementen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#TelecommunicationsAppurtenance'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._appurtenanceType = OTLAttribuut(field=KlTelecommunicationsAppurtenanceType,
                                              naam='appurtenanceType',
                                              label='appurtenance type',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#TelecommunicationsAppurtenance.appurtenanceType',
                                              definition='Classificatie van accessoires.',
                                              owner=self)

    @property
    def appurtenanceType(self):
        """Classificatie van accessoires."""
        return self._appurtenanceType.get_waarde()

    @appurtenanceType.setter
    def appurtenanceType(self, value):
        self._appurtenanceType.set_waarde(value, owner=self)
