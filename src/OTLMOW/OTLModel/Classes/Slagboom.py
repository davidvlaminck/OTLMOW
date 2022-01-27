# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.NaampadObject import NaampadObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Slagboom(NaampadObject):
    """Een afsluitingsmechanisme met slagboomarmen dat dient om controle uit te kunnen oefenen over het gebruik van een doorgang of een toegang."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Slagboom'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
