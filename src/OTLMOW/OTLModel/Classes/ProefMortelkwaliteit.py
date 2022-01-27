# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Proef import Proef
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefMortelkwaliteit(Proef):
    """Controle van de sterkte van voegmortel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefMortelkwaliteit'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._mortelkwaliteit = OTLAttribuut(field=DtcDocument,
                                             naam='mortelkwaliteit',
                                             label='mortelkwaliteit',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefMortelkwaliteit.mortelkwaliteit',
                                             definition='Een rapport van de mortelkwaliteit van de onderbouw laag.')

    @property
    def mortelkwaliteit(self):
        """Een rapport van de mortelkwaliteit van de onderbouw laag."""
        return self._mortelkwaliteit.waarde

    @mortelkwaliteit.setter
    def mortelkwaliteit(self, value):
        self._mortelkwaliteit.set_waarde(value, owner=self)
