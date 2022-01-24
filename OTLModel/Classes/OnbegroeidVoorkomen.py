# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AndereVerharding import AndereVerharding
from OTLModel.Datatypes.KlOnbegroeidVoorkomenType import KlOnbegroeidVoorkomenType


# Generated with OTLClassCreator. To modify: extend, do not edit
class OnbegroeidVoorkomen(AndereVerharding):
    """Een ander fysiek voorkomen van het aardoppervlak dat niet vegetatief is."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OnbegroeidVoorkomen'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._type = OTLAttribuut(field=KlOnbegroeidVoorkomenType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OnbegroeidVoorkomen.type',
                                  definition='Type van onbegroeid voorkomen.')

    @property
    def type(self):
        """Type van onbegroeid voorkomen."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
