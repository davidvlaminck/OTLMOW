# coding=utf-8
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.KabelgeleidingEnLeidingBevestiging import KabelgeleidingEnLeidingBevestiging
from OTLMOW.OTLModel.Classes.OmhullendeInrichting import OmhullendeInrichting
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kabelgeleiding(KabelgeleidingEnLeidingBevestiging, OmhullendeInrichting, AIMNaamObject):
    """Abstracte voor het groeperen van inrichting met als functie het begeleiden van kabels en leidingen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabelgeleiding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMNaamObject.__init__(self)
        KabelgeleidingEnLeidingBevestiging.__init__(self)
        OmhullendeInrichting.__init__(self)
