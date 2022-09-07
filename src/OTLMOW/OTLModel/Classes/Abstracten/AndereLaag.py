# coding=utf-8
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.Abstracten.Laag import Laag
from OTLMOW.OTLModel.Classes.Abstracten.LaagProductidentificatiecode import LaagProductidentificatiecode


# Generated with OTLClassCreator. To modify: extend, do not edit
class AndereLaag(Laag, LaagProductidentificatiecode):
    """Abstracte als tussenlaag voor de andere laag-objecten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AndereLaag'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        Laag.__init__(self)
        LaagProductidentificatiecode.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair')
