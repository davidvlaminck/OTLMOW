# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLuidsprekerMerk(Keuzelijst):
    """Het merk van de luidspreker."""

    def __init__(self):
        super().__init__(naam="KlLuidsprekerMerk",
                         label="Luidspreker merk",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLuidsprekerMerk",
                         definition="Het merk van de luidspreker.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLuidsprekerMerk")

