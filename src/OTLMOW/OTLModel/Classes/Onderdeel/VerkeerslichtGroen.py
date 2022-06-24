# coding=utf-8
from OTLMOW.OTLModel.Classes.Abstracten.Verkeerslicht import Verkeerslicht


# Generated with OTLClassCreator. To modify: extend, do not edit
class VerkeerslichtGroen(Verkeerslicht):
    """Een lichtbron met groene kleur om de weggebruikers aan te geven dat het verkeerslicht mag voorbijgereden worden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerkeerslichtGroen'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
