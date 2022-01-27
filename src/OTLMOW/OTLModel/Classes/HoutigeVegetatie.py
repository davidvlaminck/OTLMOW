# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.BegroeidVoorkomen import BegroeidVoorkomen
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcHoutigeAanleg import DtcHoutigeAanleg
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class HoutigeVegetatie(BegroeidVoorkomen):
    """Houtige planten of houtige gewassen (planta lignosa) zijn overblijvende planten die worden gekenmerkt door secundaire diktegroei, waardoor de takken, stammen en wortels veel hout bevatten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HoutigeVegetatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._aanleg = OTLAttribuut(field=DtcHoutigeAanleg,
                                    naam='aanleg',
                                    label='aanleg',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HoutigeVegetatie.aanleg',
                                    kardinaliteit_max='*',
                                    definition='De manier van aanplanten van de houtige vegetatie.')

        self._hoogte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HoutigeVegetatie.hoogte',
                                    definition='De hoogte in meter gemeten van de stamvoet tot de top of bovenste snoeivlak van de houtige vegetatie. ')

        self._isVrijUitgroeiend = OTLAttribuut(field=BooleanField,
                                               naam='isVrijUitgroeiend',
                                               label='is vrij uitgroeiend',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HoutigeVegetatie.isVrijUitgroeiend',
                                               definition='Geeft aan of de vegetatie of begroeiing al dan niet snoei vereist.')

        self._knipoppervlak = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                           naam='knipoppervlak',
                                           label='knipoppervlak',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HoutigeVegetatie.knipoppervlak',
                                           definition='De afmeting van de begroeiing in vierkante meter dat geschoren moet worden.')

    @property
    def aanleg(self):
        """De manier van aanplanten van de houtige vegetatie."""
        return self._aanleg.waarde

    @aanleg.setter
    def aanleg(self, value):
        self._aanleg.set_waarde(value, owner=self)

    @property
    def hoogte(self):
        """De hoogte in meter gemeten van de stamvoet tot de top of bovenste snoeivlak van de houtige vegetatie. """
        return self._hoogte.waarde

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self)

    @property
    def isVrijUitgroeiend(self):
        """Geeft aan of de vegetatie of begroeiing al dan niet snoei vereist."""
        return self._isVrijUitgroeiend.waarde

    @isVrijUitgroeiend.setter
    def isVrijUitgroeiend(self, value):
        self._isVrijUitgroeiend.set_waarde(value, owner=self)

    @property
    def knipoppervlak(self):
        """De afmeting van de begroeiing in vierkante meter dat geschoren moet worden."""
        return self._knipoppervlak.waarde

    @knipoppervlak.setter
    def knipoppervlak(self, value):
        self._knipoppervlak.set_waarde(value, owner=self)
