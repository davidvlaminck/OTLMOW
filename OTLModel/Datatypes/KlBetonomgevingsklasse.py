# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBetonomgevingsklasse(Keuzelijst):
    """Omgevingsklasse waaraan het beton wordt blootgesteld."""

    def __init__(self):
        super().__init__(naam="KlBetonomgevingsklasse",
                         label="Betonomgevingsklasse",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlBetonomgevingsklasse",
                         definition="Omgevingsklasse waaraan het beton wordt blootgesteld.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBetonomgevingsklasse")

        self.add_option("e-s-4", "ES4", "Zeeomgeving : contact met zeewater en getijden- en spatzone.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-s-4")
        self.add_option("e-s-2", "ES2", "Zeeomgeving : geen contact met zeewater, wel contact met zeelucht (tot 3 km van de kust) en/of brak water, en wel contact met vorst.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-s-2")
        self.add_option("e-a-2", "EA2", "Middelmatig agressieve chemische omgeving volgens tabel 2 van NBN EN 206-1:2001.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-a-2")
        self.add_option("e-e-2", "EE2", "Buitenomgeving : vorst, geen contact met regen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-e-2")
        self.add_option("e-a-3", "EA3", "Sterk agressieve chemische omgeving volgens tabel 2 van NBN EN 206-1:2001.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-a-3")
        self.add_option("ei", "EI", "Binnenomgeving.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/ei")
        self.add_option("e-s-1", "ES1", "Zeeomgeving : geen contact met zeewater, wel contact met zeelucht (tot 3 km van de kust) en/of brak water, en geen contact met vorst.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-s-1")
        self.add_option("e-e-3", "EE3", "Buitenomgeving : vorst, contact met regen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-e-3")
        self.add_option("e-0", "E0", "Niet schadelijk.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-0")
        self.add_option("e-e-1", "EE1", "Buitenomgeving : geen vorst.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-e-1")
        self.add_option("e-a-1", "EA1", "Zwak agressieve chemische omgeving volgens tabel 2 van NBN EN 206-1:2001.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-a-1")
        self.add_option("e-e-4", "EE4", "Buitenomgeving : vorst en dooizouten (aanwezigheid van ter plaatse ontdooid of opspattend of aflopend dooizouthoudend water).", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-e-4")
        self.add_option("e-s-3", "ES3", "Zeeomgeving : contact met zeewater en ondergedompeld.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-s-3")
