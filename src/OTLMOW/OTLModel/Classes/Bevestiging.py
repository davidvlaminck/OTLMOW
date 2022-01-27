# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.NietDirectioneleRelatie import NietDirectioneleRelatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bevestiging(NietDirectioneleRelatie):
    """Deze relatie geeft aan dat twee onderdelen direct fysiek op elkaar bevestigd zijn. Dit kan zowel aan de buitenkant als aan de binnenkant zijn zoals bv. een camera aan een paal of een laagspanningsbord in een kast. Deze relatie heeft geen richting."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
