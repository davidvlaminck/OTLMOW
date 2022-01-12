# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlConstructiestaalsoort(Keuzelijst):
    """De soort van het constructiestaal."""

    def __init__(self):
        super().__init__(naam="KlConstructiestaalsoort",
                         label="Constructiestaalsoort",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlConstructiestaalsoort",
                         definition="De soort van het constructiestaal.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlConstructiestaalsoort")

        self.add_option("s-235-j-0", "S235J0", "S staat voor Structural steel (constructiestaal), 235 voor de vloeigrens in MPa, J staat voor een kerfslagwaarde van 27 Joule en 0 voor 0 graden celsius.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-235-j-0")
        self.add_option("s-235-j-2-n", "S235J2+N", "S staat voor Structural steel (constructiestaal), 235 voor de vloeigrens in MPa, J staat voor een kerfslagwaarde van 27 Joule en 2 voor -20 graden celsius. De N duidt aan dat producten in genormaliseerde of equivalente toestand dienen geleverd te worden.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-235-j-2-n")
        self.add_option("s-235-jr", "S235JR", "S staat voor Structural steel (constructiestaal), 235 voor de vloeigrens in MPa, J staat voor een kerfslagwaarde van 27 Joule en R voor kampertemperatuur.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-235-jr")
        self.add_option("s-240-gp", "S240GP", "Warmgewalste staalsoort S 240 GP.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-240-gp")
        self.add_option("s-270-gp", "S270GP", "Warmgewalste staalsoort S 270 GP.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-270-gp")
        self.add_option("s-275-j-0", "S275J0", "S staat voor Structural steel (constructiestaal), 275 voor de vloeigrens in MPa, J staat voor een kerfslagwaarde van 27 Joule en 0 voor 0 graden celsius.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-275-j-0")
        self.add_option("s-275-j-2-n", "S275J2+N", "S staat voor Structural steel (constructiestaal), 275 voor de vloeigrens in MPa, J staat voor een kerfslagwaarde van 27 Joule en 2 voor -20 graden celsius. De N duidt aan dat producten in genormaliseerde of equivalente toestand dienen geleverd te worden.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-275-j-2-n")
        self.add_option("s-275-jr", "S275JR", "S staat voor Structural steel (constructiestaal), 275 voor de vloeigrens in MPa, J staat voor een kerfslagwaarde van 27 Joule en R voor kampertemperatuur.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-275-jr")
        self.add_option("s-320-gp", "S320GP", "Warmgewalste staalsoort S 320 GP.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-320-gp")
        self.add_option("s-355-gp", "S355GP", "Warmgewalste staalsoort S 355 GP.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-355-gp")
        self.add_option("s-355-j-0", "S355J0", "S staat voor Structural steel (constructiestaal), 355 voor de vloeigrens in MPa, J staat voor een kerfslagwaarde van 27 Joule en 0 voor 0 graden celsius.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-355-j-0")
        self.add_option("s-355-j-0-c", "S355J0C", "S staat voor Structural steel (constructiestaal), 355 voor de vloeigrens in MPa, J staat voor een kerfslagwaarde van 27 Joule en 0 voor 0 graden celsius. De C duidt aan het staal geschikt is voor specifieke aanwending zoals koudtrekken, profileren, koudflenzen (C van Cold forming) of dat het staal een hoog koolstofgehalte heeft (C van Carbon).", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-355-j-0-c")
        self.add_option("s-355-j-2-n", "S355J2+N", "S staat voor Structural steel (constructiestaal), 355 voor de vloeigrens in MPa, J staat voor een kerfslagwaarde van 27 Joule en 2 voor -20 graden celsius. De N duidt aan dat producten in genormaliseerde of equivalente toestand dienen geleverd te worden.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-355-j-2-n")
        self.add_option("s-355-jr", "S355JR", "S staat voor Structural steel (constructiestaal), 355 voor de vloeigrens in MPa, J staat voor een kerfslagwaarde van 27 Joule en R voor kampertemperatuur.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-355-jr")
        self.add_option("s-355-k-2-n", "S355K2+N", "S staat voor Structural steel (constructiestaal), 355 voor de vloeigrens in MPa, K staat voor een kerfslagwaarde van 40 Joule en 2 voor -20 graden celsius. De N duidt aan dat producten in genormaliseerde of equivalente toestand dienen geleverd te worden.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-355-k-2-n")
        self.add_option("s-390-gp", "S390GP", "Warmgewalste staalsoort S 390 GP.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-390-gp")
        self.add_option("s-430-gp", "S430GP", "Warmgewalste staalsoort S 430 GP.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-430-gp")
        self.add_option("s-460-m", "S460M", "S staat voor Structural steel (constructiestaal), 460 voor de vloeigrens in MPa en M staat voor thermo mechanisch gewalst staal (M van Mechanically).", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-460-m")
        self.add_option("s-460-ml", "S460ML", "S staat voor Structural steel (constructiestaal), 460 voor de vloeigrens in MPa en ML staat voor thermo mechanisch gewalst staal met min. gespecificeerde kerfslagwaarden onder -50° celsius.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-460-ml")
        self.add_option("s-460-n", "S460N", "S staat voor Structural steel (constructiestaal) en 460 voor de vloeigrens in MPa. De N duidt aan dat producten in genormaliseerde of equivalente toestand dienen geleverd te worden.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-460-n")
        self.add_option("s-460-nl", "S460NL", "S staat voor Structural steel (constructiestaal), 460 voor de vloeigrens in MPa en NL staat voor gegloeid en normaliserend gewalst staal met min. gespecificeerde kerfslagwaarden onder -50° celsius.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-460-nl")
