# coding=utf-8
from OTLMOW.OTLModel.Classes.Abstracten.Waarschuwingslantaarn import Waarschuwingslantaarn


# Generated with OTLClassCreator. To modify: extend, do not edit
class Vooraankondiging(Waarschuwingslantaarn):
    """Geheel van één of meerdere knipperlantaarns, inclusief knipperdoos, bevestigd op een draagconstructie ter waarschuwing (ter benadering) van een verkeerslichtengeregeld kruispunt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Vooraankondiging'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
