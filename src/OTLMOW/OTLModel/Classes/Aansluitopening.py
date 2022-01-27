# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.LinkendElement import LinkendElement
from src.OTLMOW.OTLModel.Datatypes.KlRioleringVorm import KlRioleringVorm
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Aansluitopening(LinkendElement):
    """Een kleine doorgang in de wand tussen twee kamers, of aan het begin van een leiding."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aansluitopening'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._breedte = OTLAttribuut(field=KwantWrdInMillimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aansluitopening.breedte',
                                     definition='De afstand tussen de uiterste zijden van de aansluitopening in millimeter.')

        self._hoogte = OTLAttribuut(field=KwantWrdInMillimeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aansluitopening.hoogte',
                                    definition='De afstand tussen het hoogste en laagste punt van de aansluitopening in millimeter.')

        self._peil = OTLAttribuut(field=KwantWrdInMeterTAW,
                                  naam='peil',
                                  label='peil',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aansluitopening.peil',
                                  definition='BOK peil in meter-TAW van de knijpopening.')

        self._vorm = OTLAttribuut(field=KlRioleringVorm,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aansluitopening.vorm',
                                  definition='De vorm van de aansluitopening.')

    @property
    def breedte(self):
        """De afstand tussen de uiterste zijden van de aansluitopening in millimeter."""
        return self._breedte.waarde

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def hoogte(self):
        """De afstand tussen het hoogste en laagste punt van de aansluitopening in millimeter."""
        return self._hoogte.waarde

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self)

    @property
    def peil(self):
        """BOK peil in meter-TAW van de knijpopening."""
        return self._peil.waarde

    @peil.setter
    def peil(self, value):
        self._peil.set_waarde(value, owner=self)

    @property
    def vorm(self):
        """De vorm van de aansluitopening."""
        return self._vorm.waarde

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self)
