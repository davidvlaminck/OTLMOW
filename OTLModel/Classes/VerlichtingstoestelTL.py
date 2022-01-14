# coding=utf-8
from OTLModel.Classes.Verlichtingstoestel import Verlichtingstoestel
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class VerlichtingstoestelTL(Verlichtingstoestel):
    """Het geheel van de TL-lamp en de behuizing die werden samengesteld met als doel:* de lichtstroom van de lichtbronnen hoofdzakelijk op het te verlichten oppervlak (doorlopende wegsectie, conflictgebied,...) te richten, teneinde de zichtbaarheid te verhogen;* de lichtstroom te beheersen zodat de weggebruikers niet verblind worden en de lichthinder beperkt wordt;* het optisch systeem, de lichtbronnen en de hulpapparatuur tegen uitwendige invloeden te beschermen"""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelTL"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.lichtpuntHoogte = KwantWrdInMeter()
        """Hoogte van het lichtpunt ten opzichte van de rijweg."""
        self.lichtpuntHoogte.naam = "lichtpuntHoogte"
        self.lichtpuntHoogte.label = "lichtpunt hoogte"
        self.lichtpuntHoogte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelTL.lichtpuntHoogte"
        self.lichtpuntHoogte.definition = "Hoogte van het lichtpunt ten opzichte van de rijweg."
        self.lichtpuntHoogte.constraints = ""
        self.lichtpuntHoogte.usagenote = ""
        self.lichtpuntHoogte.deprecated_version = ""
