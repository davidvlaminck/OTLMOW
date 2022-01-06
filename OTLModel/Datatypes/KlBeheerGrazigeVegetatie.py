# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBeheerGrazigeVegetatie(Keuzelijst):
    """De verschillende soorten van beheer voor grazige vegetatie."""

    def __init__(self):
        super().__init__(naam="KlBeheerGrazigeVegetatie",
                         label="Beheer grazige vegetatie ",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlBeheerGrazigeVegetatie",
                         definition="De verschillende soorten van beheer voor grazige vegetatie.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBeheerGrazigeVegetatie")

        self.add_option("begrazing", "begrazing", "De vegetatie wordt begraasd door dieren.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/begrazing")
        self.add_option("niets-doen", "niets doen", "Er wordt geen beheer uitgevoerd", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/niets-doen")
        self.add_option("aflagen", "aflagen", "Het verwijderen van de bovenste grondlaag met begroeiing om afwatering te garanderen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/aflagen")
        self.add_option("plaggen", "plaggen", "Plaggen is het verwijderen van de bovenste grondlaag met begroeiing om grond te verschralen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/plaggen")
        self.add_option("afboorden", "afboorden", "Het afsteken van de overgroeiende vegetatie langs de rand van de verharding. (wordt afranden genoemd in SB250) ", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/afboorden")
        self.add_option("beluchten", "beluchten", "Beluchten van grazige vegetatie.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/beluchten")
        self.add_option("konijnenbeheer", "konijnenbeheer", "Het reduceren van konijnenpopulaties om de stabilietit van taluds te blijven garanderen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/konijnenbeheer")
        self.add_option("reiten", "reiten", "Het inkorten van het riet tot ongeveer 10 cm boven het wateroppervlak met maaikorf. Maaisel wordt verwijderd.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/reiten")
        self.add_option("uitharken", "uitharken", "Uitharken van grazige vegetatie.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/uitharken")
        self.add_option("bestrijden-ongewenste-vegetatie", "bestrijden ongewenste vegetatie", "Bestrijden van ongewenste vegetatie die zich bevingt in het perceel van grazige vegetatie..", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/bestrijden-ongewenste-vegetatie")
        self.add_option("maaisel-verwijderen-hooien-oprapen", "maaisel verwijderen hooien-oprapen", "het maaisel wordt gehooid en binnen de 10 dagen opgeraapt en verwijderd", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/maaisel-verwijderen-hooien-oprapen")
        self.add_option("profielherstelling-zonder-herinzaaien", "profielherstelling zonder herinzaaien", "Profielherstelling zonder herinzaaiing van grazige vegetatie.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/profielherstelling-zonder-herinzaaien")
        self.add_option("maaisel-verwijderen-directe-opzuig", "maaisel verwijderen directe opzuig", "het verwijderen van het maaisel met een maaizuigcombinatie", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/maaisel-verwijderen-directe-opzuig")
