# coding=utf-8
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMObject import AIMObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Geleiding(AIMObject):
    """Abstracte om de gerelateerde objecten onder 1 noemer te houden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Geleiding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ecoduct')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ecokoker')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ecotunnel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ecovallei')
