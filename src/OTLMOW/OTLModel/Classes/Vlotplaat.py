# coding=utf-8
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Vlotplaat(AIMObject):
    """Het doel van een vlotplaat is het tegengaan van de negatieve effecten bij eventuele nazakkingen van het aansluitende wegdek of spoorlijn. Ze voorkomen een te abrupte en ongewenste overgang."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Vlotplaat'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
