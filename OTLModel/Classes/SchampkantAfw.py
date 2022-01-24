# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AfwijkendeKantopsluiting import AfwijkendeKantopsluiting


# Generated with OTLClassCreator. To modify: extend, do not edit
class SchampkantAfw(AfwijkendeKantopsluiting):
    """Afwijkende kantopsluiting, die zones van voertuigenverkeer onderling of voertuigenzones van andere verkeerszones scheidt en de overschrijding door voertuigen bemoeilijkt maar geen voertuigkerende functie heeft."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SchampkantAfw'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
