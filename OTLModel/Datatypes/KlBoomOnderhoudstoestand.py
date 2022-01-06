# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBoomOnderhoudstoestand(Keuzelijst):
    """De verschillende mogelijke onderhoudstoestanden."""

    def __init__(self):
        super().__init__(naam="KlBoomOnderhoudstoestand",
                         label="Boom onderhoudstoestand",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoomOnderhoudstoestand",
                         definition="De verschillende mogelijke onderhoudstoestanden.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoomOnderhoudstoestand")

        self.add_option("op-beeld", "op beeld", "De boom heeft een tijdige en goede begeleidings- of onderhoudssnoei en ziet er uit zoals hij er hoort uit te zien.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomOnderhoudstoestand/op-beeld")
        self.add_option("niet-op-beeld-achterstallig", "niet op beeld-achterstallig", "De boom heeft 1 snoeibeurt nodig om op beeld te komen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomOnderhoudstoestand/niet-op-beeld-achterstallig")
        self.add_option("niet-op-beeld-verwaarloosd", "niet op beeld-verwaarloosd", "De boom heeft 2 of meer snoeibeurten nodig om op beeld te komen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomOnderhoudstoestand/niet-op-beeld-verwaarloosd")
        self.add_option("niet-op-beeld-problematisch", "niet op beeld-problematisch", "De boom is niet meer in een gewenste onderhoudstoestand te brengen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomOnderhoudstoestand/niet-op-beeld-problematisch")
