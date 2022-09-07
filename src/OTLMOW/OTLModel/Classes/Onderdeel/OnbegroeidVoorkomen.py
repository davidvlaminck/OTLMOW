# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.AndereVerharding import AndereVerharding
from OTLMOW.OTLModel.Datatypes.KlOnbegroeidVoorkomenType import KlOnbegroeidVoorkomenType


# Generated with OTLClassCreator. To modify: extend, do not edit
class OnbegroeidVoorkomen(AndereVerharding):
    """Een ander fysiek voorkomen van het aardoppervlak dat niet vegetatief is."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OnbegroeidVoorkomen'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair')

        self._type = OTLAttribuut(field=KlOnbegroeidVoorkomenType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OnbegroeidVoorkomen.type',
                                  definition='Type van onbegroeid voorkomen.',
                                  owner=self)

    @property
    def type(self):
        """Type van onbegroeid voorkomen."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
