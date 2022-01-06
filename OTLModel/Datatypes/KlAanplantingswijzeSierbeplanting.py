# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAanplantingswijzeSierbeplanting(Keuzelijst):
    """De mogelijke manieren van aanplanten van sierbeplanting."""

    def __init__(self):
        super().__init__(naam="KlAanplantingswijzeSierbeplanting",
                         label="aanplantingswijze sierbeplanting",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAanplantingswijzeSierbeplanting",
                         definition="De mogelijke manieren van aanplanten van sierbeplanting.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAanplantingswijzeSierbeplanting")

        self.add_option("aanplanting-helm", "aanplanting helm", "Aanplanting via helm", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAanplantingswijzeSierbeplanting/aanplanting-helm")
        self.add_option("aanplanting-zonder-helm", "aanplanting zonder helm", "Aanplanting zonder helm", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAanplantingswijzeSierbeplanting/aanplanting-zonder-helm")
        self.add_option("aanplanting-bol--en-knolgewassen", "aanplanting bol- en knolgewassen", "Aanplanting via bol- en knolgewassen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAanplantingswijzeSierbeplanting/aanplanting-bol--en-knolgewassen")
