# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Behuizing import Behuizing
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class Lokaal(Behuizing):
    """Een ruimte binnen een gebouw."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Lokaal'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._grondplan = OTLAttribuut(field=DtcDocument,
                                       naam='grondplan',
                                       label='grondplan',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Lokaal.grondplan',
                                       definition='Plattegrond van het lokaal met aanduidingen van de verschillende aanwezige elementen zoals kasten met kastnummers, toegangscontrole en meer.')

    @property
    def grondplan(self):
        """Plattegrond van het lokaal met aanduidingen van de verschillende aanwezige elementen zoals kasten met kastnummers, toegangscontrole en meer."""
        return self._grondplan.waarde

    @grondplan.setter
    def grondplan(self, value):
        self._grondplan.set_waarde(value, owner=self)
