# coding=utf-8
from OTLMOW.OTLModel.Classes.ImplementatieElement.DirectioneleRelatie import DirectioneleRelatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Omhult(DirectioneleRelatie):
    """Deze relatie geeft aan dat het ene onderdeel het andere omhult. Dit vereist geen gesloten omhulling: de omhulling kan een open zijde hebben of bestaan uit open ruimtes. Deze relatie heeft een richting en gaat van het omhullende onderdeel naar het onderdeel dat omhuld wordt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
