from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlTsklepAfsluiterMateriaal(Keuzelijst):
    """Materialen van de terugslagklep."""

    def __init__(self):
        super().__init__(naam="KlTsklepAfsluiterMateriaal",
                         label="Terugslagklep afsluiter materiaal",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTsklepAfsluiterMateriaal",
                         definition="Materialen van de terugslagklep.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTsklepAfsluiterMateriaal")

        self.add_option("am---Gietijzer", "am - Gietijzer", "Een gietijzeren terugslagklep.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTsklepAfsluiterMateriaal/am---Gietijzer")
        self.add_option("av---Hdpe", "av - Hdpe", "Een terugslagklep uit HDPE.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTsklepAfsluiterMateriaal/av---Hdpe")
        self.add_option("ap---Staal", "ap - Staal", "Een stalen terugslagklep.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTsklepAfsluiterMateriaal/ap---Staal")
        self.add_option("z---Anders", "z - Anders", "Een terugslagklep uit een ander materiaal.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTsklepAfsluiterMateriaal/z---Anders")
