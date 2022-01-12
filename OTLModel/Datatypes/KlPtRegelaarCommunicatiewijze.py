# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPtRegelaarCommunicatiewijze(Keuzelijst):
    """Keuzelijst met de verschillende manieren waarop een PT_Regelaar communiceert met de Verkeersregelaar."""

    def __init__(self):
        super().__init__(naam="KlPtRegelaarCommunicatiewijze",
                         label="Ptregelaar communicatiewijze",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPtRegelaarCommunicatiewijze",
                         definition="Keuzelijst met de verschillende manieren waarop een PT_Regelaar communiceert met de Verkeersregelaar.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPtRegelaarCommunicatiewijze")

        self.add_option("VR-PT-kaart", "VR PT-kaart", "De PT kaart is een module die is ingebouwd in de verkeersregelaar", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPtRegelaarCommunicatiewijze/VR-PT-kaart")
        self.add_option("contact", "contact", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPtRegelaarCommunicatiewijze/contact")
        self.add_option("protocol", "protocol", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPtRegelaarCommunicatiewijze/protocol")
        self.add_option("serieel", "serieel", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPtRegelaarCommunicatiewijze/serieel")
