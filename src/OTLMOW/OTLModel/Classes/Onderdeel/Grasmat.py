# coding=utf-8
from OTLMOW.OTLModel.Classes.Abstracten.GrazigeVegetatie import GrazigeVegetatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Grasmat(GrazigeVegetatie):
    """Grasvegetatie die een uniforme zode vormt met veel grassen en zeer regelmatig wordt gemaaid."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grasmat'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBeheer', target='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerGrazigeVegetatie')
