# coding=utf-8
from OTLMOW.OTLModel.Classes.AansluitendeConstructie import AansluitendeConstructie
from OTLMOW.OTLModel.Classes.SchokindexVoertuigkering import SchokindexVoertuigkering


# Generated with OTLClassCreator. To modify: extend, do not edit
class Overgangsconstructie(AansluitendeConstructie, SchokindexVoertuigkering):
    """Verbinding tussen twee afschermende constructies voor wegen van verschillende ontwerpen en/of prestatiekenmerken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Overgangsconstructie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AansluitendeConstructie.__init__(self)
        SchokindexVoertuigkering.__init__(self)
