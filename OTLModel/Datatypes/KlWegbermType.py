# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWegbermType(Keuzelijst):
    """Types van wegberm die de plaats ten opzichte van de weg aangeven."""

    def __init__(self):
        super().__init__(naam="KlWegbermType",
                         label="Wegberm type",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlWegbermType",
                         definition="Types van wegberm die de plaats ten opzichte van de weg aangeven.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWegbermType")

        self.add_option("buitenberm", "buitenberm", "Wegberm tussen de grens van het wegplatform en de buitengrens van de verharde zijstrook of van de rijbaan, als er geen verharde zijstrook is.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbermType/buitenberm")
        self.add_option("middenberm", "middenberm", "Wegberm tussen de middelste rijbanen van een weg met een even aantal rijbanen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbermType/middenberm")
        self.add_option("tussenberm", "tussenberm", "Wegberm tussen twee rijbanen van een weg met meer dan één rijbaan, de middenberm uitgezonderd.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbermType/tussenberm")
