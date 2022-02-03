# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Ruigte import Ruigte
from OTLMOW.OTLModel.Datatypes.KlNSB import KlNSB


# Generated with OTLClassCreator. To modify: extend, do not edit
class NatteRuigte(Ruigte):
    """Een natte ruigte is een vegetatie op natte standplaatsen die ontstaat na het wegvallen van beheer (maaien of begrazen) en dat gepaard gaat met de vestiging en/of uitbreiding van forse plantensoorten (zogenaamde ruigtekruiden). Deze ruigtekruiden zijn gekenmerkt door hun overblijvende natuur, hun snelle groei en de productie van aanzienlijke hoeveelheden strooisel, waardoor ze andere, vooral kleinere soorten, verdringen en de vestiging van andere soorten verhinderen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NatteRuigte'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._huidigNatuurbeeld = OTLAttribuut(field=KlNSB,
                                               naam='huidigNatuurbeeld',
                                               label='huidig natuurbeeld',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NatteRuigte.huidigNatuurbeeld',
                                               definition='Bepaling van het vegetatietype op basis van terreininventarisatie.',
                                               owner=self)

    @property
    def huidigNatuurbeeld(self):
        """Bepaling van het vegetatietype op basis van terreininventarisatie."""
        return self._huidigNatuurbeeld.waarde

    @huidigNatuurbeeld.setter
    def huidigNatuurbeeld(self, value):
        self._huidigNatuurbeeld.set_waarde(value, owner=self)
