from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlDekselKaderType(Keuzelijst):
    """Types van dekselkader."""

    def __init__(self):
        super().__init__(naam="KlDekselKaderType",
                         label="Dekselkader type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDekselKaderType",
                         definition="Types van dekselkader.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDekselKaderType")

        self.add_option("type-1", "type 1", "type 1", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKaderType/type-1")
        self.add_option("type-2", "type 2", "type 2", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKaderType/type-2")
        self.add_option("type-3", "type 3", "type 3", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKaderType/type-3")
        self.add_option("type-4", "type 4", "type 4", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKaderType/type-4")
        self.add_option("type-5", "type 5", "type 5", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKaderType/type-5")
        self.add_option("type-6", "type 6", "type 6", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKaderType/type-6")
        self.add_option("type-7", "type 7", "type 7", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKaderType/type-7")
        self.add_option("type-8", "type 8", "type 8", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKaderType/type-8")
        self.add_option("type-9", "type 9", "type 9", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKaderType/type-9")
        self.add_option("enkelvoudig-gietijzeren-controleluik", "enkelvoudig gietijzeren controleluik", "enkelvoudig gietijzeren controleluik", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKaderType/enkelvoudig-gietijzeren-controleluik")
        self.add_option("meerdelige-gietijzeren-controleluik", "meerdelige gietijzeren controleluik", "meerdelige gietijzeren controleluik", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKaderType/meerdelige-gietijzeren-controleluik")
