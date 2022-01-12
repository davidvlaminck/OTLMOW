# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNatuursteentegelGebruiksklasse(Keuzelijst):
    """Mogelijke waarden voor de gebruiksklasse, vorm en afwerking van de natuursteentegel."""

    def __init__(self):
        super().__init__(naam="KlNatuursteentegelGebruiksklasse",
                         label="Natuursteentegel gebruiksklasse",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNatuursteentegelGebruiksklasse",
                         definition="Mogelijke waarden voor de gebruiksklasse, vorm en afwerking van de natuursteentegel.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNatuursteentegelGebruiksklasse")

        self.add_option("0", "0", "Keuzeoptie decoratie als gebruiksklasse van natuursteentegels.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNatuursteentegelGebruiksklasse/0")
        self.add_option("1", "1", "Keuzeoptie voetgangerszones als gebruiksklasse van natuursteentegels.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNatuursteentegelGebruiksklasse/1")
        self.add_option("2", "2", "Keuzeoptie voetgangers- en fietszones als gebruiksklasse van natuursteentegels.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNatuursteentegelGebruiksklasse/2")
        self.add_option("3", "3", "Keuzeoptie voetgangerszones, occasioneel belast door wagens en lichte voertuigen, inritten van garages als gebruiksklasse van natuursteentegels.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNatuursteentegelGebruiksklasse/3")
        self.add_option("4", "4", "Keuzeoptie voetgangerszones en marktplaatsen, occasioneel belast voor leveringen en door hulpdiensten als gebruiksklasse van natuursteentegels.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNatuursteentegelGebruiksklasse/4")
        self.add_option("5", "5", "Keuzeoptie voetgangerszones, regelmatig belast door zwaar verkeer als gebruiksklasse van natuursteentegels.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNatuursteentegelGebruiksklasse/5")
        self.add_option("6", "6", "Keuzeoptie wegen als gebruiksklasse van natuursteentegels.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNatuursteentegelGebruiksklasse/6")
