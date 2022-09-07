# coding=utf-8
from OTLMOW.OTLModel.Classes.Abstracten.AfwijkendeKantopsluiting import AfwijkendeKantopsluiting


# Generated with OTLClassCreator. To modify: extend, do not edit
class TrottoirbandWatergreppelAfw(AfwijkendeKantopsluiting):
    """Afwijkende kantopsluiting, die een trottoirband en een watergreppel combineert in een geheel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandWatergreppelAfw'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
