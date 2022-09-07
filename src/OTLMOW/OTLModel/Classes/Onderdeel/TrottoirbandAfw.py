# coding=utf-8
from OTLMOW.OTLModel.Classes.Abstracten.AfwijkendeKantopsluiting import AfwijkendeKantopsluiting


# Generated with OTLClassCreator. To modify: extend, do not edit
class TrottoirbandAfw(AfwijkendeKantopsluiting):
    """Afwijkende kantopsluiting,bestemd om de rand van de verharding te beschermen en te versterken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandAfw'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KantstrookAfw')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KantstrookStd')
