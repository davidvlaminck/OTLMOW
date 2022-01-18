# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMObject import AIMObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Muurdoorgangsstuk(AIMObject, AttributeInfo):
    """Een hulpstuk als doorgang die zorgt voor een volledige verankering en een volledig waterdichte doorvoering van een persleiding door de wanden van de toegangs- of verbindingsputten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Muurdoorgangsstuk'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        AttributeInfo.__init__(self)
