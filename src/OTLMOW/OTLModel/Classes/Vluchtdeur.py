# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from src.OTLMOW.OTLModel.Classes.Deur import Deur
from src.OTLMOW.OTLModel.Classes.BevestigingGC import BevestigingGC


# Generated with OTLClassCreator. To modify: extend, do not edit
class Vluchtdeur(AIMObject, Deur, BevestigingGC):
    """Deur voor het ontvluchten in geval van calamiteiten weg van de incidentlocatie naar een veilige zone. Een vluchtdeur wordt onder alle omstandigheden zonder sleutel geopend en dit met beperkte kracht."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Vluchtdeur'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        BevestigingGC.__init__(self)
        Deur.__init__(self)
