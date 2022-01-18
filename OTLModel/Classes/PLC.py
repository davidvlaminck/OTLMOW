# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Controller import Controller
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KlPLCMerk import KlPLCMerk
from OTLModel.Datatypes.KlPLCModelnaam import KlPLCModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class PLC(Controller, AttributeInfo):
    """Een verwerkingseenheid die volgens een vaste cyclus op basis van informatie van zijn ingangen, zijn uitgangen aanstuurt op basis van zijn programma. Omwille van zijn vormfactor kan de eenheid gebruikt worden in een vijandige omgeving."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PLC'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        Controller.__init__(self)

        self._merk = OTLAttribuut(field=KlPLCMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PLC.merk',
                                  definition='Het merk van de PLC.')

        self._modelnaam = OTLAttribuut(field=KlPLCModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PLC.modelnaam',
                                       definition='De modelnaam van de PLC.')

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technischeFiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PLC.technischeFiche',
                                             definition='De technische fiche van de PLC.')

    @property
    def merk(self):
        """Het merk van de PLC."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de PLC."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """De technische fiche van de PLC."""
        return self._technischeFiche.waarde

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
