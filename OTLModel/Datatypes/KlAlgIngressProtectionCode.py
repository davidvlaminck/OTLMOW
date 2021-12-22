from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlAlgIngressProtectionCode(Keuzelijst):
    """De IP-codering als een aanduiding voor de mate van beveiliging van de constructie van elektrische of elektronische apparatuur tegen eigen schade door gebruik in 'vijandige omgevingen' en tegen eventueel gevaar voor de gebruiker volgens IEC 60529."""

    def __init__(self):
        super().__init__(naam="KlAlgIngressProtectionCode",
                         label="Ingress Protection Codering",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAlgIngressProtectionCode",
                         definition="De IP-codering als een aanduiding voor de mate van beveiliging van de constructie van elektrische of elektronische apparatuur tegen eigen schade door gebruik in 'vijandige omgevingen' en tegen eventueel gevaar voor de gebruiker volgens IEC 60529.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgIngressProtectionCode")

        self.add_option("i-p-44", "IP44", "Bescherming tegen spitse voorwerpen en plensdicht.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgIngressProtectionCode/i-p-44")
        self.add_option("i-p-65", "IP65", "Stofvrij en sproeidicht.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgIngressProtectionCode/i-p-65")
