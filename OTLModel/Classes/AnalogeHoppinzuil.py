# coding=utf-8
from OTLModel.Classes.Hoppinzuil import Hoppinzuil
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlHoppinzuilType import KlHoppinzuilType


# Generated with OTLClassCreator. To modify: extend, do not edit
class AnalogeHoppinzuil(Hoppinzuil):
    """Een hoppinzuil is een informatiezuil, die als doel heeft de reizigers te informeren omtrent de vervoersmogelijkheden en diensten die op de locatie van de zuil voorhanden zijn."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AnalogeHoppinzuil"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.macrokaart = DtcDocument()
        """Cartografische weergave van het hoppinpunt en de omliggende hoppinpunten met daarop aangeduid de attractiepolen in de omgeving."""
        self.macrokaart.naam = "macrokaart"
        self.macrokaart.label = "macrokaart"
        self.macrokaart.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AnalogeHoppinzuil.macrokaart"
        self.macrokaart.definition = "Cartografische weergave van het hoppinpunt en de omliggende hoppinpunten met daarop aangeduid de attractiepolen in de omgeving."
        self.macrokaart.constraints = ""
        self.macrokaart.usagenote = ""
        self.macrokaart.deprecated_version = ""

        self.microkaart = DtcDocument()
        """Cartografische weergave van het hoppinpunt en de omliggende straten met daarop de hoppinzuil, de verschillende beschikbare vervoersmodi en diensten aangeduid."""
        self.microkaart.naam = "microkaart"
        self.microkaart.label = "microkaart"
        self.microkaart.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AnalogeHoppinzuil.microkaart"
        self.microkaart.definition = "Cartografische weergave van het hoppinpunt en de omliggende straten met daarop de hoppinzuil, de verschillende beschikbare vervoersmodi en diensten aangeduid."
        self.microkaart.constraints = ""
        self.microkaart.usagenote = ""
        self.microkaart.deprecated_version = ""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlHoppinzuilType(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AnalogeHoppinzuil.type",
                                    definition="De mogelijke types van een analoge hoppinzuil.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De mogelijke types van een analoge hoppinzuil."""
