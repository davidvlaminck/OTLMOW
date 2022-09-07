# coding=utf-8
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ForfaitaireAansluiting(AIMNaamObject, PuntGeometrie):
    """Een elektrische aansluiting waarbij met een forfaitair tarief gewerkt wordt, hierbij is er geen teller voorzien door de DNB."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ForfaitaireAansluiting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring')
