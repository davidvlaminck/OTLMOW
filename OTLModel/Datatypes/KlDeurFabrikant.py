# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDeurFabrikant(Keuzelijst):
    """Lijst van fabrikanten van deuren."""

    def __init__(self):
        super().__init__(naam="KlDeurFabrikant",
                         label="Deur fabrikant",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlDeurFabrikant",
                         definition="Lijst van fabrikanten van deuren.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDeurFabrikant")

