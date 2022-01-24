# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AndereVerharding import AndereVerharding


# Generated with OTLClassCreator. To modify: extend, do not edit
class ColloidaalBeton(AndereVerharding):
    """Betonspecie voor toepassing onder water, waarvan de samenhang is verbeterd door toevoeging van een waterretentiemiddel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ColloidaalBeton'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
