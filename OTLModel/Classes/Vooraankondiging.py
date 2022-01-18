# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Waarschuwingslantaarn import Waarschuwingslantaarn


# Generated with OTLClassCreator. To modify: extend, do not edit
class Vooraankondiging(Waarschuwingslantaarn, AttributeInfo):
    """Geheel van één of meerdere knipperlantaarns, inclusief knipperdoos, bevestigd op een draagconstructie ter waarschuwing (ter benadering) van een verkeerslichtengeregeld kruispunt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Vooraankondiging'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        Waarschuwingslantaarn.__init__(self)
