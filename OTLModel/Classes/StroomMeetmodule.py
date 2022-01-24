# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMNaamObject import AIMNaamObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class StroomMeetmodule(AIMNaamObject):
    """Differentieel dat de spanning op de leidingen detecteert en fouten doorgeeft naar de PLC."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StroomMeetmodule'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
