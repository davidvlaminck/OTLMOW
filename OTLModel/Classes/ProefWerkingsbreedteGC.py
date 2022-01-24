# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Proef import Proef


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefWerkingsbreedteGC(Proef):
    """Proef om de afstand te bepalen tussen de voorkant van de geleideconstructie in normale positie en de plaats van het verst uitwijkend onderdeel aan de achterzijde van de geleideconstructie bij aanrijding. (gemeten op het voorvlak van een geleideconstructie en loodrecht op de as van de weg)"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWerkingsbreedteGC'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.0.0'

    def __init__(self):
        super().__init__()
