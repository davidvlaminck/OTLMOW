# coding=utf-8
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMObject import AIMObject
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Muurdoorgangsstuk(AIMObject, PuntGeometrie):
    """Een hulpstuk als doorgang die zorgt voor een volledige verankering en een volledig waterdichte doorvoering van een persleiding door de wanden van de toegangs- of verbindingsputten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Muurdoorgangsstuk'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Persleiding')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pomp')
