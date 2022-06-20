# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod, ABC
from OTLMOW.OTLModel.Datatypes.KlVriTypeweggebruiker import KlVriTypeweggebruiker


# Generated with OTLClassCreator. To modify: extend, do not edit
class TypeWeggebruiker(ABC):
    """Abstracte klasse die het type weggebruiker met een attribuut (volgens keuzelijst) aangeeft."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#TypeWeggebruiker'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self._typeWeggebruiker = OTLAttribuut(field=KlVriTypeweggebruiker,
                                              naam='typeWeggebruiker',
                                              label='type weggebruiker',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#TypeWeggebruiker.typeWeggebruiker',
                                              definition='het type weggebruiker.',
                                              owner=self)

    @property
    def typeWeggebruiker(self):
        """het type weggebruiker."""
        return self._typeWeggebruiker.get_waarde()

    @typeWeggebruiker.setter
    def typeWeggebruiker(self, value):
        self._typeWeggebruiker.set_waarde(value, owner=self)
