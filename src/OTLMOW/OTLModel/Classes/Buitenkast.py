# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from src.OTLMOW.OTLModel.Classes.Kast import Kast
from src.OTLMOW.OTLModel.Datatypes.KlAlgIngressProtectionCode import KlAlgIngressProtectionCode
from src.OTLMOW.OTLModel.Datatypes.KlBuitenkastVerfraaid import KlBuitenkastVerfraaid
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInJaar import KwantWrdInJaar


# Generated with OTLClassCreator. To modify: extend, do not edit
class Buitenkast(Kast):
    """Abstracte voor kasten die typisch buiten staan en daarom bestand moeten zijn tegen de elementen en verfraaiing kunnen krijgen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buitenkast'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._ipKlasse = OTLAttribuut(field=KlAlgIngressProtectionCode,
                                      naam='ipKlasse',
                                      label='ingress protection klasse',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buitenkast.ipKlasse',
                                      definition='De IP-codering als een aanduiding voor de mate van beveiliging van de constructie van elektrische of elektronische apparatuur tegen eigen schade door gebruik in "vijandige omgevingen" en tegen eventueel gevaar voor de gebruiker volgens IEC 60529.')

        self._keuringsfrequentie = OTLAttribuut(field=KwantWrdInJaar,
                                                naam='keuringsfrequentie',
                                                label='keuringsfrequentie',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buitenkast.keuringsfrequentie',
                                                definition='Frequentie (in jaar) waarmee de kast moet onderworpen worden aan een periodieke keuring door een externe dienst voor technische controle.')

        self._verfraaid = OTLAttribuut(field=KlBuitenkastVerfraaid,
                                       naam='verfraaid',
                                       label='verfraaid',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buitenkast.verfraaid',
                                       definition='Geeft aan of de wegkantkast voorzien van verfraaiing en of die al dan niet vergund is.')

    @property
    def ipKlasse(self):
        """De IP-codering als een aanduiding voor de mate van beveiliging van de constructie van elektrische of elektronische apparatuur tegen eigen schade door gebruik in "vijandige omgevingen" en tegen eventueel gevaar voor de gebruiker volgens IEC 60529."""
        return self._ipKlasse.waarde

    @ipKlasse.setter
    def ipKlasse(self, value):
        self._ipKlasse.set_waarde(value, owner=self)

    @property
    def keuringsfrequentie(self):
        """Frequentie (in jaar) waarmee de kast moet onderworpen worden aan een periodieke keuring door een externe dienst voor technische controle."""
        return self._keuringsfrequentie.waarde

    @keuringsfrequentie.setter
    def keuringsfrequentie(self, value):
        self._keuringsfrequentie.set_waarde(value, owner=self)

    @property
    def verfraaid(self):
        """Geeft aan of de wegkantkast voorzien van verfraaiing en of die al dan niet vergund is."""
        return self._verfraaid.waarde

    @verfraaid.setter
    def verfraaid(self, value):
        self._verfraaid.set_waarde(value, owner=self)
