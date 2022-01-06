# coding=utf-8
from OTLModel.Classes.Seinlantaarn import Seinlantaarn


# Generated with OTLClassCreator. To modify: extend, do not edit
class Knipperlantaarn(Seinlantaarn):
    """Een lantaarn bestaande uit één of meerdere knipperende oranje-geel verkeerslichten bevestigd op een steun, teneinde de weggebruiker te waarschuwen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Knipperlantaarn"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
