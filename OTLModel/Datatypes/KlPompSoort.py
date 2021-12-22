from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlPompSoort(Keuzelijst):
    """Soorten pomp."""

    def __init__(self):
        super().__init__(naam="KlPompSoort",
                         label="Pomp soort",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPompSoort",
                         definition="Soorten pomp.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPompSoort")

        self.add_option("radiale-centrifugaalpomp-(dompel)", "radiale centrifugaalpomp (dompel)", "Radiale centrifugaalpomp (dompel)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPompSoort/radiale-centrifugaalpomp-(dompel)")
        self.add_option("radiale-centrifugaalpomp-(droog)", "radiale centrifugaalpomp (droog)", "Radiale centrifugaalpomp (droog)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPompSoort/radiale-centrifugaalpomp-(droog)")
        self.add_option("vijzelpomp", "vijzelpomp", "Vijzelpomp", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPompSoort/vijzelpomp")
        self.add_option("schachtpomp", "schachtpomp", "Schachtpomp", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPompSoort/schachtpomp")
        self.add_option("LPR-pomp-(luchtpersriolering)", "LPR-pomp (luchtpersriolering)", "LPR-pomp (luchtpersriolering)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPompSoort/LPR-pomp-(luchtpersriolering)")
        self.add_option("dompelpomp", "dompelpomp", "dompelpomp", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPompSoort/dompelpomp")
