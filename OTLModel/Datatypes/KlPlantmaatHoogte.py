from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlPlantmaatHoogte(Keuzelijst):
    """Keuzelijst die de hoogte in centimeter gemeten van de stamvoet tot de top met een minimum en maximum waarde oplijst."""

    def __init__(self):
        super().__init__(naam="KlPlantmaatHoogte",
                         label="Plantmaat houtige vegetatie",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPlantmaatHoogte",
                         definition="Keuzelijst die de hoogte in centimeter gemeten van de stamvoet tot de top met een minimum en maximum waarde oplijst.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPlantmaatHoogte")

        self.add_option("40-60", "40-60", "40/60", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatHoogte/40-60")
        self.add_option("60-80", "60-80", "60/80", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatHoogte/60-80")
        self.add_option("80-100", "80-100", "80/100", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatHoogte/80-100")
        self.add_option("100-125", "100-125", "100/125", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatHoogte/100-125")
        self.add_option("125-150", "125-150", "125/150", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatHoogte/125-150")
        self.add_option("150-175", "150-175", "150/175", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatHoogte/150-175")
        self.add_option("175-200", "175-200", "175/200", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatHoogte/175-200")
        self.add_option("200-250", "200-250", "200/250", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatHoogte/200-250")
        self.add_option("350-400", "350-400", "350/400", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatHoogte/350-400")
        self.add_option("250-300", "250-300", "250/300", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatHoogte/250-300")
        self.add_option("300-350", "300-350", "300/350", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatHoogte/300-350")
