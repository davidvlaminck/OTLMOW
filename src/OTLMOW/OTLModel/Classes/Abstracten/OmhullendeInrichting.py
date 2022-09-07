# coding=utf-8
from abc import abstractmethod, ABC


# Generated with OTLClassCreator. To modify: extend, do not edit
class OmhullendeInrichting(ABC):
    """Abstracte voor het groeperen van de relaties voor onderdelen die kabels kunnen omhullen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#OmhullendeInrichting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Leiding')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#ElectricityCable')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Pipe')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#TelecommunicationsCable')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Beschermbuis')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Datakabel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Signaalkabel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Telecomkabel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedingskabel')

        pass
