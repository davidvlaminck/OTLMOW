# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Brandvoorziening import Brandvoorziening
from OTLMOW.OTLModel.Datatypes.KwantWrdInBar import KwantWrdInBar
from OTLMOW.OTLModel.Datatypes.KwantWrdInKiloWatt import KwantWrdInKiloWatt


# Generated with OTLClassCreator. To modify: extend, do not edit
class Drukverhogingsgroep(Brandvoorziening):
    """Onderdeel dat de druk van het aangevoerde water regelt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Drukverhogingsgroep'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._inkomendeDruk = OTLAttribuut(field=KwantWrdInBar,
                                           naam='inkomendeDruk',
                                           label='inkomende druk',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Drukverhogingsgroep.inkomendeDruk',
                                           definition='Verwachte inkomende druk van het water bij de groep.',
                                           owner=self)

        self._uitgaandeDruk = OTLAttribuut(field=KwantWrdInBar,
                                           naam='uitgaandeDruk',
                                           label='uitgaande druk',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Drukverhogingsgroep.uitgaandeDruk',
                                           definition='Verwachte uitgaande druk van het water na regeling door de groep.',
                                           owner=self)

        self._vermogen = OTLAttribuut(field=KwantWrdInKiloWatt,
                                      naam='vermogen',
                                      label='vermogen',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Drukverhogingsgroep.vermogen',
                                      definition='Elektrische vermogen vereist voor de goede werking van de groep.',
                                      owner=self)

    @property
    def inkomendeDruk(self):
        """Verwachte inkomende druk van het water bij de groep."""
        return self._inkomendeDruk.waarde

    @inkomendeDruk.setter
    def inkomendeDruk(self, value):
        self._inkomendeDruk.set_waarde(value, owner=self)

    @property
    def uitgaandeDruk(self):
        """Verwachte uitgaande druk van het water na regeling door de groep."""
        return self._uitgaandeDruk.waarde

    @uitgaandeDruk.setter
    def uitgaandeDruk(self, value):
        self._uitgaandeDruk.set_waarde(value, owner=self)

    @property
    def vermogen(self):
        """Elektrische vermogen vereist voor de goede werking van de groep."""
        return self._vermogen.waarde

    @vermogen.setter
    def vermogen(self, value):
        self._vermogen.set_waarde(value, owner=self)
