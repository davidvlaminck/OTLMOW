# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeerslichtMasker(Keuzelijst):
    """Keuzelijst met de gangbare types masker die op een verkeerslicht zijn aangebracht."""

    def __init__(self):
        super().__init__(naam="KlVerkeerslichtMasker",
                         label="Verkeerslicht masker",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVerkeerslichtMasker",
                         definition="Keuzelijst met de gangbare types masker die op een verkeerslicht zijn aangebracht.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeerslichtMasker")

        self.add_option("voetganger", "voetganger", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/voetganger")
        self.add_option("pijl-links", "pijl links", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/pijl-links")
        self.add_option("fietser", "fietser", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/fietser")
        self.add_option("kleine-cirkel", "kleine cirkel", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/kleine-cirkel")
        self.add_option("pijl-rechtdoor-links", "pijl rechtdoor links", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/pijl-rechtdoor-links")
        self.add_option("driehoek", "driehoek", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/driehoek")
        self.add_option("vierkant-groen", "vierkant groen", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/vierkant-groen")
        self.add_option("schuine-balk--45°", "schuine balk -45°", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/schuine-balk--45°")
        self.add_option("volle-lens", "volle lens", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/volle-lens")
        self.add_option("niet-gekend", "niet gekend", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/niet-gekend")
        self.add_option("schuine-balk-+45°", "schuine balk +45°", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/schuine-balk-+45°")
        self.add_option("kruis", "kruis", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/kruis")
        self.add_option("pijl-rechts", "pijl rechts", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/pijl-rechts")
        self.add_option("pijl-rechtdoor-rechts", "pijl rechtdoor rechts", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/pijl-rechtdoor-rechts")
        self.add_option("verticale-balk", "verticale balk", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/verticale-balk")
        self.add_option("horizontale-balk", "horizontale balk", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/horizontale-balk")
        self.add_option("pijl-rechtdoor", "pijl rechtdoor", "Pijl rechtdoor", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/pijl-rechtdoor")
