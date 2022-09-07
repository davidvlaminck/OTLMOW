# coding=utf-8
from OTLMOW.OTLModel.Classes.Abstracten.AndereVerharding import AndereVerharding


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ternairmengselverharding(AndereVerharding):
    """Een verharding van gebonden mengsel van grof brekerzand van natuurlijke stenen, eventueel gemengd met brekerzand van hoogovenslakken en steenslag."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ternairmengselverharding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair')
