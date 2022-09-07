# coding=utf-8
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class FieldOfView(AIMNaamObject, VlakGeometrie):
    """2D-polygoon die het gezichtsveld van een gekoppeld camera onderdeel voorstelt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FieldOfView'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.4.0'

    def __init__(self):
        AIMNaamObject.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera', deprecated='2.4.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera', deprecated='2.4.0')
