# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.KlToegangscontroleSleuteltype import KlToegangscontroleSleuteltype


# Generated with OTLClassCreator. To modify: extend, do not edit
class Toegangscontrole(AIMNaamObject):
    """Component voor controle van de toegang tot een ruimte of behuizing."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangscontrole'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._heeftBadgelezer = OTLAttribuut(field=BooleanField,
                                             naam='heeftBadgelezer',
                                             label='heeft badgelezer',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangscontrole.heeftBadgelezer',
                                             definition='Geeft aan of de toegangscontrole uitgerust is met een badgelezer.')

        self._heeftSlotMetAfstandsbediening = OTLAttribuut(field=BooleanField,
                                                           naam='heeftSlotMetAfstandsbediening',
                                                           label='heeft slot met afstandsbediening',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangscontrole.heeftSlotMetAfstandsbediening',
                                                           definition='Geeft aan of het objecttype waaraan de toegangscontrole bevestigd is, kan geopend worden via een slot met afstandsbediening.')

        self._sleutelType = OTLAttribuut(field=KlToegangscontroleSleuteltype,
                                         naam='sleutelType',
                                         label='type sleutel',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangscontrole.sleutelType',
                                         definition='De soort sleutel die wordt gebruikt om de toegang te regelen.')

    @property
    def heeftBadgelezer(self):
        """Geeft aan of de toegangscontrole uitgerust is met een badgelezer."""
        return self._heeftBadgelezer.waarde

    @heeftBadgelezer.setter
    def heeftBadgelezer(self, value):
        self._heeftBadgelezer.set_waarde(value, owner=self)

    @property
    def heeftSlotMetAfstandsbediening(self):
        """Geeft aan of het objecttype waaraan de toegangscontrole bevestigd is, kan geopend worden via een slot met afstandsbediening."""
        return self._heeftSlotMetAfstandsbediening.waarde

    @heeftSlotMetAfstandsbediening.setter
    def heeftSlotMetAfstandsbediening(self, value):
        self._heeftSlotMetAfstandsbediening.set_waarde(value, owner=self)

    @property
    def sleutelType(self):
        """De soort sleutel die wordt gebruikt om de toegang te regelen."""
        return self._sleutelType.waarde

    @sleutelType.setter
    def sleutelType(self, value):
        self._sleutelType.set_waarde(value, owner=self)
