from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlWegbebakeningType(Keuzelijst):
    """De vormen van wegbebakening."""

    def __init__(self):
        super().__init__(naam="KlWegbebakeningType",
                         label="Wegbebakening type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWegbebakeningType",
                         definition="De vormen van wegbebakening.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWegbebakeningType")

        self.add_option("type-1-(new-jersey-reclip)", "type 1 (new jersey reclip)", "type 1 (new jersey reclip)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbebakeningType/type-1-(new-jersey-reclip)")
        self.add_option("type-2-(new-jersey)", "type 2 (new jersey)", "type 2 (new jersey)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbebakeningType/type-2-(new-jersey)")
        self.add_option("type-A-(vangrail-reclip)", "type A (vangrail reclip)", "type A (vangrail reclip)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbebakeningType/type-A-(vangrail-reclip)")
        self.add_option("type-C-(vangrail-trapezium)", "type C (vangrail trapezium)", "Type C (vangrail trapezium)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbebakeningType/type-C-(vangrail-trapezium)")
        self.add_option("type-B-(vangrail)", "type B (vangrail)", "type B (vangrail)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbebakeningType/type-B-(vangrail)")
        self.add_option("type-3-(referentiepaal)", "type 3 (referentiepaal)", "type 3 (referentiepaal)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbebakeningType/type-3-(referentiepaal)")
