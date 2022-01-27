# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AndereVerharding import AndereVerharding


# Generated with OTLClassCreator. To modify: extend, do not edit
class Walsbetonverharding(AndereVerharding):
    """Een verharding van aardvochtig beton met maximum korrelafmeting (40mm) en cementgehalte tussen 200-250 kg per kubieke meter om hogere druksterktes (minimum 20 Newton) te bekomen, wordt zowel toegepast voor wegverharding als in funderingen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Walsbetonverharding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
