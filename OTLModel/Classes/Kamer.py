# coding=utf-8
from OTLModel.Classes.PutRelatie import PutRelatie
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlKamerKlasse import KlKamerKlasse
from OTLModel.Datatypes.KlPutMateriaal import KlPutMateriaal
from OTLModel.Datatypes.KlRioleringVorm import KlRioleringVorm
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kamer(PutRelatie):
    """Een kamer is een aanééngesloten ondergrondse constructie waarbinnen vrije stroming van water over de
 bodem mogelijk is. Een constructie of inspectieput kan één of meerdere kamers hebben."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.breedte = KwantWrdInMillimeter()
        """De afmeting 1 (breedte) van het grondplan van de putkamer in millimeter."""
        self.breedte.naam = "breedte"
        self.breedte.label = "breedte"
        self.breedte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer.breedte"
        self.breedte.definition = "De afmeting 1 (breedte) van het grondplan van de putkamer in millimeter."
        self.breedte.constraints = ""
        self.breedte.usagenote = ""
        self.breedte.deprecated_version = ""

        self.diepte = KwantWrdInMeter()
        """De diepte van de putkamer in meter."""
        self.diepte.naam = "diepte"
        self.diepte.label = "diepte"
        self.diepte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer.diepte"
        self.diepte.definition = "De diepte van de putkamer in meter."
        self.diepte.constraints = ""
        self.diepte.usagenote = ""
        self.diepte.deprecated_version = ""

        self.hoogte = KwantWrdInMillimeter()
        """De afmeting 2 (hoogte) van het grondplan van de putkamer in millimeter."""
        self.hoogte.naam = "hoogte"
        self.hoogte.label = "hoogte"
        self.hoogte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer.hoogte"
        self.hoogte.definition = "De afmeting 2 (hoogte) van het grondplan van de putkamer in millimeter."
        self.hoogte.constraints = ""
        self.hoogte.usagenote = ""
        self.hoogte.deprecated_version = ""

        self.klasse = KeuzelijstField(naam="klasse",
                                      label="klasse",
                                      lijst=KlKamerKlasse(),
                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer.klasse",
                                      definition="De stabiliteitsklasse van de kamer.",
                                      constraints="",
                                      usagenote="",
                                      deprecated_version="")
        """De stabiliteitsklasse van de kamer."""

        self.materiaal = KeuzelijstField(naam="materiaal",
                                         label="materiaal",
                                         lijst=KlPutMateriaal(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer.materiaal",
                                         definition="Het materiaal waaruit de kamer opgebouwd is.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Het materiaal waaruit de kamer opgebouwd is."""

        technischeFicheField = DtcDocument()
        technischeFicheField.naam = "technischeFiche"
        technischeFicheField.label = "technische fiche"
        technischeFicheField.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer.technischeFiche"
        technischeFicheField.definition = "De technische fiche van de kamer."
        technischeFicheField.constraints = ""
        technischeFicheField.usagenote = "Bestanden van het type xlsx, dwg of pdf."
        technischeFicheField.deprecated_version = ""
        self.technischeFiche = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=technischeFicheField)
        """De technische fiche van de kamer."""

        self.vorm = KeuzelijstField(naam="vorm",
                                    label="vorm",
                                    lijst=KlRioleringVorm(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer.vorm",
                                    definition="De vorm van de kamer.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De vorm van de kamer."""
