# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefTextuurdiepte(Proef):
    """Bepaling van de uitwasdiepte van de verharding na een oppervlaktebehandeling volgens NBN EN ISO 13473-1."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefTextuurdiepte'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._textuurdiepte = OTLAttribuut(field=DtcDocument,
                                           naam='textuurdiepte',
                                           label='textuurdiepte',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefTextuurdiepte.textuurdiepte',
                                           definition='Proefresultaten van de textuurdiepte van de toplaag.')

    @property
    def textuurdiepte(self):
        """Proefresultaten van de textuurdiepte van de toplaag."""
        return self._textuurdiepte.waarde

    @textuurdiepte.setter
    def textuurdiepte(self, value):
        self._textuurdiepte.set_waarde(value, owner=self)
