# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.MeteropnameEnergiemeter import MeteropnameEnergiemeter
from OTLModel.Datatypes.KwantWrdInKiloWatt import KwantWrdInKiloWatt
from OTLModel.Datatypes.KwantWrdInkVARh import KwantWrdInkVARh


# Generated with OTLClassCreator. To modify: extend, do not edit
class MeteropnameEnergiemeterGecombineerd(MeteropnameEnergiemeter, AttributeInfo):
    """Resultaten van een meteropname van een gecombineerde energiemeter."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#MeteropnameEnergiemeterGecombineerd'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        MeteropnameEnergiemeter.__init__(self)

        self._meterstandPiek = OTLAttribuut(field=KwantWrdInKiloWatt,
                                            naam='meterstandPiek',
                                            label='meterstand piek',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#MeteropnameEnergiemeterGecombineerd.meterstandPiek',
                                            definition='De stand van de energiemeter waarmee het piekvermogen gemeten wordt.')

        self._meterstandReactiefVermogenDag = OTLAttribuut(field=KwantWrdInkVARh,
                                                           naam='meterstandReactiefVermogenDag',
                                                           label='dag-meterstand reactief vermogen',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#MeteropnameEnergiemeterGecombineerd.meterstandReactiefVermogenDag',
                                                           definition='De stand van de dag-energiemeter waarmee het reactief vermogen gemeten wordt.')

        self._meterstandReactiefVermogenNacht = OTLAttribuut(field=KwantWrdInkVARh,
                                                             naam='meterstandReactiefVermogenNacht',
                                                             label='nacht-meterstand reactief vermogen',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#MeteropnameEnergiemeterGecombineerd.meterstandReactiefVermogenNacht',
                                                             definition='De stand van de nacht-energiemeter waarmee het reactief vermogen gemeten wordt.')

    @property
    def meterstandPiek(self):
        """De stand van de energiemeter waarmee het piekvermogen gemeten wordt."""
        return self._meterstandPiek.waarde

    @meterstandPiek.setter
    def meterstandPiek(self, value):
        self._meterstandPiek.set_waarde(value, owner=self)

    @property
    def meterstandReactiefVermogenDag(self):
        """De stand van de dag-energiemeter waarmee het reactief vermogen gemeten wordt."""
        return self._meterstandReactiefVermogenDag.waarde

    @meterstandReactiefVermogenDag.setter
    def meterstandReactiefVermogenDag(self, value):
        self._meterstandReactiefVermogenDag.set_waarde(value, owner=self)

    @property
    def meterstandReactiefVermogenNacht(self):
        """De stand van de nacht-energiemeter waarmee het reactief vermogen gemeten wordt."""
        return self._meterstandReactiefVermogenNacht.waarde

    @meterstandReactiefVermogenNacht.setter
    def meterstandReactiefVermogenNacht(self, value):
        self._meterstandReactiefVermogenNacht.set_waarde(value, owner=self)
