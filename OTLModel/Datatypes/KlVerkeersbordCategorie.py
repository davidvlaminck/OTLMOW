# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeersbordCategorie(Keuzelijst):
    """Klassen van een verkeersbord."""

    def __init__(self):
        super().__init__(naam="KlVerkeersbordCategorie",
                         label="Verkeersbord categorie",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersbordCategorie",
                         definition="Klassen van een verkeersbord.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersbordCategorie")

        self.add_option("aanwijzingsborden", "aanwijzingsborden", "aanwijzingsborden", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordCategorie/aanwijzingsborden")
        self.add_option("gebodsborden", "gebodsborden", "gebodsborden", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordCategorie/gebodsborden")
        self.add_option("gevaarsborden", "gevaarsborden", "gevaarsborden", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordCategorie/gevaarsborden")
        self.add_option("voorrangsborden", "voorrangsborden", "voorrangsborden", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordCategorie/voorrangsborden")
