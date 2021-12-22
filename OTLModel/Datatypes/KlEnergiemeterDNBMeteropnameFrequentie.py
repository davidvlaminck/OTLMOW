from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlEnergiemeterDNBMeteropnameFrequentie(Keuzelijst):
    """Frequentie waarmee de meterstand opgenomen wordt door de netbeheerder."""

    def __init__(self):
        super().__init__(naam="KlEnergiemeterDNBMeteropnameFrequentie",
                         label="Energiemeter DNB meteropname frequentie",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlEnergiemeterDNBMeteropnameFrequentie",
                         definition="Frequentie waarmee de meterstand opgenomen wordt door de netbeheerder.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEnergiemeterDNBMeteropnameFrequentie")

        self.add_option("AMR", "AMR", "automatische meter reading", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEnergiemeterDNBMeteropnameFrequentie/AMR")
        self.add_option("MMR", "MMR", "manuele meter opname", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEnergiemeterDNBMeteropnameFrequentie/MMR")
        self.add_option("YMR", "YMR", "jaarlijkse meter opname", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEnergiemeterDNBMeteropnameFrequentie/YMR")
