# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMozaiekkeiFormaat(Keuzelijst):
    """Formaten van de mozaïekkei."""

    def __init__(self):
        super().__init__(naam="KlMozaiekkeiFormaat",
                         label="Mozaiekkei formaat",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMozaiekkeiFormaat",
                         definition="Formaten van de mozaïekkei.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMozaiekkeiFormaat")

        self.add_option("bestratingen-van-mozaïekkeien-van-het-1ste-formaat", "bestratingen van mozaïekkeien van het 1ste formaat", "Bestratingen van mozaïekkeien van het 1ste formaat", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMozaiekkeiFormaat/bestratingen-van-mozaïekkeien-van-het-1ste-formaat")
        self.add_option("bestratingen-van-mozaïekkeien-van-het-2de-formaat", "bestratingen van mozaïekkeien van het 2de formaat", "Bestratingen van mozaïekkeien van het 2de formaat", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMozaiekkeiFormaat/bestratingen-van-mozaïekkeien-van-het-2de-formaat")
        self.add_option("bestratingen-van-mozaïekkeien-van-het-3de-formaat", "bestratingen van mozaïekkeien van het 3de formaat", "Bestratingen van mozaïekkeien van het 3de formaat", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMozaiekkeiFormaat/bestratingen-van-mozaïekkeien-van-het-3de-formaat")
        self.add_option("bestratingen-van-mozaïekkeien-van-het-4de-formaat", "bestratingen van mozaïekkeien van het 4de formaat", "Bestratingen van mozaïekkeien van het 4de formaat", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMozaiekkeiFormaat/bestratingen-van-mozaïekkeien-van-het-4de-formaat")
        self.add_option("bestratingen-van-mozaïekkeien-van-het-5de-formaat", "bestratingen van mozaïekkeien van het 5de formaat", "Bestratingen van mozaïekkeien van het 5de formaat", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMozaiekkeiFormaat/bestratingen-van-mozaïekkeien-van-het-5de-formaat")
