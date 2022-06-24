# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.Abstracten.Energiemeter import Energiemeter
from OTLMOW.OTLModel.Datatypes.KlEnergiemeterDNBMeteropnameFrequentie import KlEnergiemeterDNBMeteropnameFrequentie


# Generated with OTLClassCreator. To modify: extend, do not edit
class DNBMeter(Energiemeter):
    """Abstracte voor elk toestel dat eigendom is van de distributienetbeheerder en in de installatie van de asset beheerder geplaatst wordt voor diverse metingen van doorgevoerde energie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNBMeter'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._meteropnameFrequentie = OTLAttribuut(field=KlEnergiemeterDNBMeteropnameFrequentie,
                                                   naam='meteropnameFrequentie',
                                                   label='meteropname frequentie',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNBMeter.meteropnameFrequentie',
                                                   definition='Frequentie waarmee de meterstand opgenomen wordt door de netbeheerder.',
                                                   owner=self)

    @property
    def meteropnameFrequentie(self):
        """Frequentie waarmee de meterstand opgenomen wordt door de netbeheerder."""
        return self._meteropnameFrequentie.get_waarde()

    @meteropnameFrequentie.setter
    def meteropnameFrequentie(self, value):
        self._meteropnameFrequentie.set_waarde(value, owner=self)
