# coding=utf-8
from OTLMOW.OTLModel.Classes.Waarschuwingslantaarn import Waarschuwingslantaarn


# Generated with OTLClassCreator. To modify: extend, do not edit
class Seinbord(Waarschuwingslantaarn):
    """Paneel met waarschuwingstekst in oplichtende letters in de nabijheid van het kruispunt om weggebruikers te wijzen op een gesloten overweg, openstaande brug, voorbijrijdende tram,..."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbord'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
