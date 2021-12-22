from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlTaludgootType(Keuzelijst):
    """Het type van taludgoot."""

    def __init__(self):
        super().__init__(naam="KlTaludgootType",
                         label="Taludgoot type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTaludgootType",
                         definition="Het type van taludgoot.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTaludgootType")

        self.add_option("taludgoot-type-A", "taludgoot type A", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTaludgootType/taludgoot-type-A")
        self.add_option("taludgoot-type-B", "taludgoot type B", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTaludgootType/taludgoot-type-B")
        self.add_option("Beginstuk-taludgoten-type-A-met-één-opening", "Beginstuk taludgoten type A met één opening", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTaludgootType/Beginstuk-taludgoten-type-A-met-één-opening")
        self.add_option("Beginstuk-taludgoten-type-A-met-twee-openingen", "Beginstuk taludgoten type A met twee openingen", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTaludgootType/Beginstuk-taludgoten-type-A-met-twee-openingen")
        self.add_option("Beginstuk-taludgoten-type-B-met-één-opening", "Beginstuk taludgoten type B met één opening", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTaludgootType/Beginstuk-taludgoten-type-B-met-één-opening")
        self.add_option("Beginstuk-taludgoten-type-B-met-twee-openingen", "Beginstuk taludgoten type B met twee openingen", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTaludgootType/Beginstuk-taludgoten-type-B-met-twee-openingen")
        self.add_option("Eindstuk-taludgoten-type-A", "Eindstuk taludgoten type A", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTaludgootType/Eindstuk-taludgoten-type-A")
        self.add_option("Eindstuk-taludgoten-type-B", "Eindstuk taludgoten type B", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTaludgootType/Eindstuk-taludgoten-type-B")
