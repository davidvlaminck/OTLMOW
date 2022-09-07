# coding=utf-8
from OTLMOW.OTLModel.Classes.Abstracten.Inloopbehuizing import Inloopbehuizing


# Generated with OTLClassCreator. To modify: extend, do not edit
class Container(Inloopbehuizing):
    """Een verplaatsbare behuizing voor het beschermen van technieken en materialen waarin het omwille van de grootte en toegankelijkheid mogelijk is om rond te lopen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Container'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag')
