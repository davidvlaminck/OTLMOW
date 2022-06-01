# coding=utf-8
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Draagkabel(AIMObject):
    """Een kabel opgebouwd uit vele strengen, die gebundeld en omhuld worden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Draagkabel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
