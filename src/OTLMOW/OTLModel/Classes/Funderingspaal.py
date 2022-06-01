# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AxiaalDraagvermogen import AxiaalDraagvermogen
from OTLMOW.OTLModel.Classes.Fundering import Fundering
from OTLMOW.OTLModel.Datatypes.DtuDwarsafmetingen import DtuDwarsafmetingen
from OTLMOW.OTLModel.Datatypes.DtuHellingsSchoorhoek import DtuHellingsSchoorhoek
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW


# Generated with OTLClassCreator. To modify: extend, do not edit
class Funderingspaal(AxiaalDraagvermogen, Fundering):
    """Paal die onder het bouwwerk of kunstwerk is aangebracht. Het gewicht van een bouwwerk of kunstwerk wordt overgedragen op die paal. Enkel te gebruiken wanneer het type paal nog niet is vastgelegd bij ontwerp."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingspaal'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AxiaalDraagvermogen.__init__(self)
        Fundering.__init__(self)

        self._afkappeil = OTLAttribuut(field=KwantWrdInMeterTAW,
                                       naam='afkappeil',
                                       label='afkappeil',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingspaal.afkappeil',
                                       definition='De hoogte van het bovenvlak van de paal, na verwijderen van eventuele overlengte, exclusief uitstekende wapening. Berekend ten opzichte van gemiddeld laagwaterpeil te Oostende (TAWpeil).',
                                       owner=self)

        self._dwarsafmetingen = OTLAttribuut(field=DtuDwarsafmetingen,
                                             naam='dwarsafmetingen',
                                             label='dwarsafmetingen',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingspaal.dwarsafmetingen',
                                             definition='Dwarsdoorsnede van het element bv. lengte, breedte, diameter,...',
                                             owner=self)

        self._hellingsSchoorhoek = OTLAttribuut(field=DtuHellingsSchoorhoek,
                                                naam='hellingsSchoorhoek',
                                                label='hellings- of schoorhoek',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingspaal.hellingsSchoorhoek',
                                                definition='De hoek die de paal maakt ten opzichte van de verticale, uitgedrukt in decimale graden of in 1 op x.',
                                                owner=self)

        self._paallengte = OTLAttribuut(field=KwantWrdInMeter,
                                        naam='paallengte',
                                        label='paallengte',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingspaal.paallengte',
                                        definition='Afstand gemeten, in meter, volgens de as van de paal tussen het afkappeil en het aanzetpeil.',
                                        owner=self)

    @property
    def afkappeil(self):
        """De hoogte van het bovenvlak van de paal, na verwijderen van eventuele overlengte, exclusief uitstekende wapening. Berekend ten opzichte van gemiddeld laagwaterpeil te Oostende (TAWpeil)."""
        return self._afkappeil.get_waarde()

    @afkappeil.setter
    def afkappeil(self, value):
        self._afkappeil.set_waarde(value, owner=self)

    @property
    def dwarsafmetingen(self):
        """Dwarsdoorsnede van het element bv. lengte, breedte, diameter,..."""
        return self._dwarsafmetingen.get_waarde()

    @dwarsafmetingen.setter
    def dwarsafmetingen(self, value):
        self._dwarsafmetingen.set_waarde(value, owner=self)

    @property
    def hellingsSchoorhoek(self):
        """De hoek die de paal maakt ten opzichte van de verticale, uitgedrukt in decimale graden of in 1 op x."""
        return self._hellingsSchoorhoek.get_waarde()

    @hellingsSchoorhoek.setter
    def hellingsSchoorhoek(self, value):
        self._hellingsSchoorhoek.set_waarde(value, owner=self)

    @property
    def paallengte(self):
        """Afstand gemeten, in meter, volgens de as van de paal tussen het afkappeil en het aanzetpeil."""
        return self._paallengte.get_waarde()

    @paallengte.setter
    def paallengte(self, value):
        self._paallengte.set_waarde(value, owner=self)
