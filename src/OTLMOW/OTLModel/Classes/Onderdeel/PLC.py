# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Controller import Controller
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KlPLCMerk import KlPLCMerk
from OTLMOW.OTLModel.Datatypes.KlPLCModelnaam import KlPLCModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class PLC(Controller):
    """Een verwerkingseenheid die volgens een vaste cyclus op basis van informatie van zijn ingangen, zijn uitgangen aanstuurt op basis van zijn programma. Omwille van zijn vormfactor kan de eenheid gebruikt worden in een vijandige omgeving."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PLC'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._merk = OTLAttribuut(field=KlPLCMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PLC.merk',
                                  definition='Het merk van de PLC.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlPLCModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PLC.modelnaam',
                                       definition='De modelnaam van de PLC.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technischeFiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PLC.technischeFiche',
                                             definition='De technische fiche van de PLC.',
                                             owner=self)

    @property
    def merk(self):
        """Het merk van de PLC."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de PLC."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """De technische fiche van de PLC."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
