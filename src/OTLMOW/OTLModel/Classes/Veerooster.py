# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ComplexeGeleiding import ComplexeGeleiding
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Veerooster(ComplexeGeleiding):
    """Een veerooster is een infrastructurele voorziening die is aangebracht in het wegdek om te voorkomen dat vee een gebied binnenkomt of verlaat."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Veerooster'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._breedte = OTLAttribuut(field=KwantWrdInMeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Veerooster.breedte',
                                     definition='De breedte van het veerooster in meter.')

    @property
    def breedte(self):
        """De breedte van het veerooster in meter."""
        return self._breedte.waarde

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)
