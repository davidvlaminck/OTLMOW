# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSierbeplantingType(Keuzelijst):
    """Verschillende types van sierbeplanting."""

    def __init__(self):
        super().__init__(naam="KlSierbeplantingType",
                         label="Sierbeplanting type",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSierbeplantingType",
                         definition="Verschillende types van sierbeplanting.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSierbeplantingType")

        self.add_option("bodembedekkers", "bodembedekkers", "Aangelegd begroeiingstype, doorgaans met vaste planten, die bedoeld is om snel de bodem af te dekken.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplantingType/bodembedekkers")
        self.add_option("bol-en-knolgewassen", "bol- en knolgewassen", "Bol- en knolgewassen beschikken over boven- of ondergrondse delen waarin voedsel voor ‘barre’ tijden kan worden opgeslagen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplantingType/bol-en-knolgewassen")
        self.add_option("siergrassen", "siergrassen", "Grasachtige planten, doorgaans vaste planten, met een decoratieve waarde. Niet geplant als gazon", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplantingType/siergrassen")
        self.add_option("vaste-planten", "vaste planten", "Begroeiingstype met planten die een kruidachtige stengel hebben en overblijvend zijn. Dus niet de eenjarige en tweejarige kruidachtige soorten.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplantingType/vaste-planten")
