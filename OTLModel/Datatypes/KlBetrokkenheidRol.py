# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBetrokkenheidRol(Keuzelijst):
    """Keuzelijst met mogelijke waarden voor de rol waarmee een agent betrokken is bij een object."""

    def __init__(self):
        super().__init__(naam="KlBetrokkenheidRol",
                         label="Betrokkenheid rol",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBetrokkenheidRol",
                         definition="Keuzelijst met mogelijke waarden voor de rol waarmee een agent betrokken is bij een object.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBetrokkenheidRol")

        self.add_option("lid", "lid", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/lid")
        self.add_option("verantwoordelijke-reiniging", "verantwoordelijke reiniging", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/verantwoordelijke-reiniging")
        self.add_option("installatieverantwoordelijke", "Installatieverantwoordelijke", "De installatieverantwoordelijke is de persoon, aangeduid door de werkgever, om de verantwoordelijkheid voor de exploitatie van de elektrische installatie op zich te nemen. Indien nodig kan hij die verantwoordelijkheid wel gedeeltelijk op andere personen overdragen. Concreet is hij op de hoogte van de eventuele afwijkende situaties en gaat, in overleg met de werkverantwoordelijke, na of de nodige maatregelen genomen worden om op een veilige manier te werken met een dergelijke installatie.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/installatieverantwoordelijke")
        self.add_option("beheerder", "beheerder", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/beheerder")
        self.add_option("toezichter", "toezichter", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/toezichter")
        self.add_option("toezichtsgroep", "toezichtsgroep", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/toezichtsgroep")
        self.add_option("klant", "klant", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/klant")
        self.add_option("berekende-beheerder", "berekende beheerder", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/berekende-beheerder")
        self.add_option("keuringsinstantie", "keuringsinstantie", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/keuringsinstantie")
        self.add_option("eigenaar", "eigenaar", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/eigenaar")
        self.add_option("toezicht-onderhoud", "toezicht onderhoud", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/toezicht-onderhoud")
        self.add_option("schadebeheerder", "schadebeheerder", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/schadebeheerder")
        self.add_option("leidinggevende", "leidinggevende", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/leidinggevende")
        self.add_option("suborganisatie-van", "suborganisatie van", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/suborganisatie-van")
