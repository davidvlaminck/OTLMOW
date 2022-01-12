# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDraagConstrBijzondertransport(Keuzelijst):
    """De mogelijkheden en manieren waarop een steun geschikt is om bijzonder transport mogelijk te maken."""

    def __init__(self):
        super().__init__(naam="KlDraagConstrBijzondertransport",
                         label="Draagconstructie bijzonder transport",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlDraagConstrBijzondertransport",
                         definition="De mogelijkheden en manieren waarop een steun geschikt is om bijzonder transport mogelijk te maken.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDraagConstrBijzondertransport")

        self.add_option("afkoppelbaar", "afkoppelbaar", "Het object is afkoppelbaar.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagConstrBijzondertransport/afkoppelbaar")
        self.add_option("draaibaar", "draaibaar", "Het object is draaibaar.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagConstrBijzondertransport/draaibaar")
        self.add_option("geen-voorziening", "geen voorziening", "Geen voorziening.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagConstrBijzondertransport/geen-voorziening")
        self.add_option("kantelbaar", "kantelbaar", "Het object is kantelbaar.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagConstrBijzondertransport/kantelbaar")
