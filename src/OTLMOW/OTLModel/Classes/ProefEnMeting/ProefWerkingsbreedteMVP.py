# coding=utf-8
from OTLMOW.OTLModel.Classes.Abstracten.Proef import Proef
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefWerkingsbreedteMVP(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Proef om de afstand tussen de voorkant van het onvervormd systeem tot de maximale dynamische laterale positie van elk onderdeel van het systeem te bepalen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWerkingsbreedteMVP'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.0.0'

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Motorvangplank', deprecated='2.0.0')
