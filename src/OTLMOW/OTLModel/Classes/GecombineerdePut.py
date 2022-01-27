# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class GecombineerdePut(AIMObject):
    """Alle putrelaties."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GecombineerdePut'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
