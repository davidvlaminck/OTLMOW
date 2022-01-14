from UnitTests.OTLFieldTests.KeuzelijstField import KeuzelijstField


class KlRioleringsbuisMateriaal(KeuzelijstField):
    """Keuzelijst met fasen uit de levenscyclus van een object om de toestand op een moment mee vast te leggen."""

    def __init__(self):
        super().__init__(naam="KlRioleringsbuisMateriaal",
                         label="Rioleringsbuis materiaal",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRioleringsbuisMateriaal",
                         definition="Materialen van de rioleringbuis.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRioleringsbuisMateriaal")

        self.add_option("PP-buizen", "PP-buizen", "PP-buizen",
                        "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisMateriaal/PP-buizen")
        self.add_option("PVC-U-composietleidingen", "PVC-U-composietleidingen", "PVC-U-composietleidingen",
                        "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisMateriaal/PVC-U-composietleidingen")
        self.add_option("PVC-buizen", "PVC-buizen", "PVC-buizen",
                        "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisMateriaal/PVC-buizen")
        self.add_option("afvoerbuizen-van-polyethyleen", "afvoerbuizen van polyethyleen", "buizen vervaardigd uit polyethyleen",
                        "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisMateriaal/afvoerbuizen-van-polyethyleen")
        self.add_option("betonbuizen-met-plaatstalen-kern", "betonbuizen met plaatstalen kern",
                        "Betonbuizen met plaatstalen kern",
                        "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisMateriaal/betonbuizen-met-plaatstalen-kern")
        self.add_option("buizen-van-gevuld-en-glasvezelversterkt-polyesterhars-(UP-GF)",
                        "buizen van gevuld en glasvezelversterkt polyesterhars (UP-GF)",
                        "Buizen van gevuld en glasvezelversterkt polyesterhars (UP-GF)",
                        "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisMateriaal/buizen-van-gevuld-en-glasvezelversterkt-polyesterhars-(UP-GF)")
        self.add_option("buizen-van-hoogwaardig-beton", "buizen van hoogwaardig beton", "Buizen van hoogwaardig beton",
                        "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisMateriaal/buizen-van-hoogwaardig-beton")
        self.add_option("buizen-van-nodulair-gietijzer-zonder-inwendige-druk",
                        "buizen van nodulair gietijzer zonder inwendige druk",
                        "Buizen van nodulair gietijzer zonder inwendige druk",
                        "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisMateriaal/buizen-van-nodulair-gietijzer-zonder-inwendige-druk")
        self.add_option("buizen-van-poreus-beton-volgens-3-24.6", "buizen van poreus beton volgens 3-24.6",
                        "Buizen van poreus beton volgens 3-24.6",
                        "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisMateriaal/buizen-van-poreus-beton-volgens-3-24.6")
        self.add_option("doorpersbuizen-van-beton-met-plaatstalen-kern-en-dubbel-voegsysteem",
                        "doorpersbuizen van beton met plaatstalen kern en dubbel voegsysteem",
                        "Doorpersbuizen van beton met plaatstalen kern en dubbel voegsysteem",
                        "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisMateriaal/doorpersbuizen-van-beton-met-plaatstalen-kern-en-dubbel-voegsysteem")
        self.add_option("doorpersbuizen-van-gevuld-en-glasvezelversterkt-polyesterhars",
                        "doorpersbuizen van gevuld en glasvezelversterkt polyesterhars",
                        "Doorpersbuizen van gevuld en glasvezelversterkt polyesterhars",
                        "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisMateriaal/doorpersbuizen-van-gevuld-en-glasvezelversterkt-polyesterhars")
        self.add_option("doorpersbuizen-van-gewapend-beton-voorzien-van-een-harde-PVC-bekleding",
                        "doorpersbuizen van gewapend beton voorzien van een harde PVC-bekleding",
                        "Doorpersbuizen van polymeerbeton",
                        "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisMateriaal/doorpersbuizen-van-gewapend-beton-voorzien-van-een-harde-PVC-bekleding")
        self.add_option("doorpersbuizen-van-gewapend-beton.-sterktereeks-135",
                        "doorpersbuizen van gewapend beton. sterktereeks 135",
                        "Doorpersbuizen van gewapend beton, sterktereeks 135",
                        "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisMateriaal/doorpersbuizen-van-gewapend-beton.-sterktereeks-135")
        self.add_option("doorpersbuizen-van-gres", "doorpersbuizen van gres", "Doorpersbuizen van gres",
                        "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisMateriaal/doorpersbuizen-van-gres")
        self.add_option("gewapend-betonbuizen", "gewapend-betonbuizen", "Gewapend-betonbuizen",
                        "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisMateriaal/gewapend-betonbuizen")
        self.add_option("gresbuizen", "gresbuizen",
                        "gresbuis is een (riool)buis gemaakt van vette klei en chamotte met een gladde en zeer harde afwerking.",
                        "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisMateriaal/gresbuizen")
        self.add_option("met-staalvezels-versterkte-betonbuizen", "met staalvezels versterkte betonbuizen",
                        "Met staalvezels versterkte betonbuizen",
                        "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisMateriaal/met-staalvezels-versterkte-betonbuizen")
        self.add_option("ongewapende-betonbuizen", "ongewapende betonbuizen", "Ongewapende betonbuizen",
                        "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisMateriaal/ongewapende-betonbuizen")
        self.add_option("voorgespannen-gewapende-betonbuizen", "voorgespannen gewapende betonbuizen",
                        "Voorgespannen gewapende betonbuizen",
                        "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisMateriaal/voorgespannen-gewapende-betonbuizen")
        self.add_option("wandversterkte-HDPE-buizen", "wandversterkte HDPE-buizen", "Wandversterkte HDPE-buizen",
                        "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisMateriaal/wandversterkte-HDPE-buizen")
