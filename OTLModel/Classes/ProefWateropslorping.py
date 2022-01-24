# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefWateropslorping(Proef):
    """Proef waarbij de compactheid of poreusheid van het proefstuk door onderdompeling wordt bepaald."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWateropslorping'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._wateropslorping = OTLAttribuut(field=DtcDocument,
                                             naam='wateropslorping',
                                             label='wateropslorping',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWateropslorping.wateropslorping',
                                             definition='Proef om de wateropslorping van de laag te bepalen.')

    @property
    def wateropslorping(self):
        """Proef om de wateropslorping van de laag te bepalen."""
        return self._wateropslorping.waarde

    @wateropslorping.setter
    def wateropslorping(self, value):
        self._wateropslorping.set_waarde(value, owner=self)
