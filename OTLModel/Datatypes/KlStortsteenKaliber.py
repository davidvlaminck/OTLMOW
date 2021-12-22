from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlStortsteenKaliber(Keuzelijst):
    """Mogelijke kalibers van stortsteen."""

    def __init__(self):
        super().__init__(naam="KlStortsteenKaliber",
                         label="Stortsteen kaliber",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlStortsteenKaliber",
                         definition="Mogelijke kalibers van stortsteen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlStortsteenKaliber")

        self.add_option("kleiner-dan-0.063-mm", "kleiner dan 0.063 mm", "< 0,063 mm", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/kleiner-dan-0.063-mm")
        self.add_option("groter-dan-125-mm", "groter dan 125 mm", "> 125 mm", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/groter-dan-125-mm")
        self.add_option("CP-90-180A", "CP 90/180A", "< 0,063 mm", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/CP-90-180A")
        self.add_option("CP-90-250", "CP 90/250", "< 0,063 mm", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/CP-90-250")
        self.add_option("LMA-5-40", "LMA 5/40", "< 0,063 mm", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/LMA-5-40")
        self.add_option("LMA-10-60", "LMA 10/60", "< 0,063 mm", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/LMA-10-60")
        self.add_option("LMA-40-200", "LMA 40/200", "LMA 40/200", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/LMA-40-200")
        self.add_option("LMA-60-300", "LMA 60/300", "LMA 60/300", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/LMA-60-300")
        self.add_option("LMA-15-300", "LMA 15/300", "LMA 15/300", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/LMA-15-300")
        self.add_option("LMA-300-1000", "LMA 300/1000", "LMA 300/1000", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/LMA-300-1000")
        self.add_option("HMA-3000-6000", "HMA 3000/6000", "HMA 3000/6000", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/HMA-3000-6000")
        self.add_option("HMA-6000-10000", "HMA 6000/10000", "HMA 6000/10000", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/HMA-6000-10000")
        self.add_option("HMA10000-15000", "HMA10000/15000", "HMA10000/15000", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/HMA10000-15000")
        self.add_option("HMA1000-3000", "HMA1000/3000", "HMA1000/3000", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/HMA1000-3000")
        self.add_option("korrelmaal-14-20", "korrelmaal 14/20", "korrelmaal 14/20", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/korrelmaal-14-20")
        self.add_option("korrelmaat-20-31.5", "korrelmaat 20/31.5", "korrelmaat 20/31.5", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/korrelmaat-20-31.5")
        self.add_option("korrelmaat-31.5-63", "korrelmaat 31.5/63", "korrelmaat 31.5/63", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/korrelmaat-31.5-63")
