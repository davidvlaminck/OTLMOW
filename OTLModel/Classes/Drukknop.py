# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.NietWeggebondenDetectie import NietWeggebondenDetectie
from OTLModel.Datatypes.DtcTijdsduur import DtcTijdsduur
from OTLModel.Datatypes.KlDrukknopMerk import KlDrukknopMerk
from OTLModel.Datatypes.KlDrukknopModelnaam import KlDrukknopModelnaam
from OTLModel.Datatypes.KlDrukknopSoort import KlDrukknopSoort


# Generated with OTLClassCreator. To modify: extend, do not edit
class Drukknop(NietWeggebondenDetectie, AttributeInfo):
    """Drukknoppen zijn de toestellen die opgesteld zijn op kruispunten om de aanwezigheid te melden van voetgangers of fietsers die de rijweg wensen over te steken of voor het aanmelden van openbaar vervoer. De toestellen sturen een geheugenelement (module voor de sturing en visualisatie) in de verkeersregelaar aan, zodanig dat een kortstondig indrukken van de drukknop of kortstondig aanraken van de sensor volstaat opdat de aanvraag tot doorgang blijft gelden tot de doorgang verleend wordt"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Drukknop'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        NietWeggebondenDetectie.__init__(self)

        self._bewakingstijd = OTLAttribuut(field=DtcTijdsduur,
                                           naam='bewakingstijd',
                                           label='bewakingstijd',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Drukknop.bewakingstijd',
                                           definition='Wachttijd (in uren) waarna een alarm pas mag optreden.')

        self._merk = OTLAttribuut(field=KlDrukknopMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Drukknop.merk',
                                  definition='De naam van het merk van de drukknop.')

        self._modelnaam = OTLAttribuut(field=KlDrukknopModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Drukknop.modelnaam',
                                       definition='De modelnaam van de drukknop.')

        self._soortDrukknop = OTLAttribuut(field=KlDrukknopSoort,
                                           naam='soortDrukknop',
                                           label='soort drukknop',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Drukknop.soortDrukknop',
                                           definition='Doelgroep van de drukknop (voetganger, fietser, ruiter,...).')

    @property
    def bewakingstijd(self):
        """Wachttijd (in uren) waarna een alarm pas mag optreden."""
        return self._bewakingstijd.waarde

    @bewakingstijd.setter
    def bewakingstijd(self, value):
        self._bewakingstijd.set_waarde(value, owner=self)

    @property
    def merk(self):
        """De naam van het merk van de drukknop."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de drukknop."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def soortDrukknop(self):
        """Doelgroep van de drukknop (voetganger, fietser, ruiter,...)."""
        return self._soortDrukknop.waarde

    @soortDrukknop.setter
    def soortDrukknop(self, value):
        self._soortDrukknop.set_waarde(value, owner=self)
