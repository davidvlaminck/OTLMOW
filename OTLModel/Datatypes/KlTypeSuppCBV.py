# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeSuppCBV(Keuzelijst):
    """Keuzelijst om het type van de toegevoegde supplementen van de CBV te bepalen."""

    def __init__(self):
        super().__init__(naam="KlTypeSuppCBV",
                         label="Type supplementen CBV",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeSuppCBV",
                         definition="Keuzelijst om het type van de toegevoegde supplementen van de CBV te bepalen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeSuppCBV")

        self.add_option("figureren-betonoppervlak-in-de-massa-gekleurd", "figureren betonoppervlak in de massa gekleurd", "Supplementen voor het bekomen van een in de massa gekleurde CBV.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeSuppCBV/figureren-betonoppervlak-in-de-massa-gekleurd")
        self.add_option("figureren-betonoppervlak-met-kleurverharder", "figureren betonoppervlak met kleurverharder", "Supplementen voor het bekomen van een gekleurde 2 laagse deklaag van CBV.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeSuppCBV/figureren-betonoppervlak-met-kleurverharder")
