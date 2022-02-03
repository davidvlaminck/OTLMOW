# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod, ABC
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class ContainerBuis(ABC):
    """Abstracte voor het groeperen van eigenschappen en relaties van buisvormige container elementen. Dit zijn buizen die kabels of andere leidingen kunnen bevatten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self._kleur = OTLAttribuut(field=StringField,
                                   naam='kleur',
                                   label='kleur',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis.kleur',
                                   kardinaliteit_max='*',
                                   definition='De kleur van de coating.',
                                   owner=self)

    @property
    def kleur(self):
        """De kleur van de coating."""
        return self._kleur.waarde

    @kleur.setter
    def kleur(self, value):
        self._kleur.set_waarde(value, owner=self)
