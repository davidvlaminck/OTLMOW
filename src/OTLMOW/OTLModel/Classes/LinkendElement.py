# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class LinkendElement(AIMObject):
    """Abstracte bedoeld om alle eigenschappen en relaties van linkende elementen te groeperen. Linkende elementen zijn objecten die aansluiten op een buis."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement.technischeFiche',
                                             kardinaliteit_max='*',
                                             definition='De technische fiche van een linkend element.',
                                             owner=self)

    @property
    def technischeFiche(self):
        """De technische fiche van een linkend element."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
