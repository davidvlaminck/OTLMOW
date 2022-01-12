# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHoogtedetectieMerk(Keuzelijst):
    """Keuzelijst met de gangbare merken van hoogtedetectiesystemen. De merken verwijzen doorgaans naar de fabrikant of leverancier."""

    def __init__(self):
        super().__init__(naam="KlHoogtedetectieMerk",
                         label="Hoogtedetectie merk",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHoogtedetectieMerk",
                         definition="Keuzelijst met de gangbare merken van hoogtedetectiesystemen. De merken verwijzen doorgaans naar de fabrikant of leverancier.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHoogtedetectieMerk")

