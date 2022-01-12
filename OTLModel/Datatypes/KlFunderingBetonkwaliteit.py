# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlFunderingBetonkwaliteit(Keuzelijst):
    """Mogelijke waarden voor de betonkwaliteit van een fundering."""

    def __init__(self):
        super().__init__(naam="KlFunderingBetonkwaliteit",
                         label="Fundering betonkwaliteit",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFunderingBetonkwaliteit",
                         definition="Mogelijke waarden voor de betonkwaliteit van een fundering.",
                         usagenote="Klasse uit gebruik sinds versie 2.0.0",
                         deprecated_version="2.0.0",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFunderingBetonkwaliteit")

