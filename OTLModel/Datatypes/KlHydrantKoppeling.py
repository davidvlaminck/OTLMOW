# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHydrantKoppeling(Keuzelijst):
    """Keuzelijst met types koppelingen van hydranten."""

    def __init__(self):
        super().__init__(naam="KlHydrantKoppeling",
                         label="Hydrant koppeling",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHydrantKoppeling",
                         definition="Keuzelijst met types koppelingen van hydranten.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHydrantKoppeling")

