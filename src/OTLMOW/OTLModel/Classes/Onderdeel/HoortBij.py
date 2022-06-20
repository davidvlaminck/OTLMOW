# coding=utf-8
from OTLMOW.OTLModel.Classes.ImplementatieElement.DirectioneleRelatie import DirectioneleRelatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class HoortBij(DirectioneleRelatie):
    """De relatie geeft aan dat een onderdeel of collectie behoort bij, deel van of lid van een (andere) groep of collectie is."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
