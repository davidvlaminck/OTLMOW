# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class ForfaitaireAansluiting(AIMNaamObject):
    """Een elektrische aansluiting waarbij met een forfaitair tarief gewerkt wordt, hierbij is er geen teller voorzien door de DNB."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ForfaitaireAansluiting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
