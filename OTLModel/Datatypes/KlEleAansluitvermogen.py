# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEleAansluitvermogen(Keuzelijst):
    """Keuzelijst met gangbare waarden voor elektrisch aansluitvermogen."""

    def __init__(self):
        super().__init__(naam="KlEleAansluitvermogen",
                         label="Elektrisch aansluitvermogen",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlEleAansluitvermogen",
                         definition="Keuzelijst met gangbare waarden voor elektrisch aansluitvermogen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEleAansluitvermogen")

        self.add_option("20A-230Veenfasig-4.6kVA", "20A 230Veenfasig-4.6kVA", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEleAansluitvermogen/20A-230Veenfasig-4.6kVA")
        self.add_option("40A-230Veenfasig-9.2kVA", "40A 230Veenfasig-9.2kVA", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEleAansluitvermogen/40A-230Veenfasig-9.2kVA")
        self.add_option("16A-230Vdriefasig-6.4kVA", "16A 230Vdriefasig-6.4kVA", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEleAansluitvermogen/16A-230Vdriefasig-6.4kVA")
        self.add_option("32A-230Vdriefasig-12.7kVA", "32A 230Vdriefasig-12.7kVA", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEleAansluitvermogen/32A-230Vdriefasig-12.7kVA")
        self.add_option("63A-230Vdriefasig-25.1kVA", "63A 230Vdriefasig-25.1kVA", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEleAansluitvermogen/63A-230Vdriefasig-25.1kVA")
        self.add_option("25A-400Vdriefasig-17.3kVA", "25A 400Vdriefasig-17.3kVA", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEleAansluitvermogen/25A-400Vdriefasig-17.3kVA")
        self.add_option("50A-400Vdriefasig-34.6kVA", "50A 400Vdriefasig-34.6kVA", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEleAansluitvermogen/50A-400Vdriefasig-34.6kVA")
        self.add_option("16A-230Veenfasig-3.7kVA", "16A 230Veenfasig-3.7kVA", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEleAansluitvermogen/16A-230Veenfasig-3.7kVA")
        self.add_option("32A-230Veenfasig-7.4kVA", "32A 230Veenfasig-7.4kVA", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEleAansluitvermogen/32A-230Veenfasig-7.4kVA")
        self.add_option("63A-230Veenfasig-14.5kVA", "63A 230Veenfasig-14.5kVA", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEleAansluitvermogen/63A-230Veenfasig-14.5kVA")
        self.add_option("25A-230Vdriefasig-10kVA", "25A 230Vdriefasig-10kVA", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEleAansluitvermogen/25A-230Vdriefasig-10kVA")
        self.add_option("50A-230Vdriefasig-19.9kVA", "50A 230Vdriefasig-19.9kVA", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEleAansluitvermogen/50A-230Vdriefasig-19.9kVA")
        self.add_option("20A-400Vdriefasig-13.9kVA", "20A 400Vdriefasig-13.9kVA", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEleAansluitvermogen/20A-400Vdriefasig-13.9kVA")
        self.add_option("40A-400Vdriefasig-27.7kVA", "40A 400Vdriefasig-27.7kVA", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEleAansluitvermogen/40A-400Vdriefasig-27.7kVA")
        self.add_option("25A-230Veenfasig-5.8kVA", "25A 230Veenfasig-5.8kVA", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEleAansluitvermogen/25A-230Veenfasig-5.8kVA")
        self.add_option("50A-230Veenfasig-11.5kVA", "50A 230Veenfasig-11.5kVA", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEleAansluitvermogen/50A-230Veenfasig-11.5kVA")
        self.add_option("20A-230Vdriefasig-8kVA", "20A 230Vdriefasig-8kVA", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEleAansluitvermogen/20A-230Vdriefasig-8kVA")
        self.add_option("40A-230Vdriefasig-15.9kVA", "40A 230Vdriefasig-15.9kVA", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEleAansluitvermogen/40A-230Vdriefasig-15.9kVA")
        self.add_option("16A-400Vdriefasig-11.1kVA", "16A 400Vdriefasig-11.1kVA", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEleAansluitvermogen/16A-400Vdriefasig-11.1kVA")
        self.add_option("32A-400Vdriefasig-22.2kVA", "32A 400Vdriefasig-22.2kVA", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEleAansluitvermogen/32A-400Vdriefasig-22.2kVA")
        self.add_option("63A-400Vdriefasig-43.6kVA", "63A 400Vdriefasig-43.6kVA", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEleAansluitvermogen/63A-400Vdriefasig-43.6kVA")
