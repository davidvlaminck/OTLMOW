# coding=utf-8
from abc import abstractmethod
from OTLModel.Classes.Energiemeter import Energiemeter
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlEnergiemeterDNBMeteropnameFrequentie import KlEnergiemeterDNBMeteropnameFrequentie


# Generated with OTLClassCreator. To modify: extend, do not edit
class DNBMeter(Energiemeter):
    """Abstracte voor elk toestel dat eigendom is van de distributienetbeheerder en in de installatie van de asset beheerder geplaatst wordt voor diverse metingen van doorgevoerde energie."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNBMeter"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.meteropnameFrequentie = KeuzelijstField(naam="meteropnameFrequentie",
                                                     label="meteropname frequentie",
                                                     lijst=KlEnergiemeterDNBMeteropnameFrequentie(),
                                                     uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNBMeter.meteropnameFrequentie",
                                                     definition="Frequentie waarmee de meterstand opgenomen wordt door de netbeheerder.",
                                                     constraints="",
                                                     usagenote="",
                                                     deprecated_version="")
        """Frequentie waarmee de meterstand opgenomen wordt door de netbeheerder."""
