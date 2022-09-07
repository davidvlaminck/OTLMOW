# coding=utf-8
from OTLMOW.OTLModel.Classes.Abstracten.Bebakening import Bebakening
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ReflectorInLijnvormigElement(Bebakening, LijnGeometrie):
    """Een reflector dat deel uitmaakt van een constructie met als doel de zichtbaarheid van deze constructie te verhogen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ReflectorInLijnvormigElement'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Bebakening.__init__(self)
        LijnGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kantopsluiting')
