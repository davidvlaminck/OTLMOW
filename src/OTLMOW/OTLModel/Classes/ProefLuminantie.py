# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.Proef import Proef
from src.OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefLuminantie(Proef):
    """Bij gebrek aan Qd-meting kan de luminantiefactor ß van wegmarkeringen gebruikt worden om het contrast met het wegdek en bijgevolg de dagzichtbaarheid te bepalen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefLuminantie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._luminantiefactor = OTLAttribuut(field=FloatOrDecimalField,
                                              naam='luminantiefactor',
                                              label='luminantiefactor',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefLuminantie.luminantiefactor',
                                              definition='Waarde om het contrast met het wegdek en bijgevolg de dagzichtbaarheid te bepalen.')

    @property
    def luminantiefactor(self):
        """Waarde om het contrast met het wegdek en bijgevolg de dagzichtbaarheid te bepalen."""
        return self._luminantiefactor.waarde

    @luminantiefactor.setter
    def luminantiefactor(self, value):
        self._luminantiefactor.set_waarde(value, owner=self)
