# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ConstructiefObject import ConstructiefObject
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KlTypeHorizontalePlaat import KlTypeHorizontalePlaat


# Generated with OTLClassCreator. To modify: extend, do not edit
class HorizontaleConstructieplaat(ConstructiefObject):
    """Een plaat die dient ter constructie en die horizontaal wordt gebruikt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HorizontaleConstructieplaat'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HorizontaleConstructieplaat.technischeFiche',
                                             definition='De technische fiche van de plaat.',
                                             owner=self)

        self._type = OTLAttribuut(field=KlTypeHorizontalePlaat,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HorizontaleConstructieplaat.type',
                                  definition='Het type horizontale plaat.',
                                  owner=self)

    @property
    def technischeFiche(self):
        """De technische fiche van de plaat."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type horizontale plaat."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
