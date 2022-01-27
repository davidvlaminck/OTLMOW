# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.Luchtkwaliteittoestel import Luchtkwaliteittoestel
from src.OTLMOW.OTLModel.Datatypes.KlAlgIngressProtectionCode import KlAlgIngressProtectionCode


# Generated with OTLClassCreator. To modify: extend, do not edit
class LuchtkwaliteitControleUnit(Luchtkwaliteittoestel):
    """Onderdeel voor de aansturing en interpretatie van het signaal tussen de LuchtkwaliteitZenderOntvanger en de LuchtkwaliteitSensor."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LuchtkwaliteitControleUnit'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._ipKlasse = OTLAttribuut(field=KlAlgIngressProtectionCode,
                                      naam='ipKlasse',
                                      label='ingress protection klasse',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LuchtkwaliteitControleUnit.ipKlasse',
                                      definition='De IP-codering als een aanduiding voor de mate van beveiliging van de constructie van elektrische of elektronische apparatuur tegen eigen schade door gebruik in "vijandige omgevingen" en tegen eventueel gevaar voor de gebruiker volgens IEC 60529.')

    @property
    def ipKlasse(self):
        """De IP-codering als een aanduiding voor de mate van beveiliging van de constructie van elektrische of elektronische apparatuur tegen eigen schade door gebruik in "vijandige omgevingen" en tegen eventueel gevaar voor de gebruiker volgens IEC 60529."""
        return self._ipKlasse.waarde

    @ipKlasse.setter
    def ipKlasse(self, value):
        self._ipKlasse.set_waarde(value, owner=self)
