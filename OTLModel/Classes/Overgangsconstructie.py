# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.SchokindexVoertuigkering import SchokindexVoertuigkering
from OTLModel.Classes.AansluitendeConstructie import AansluitendeConstructie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Overgangsconstructie(SchokindexVoertuigkering, AansluitendeConstructie, AttributeInfo):
    """Verbinding tussen twee afschermende constructies voor wegen van verschillende ontwerpen en/of prestatiekenmerken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Overgangsconstructie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AansluitendeConstructie.__init__(self)
        AttributeInfo.__init__(self)
        SchokindexVoertuigkering.__init__(self)
