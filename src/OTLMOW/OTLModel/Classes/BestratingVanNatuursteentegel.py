# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Bestrating import Bestrating
from OTLMOW.OTLModel.Datatypes.KlBestratingAfwerking import KlBestratingAfwerking
from OTLMOW.OTLModel.Datatypes.KlBestratingselementAfmetingLxB import KlBestratingselementAfmetingLxB
from OTLMOW.OTLModel.Datatypes.KlNatuursteentegelGebruiksklasse import KlNatuursteentegelGebruiksklasse


# Generated with OTLClassCreator. To modify: extend, do not edit
class BestratingVanNatuursteentegel(Bestrating):
    """Een buitentegel (of buitenplavei) is elk element van natuursteen gebruikt als bestratingsmateriaal, waarvan de breedte groter is dan 150 mm en doorgaans groter is dan twee maal de dikte volgens PTV841."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanNatuursteentegel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._afmetingVanBestratingselementLxB = OTLAttribuut(field=KlBestratingselementAfmetingLxB,
                                                              naam='afmetingVanBestratingselementLxB',
                                                              label='afmeting van bestratingselement LxB',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanNatuursteentegel.afmetingVanBestratingselementLxB',
                                                              definition='De lengte en breedte van het bestratingselement in millimeter.')

        self._afwerking = OTLAttribuut(field=KlBestratingAfwerking,
                                       naam='afwerking',
                                       label='afwerking',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanNatuursteentegel.afwerking',
                                       definition='Bepaling van de afwerking van het oppervlak van de natuursteentegels.')

        self._gebruiksklasse = OTLAttribuut(field=KlNatuursteentegelGebruiksklasse,
                                            naam='gebruiksklasse',
                                            label='gebruiksklasse',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanNatuursteentegel.gebruiksklasse',
                                            definition='Bepaling van het toegelaten verkeer en belasting op de bestrating van natuursteentegels.')

    @property
    def afmetingVanBestratingselementLxB(self):
        """De lengte en breedte van het bestratingselement in millimeter."""
        return self._afmetingVanBestratingselementLxB.waarde

    @afmetingVanBestratingselementLxB.setter
    def afmetingVanBestratingselementLxB(self, value):
        self._afmetingVanBestratingselementLxB.set_waarde(value, owner=self)

    @property
    def afwerking(self):
        """Bepaling van de afwerking van het oppervlak van de natuursteentegels."""
        return self._afwerking.waarde

    @afwerking.setter
    def afwerking(self, value):
        self._afwerking.set_waarde(value, owner=self)

    @property
    def gebruiksklasse(self):
        """Bepaling van het toegelaten verkeer en belasting op de bestrating van natuursteentegels."""
        return self._gebruiksklasse.waarde

    @gebruiksklasse.setter
    def gebruiksklasse(self, value):
        self._gebruiksklasse.set_waarde(value, owner=self)
