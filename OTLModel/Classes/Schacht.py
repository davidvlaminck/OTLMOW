# coding=utf-8
from OTLModel.Classes.PutRelatie import PutRelatie
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlPutMateriaal import KlPutMateriaal
from OTLModel.Datatypes.KlRioleringVorm import KlRioleringVorm
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Schacht(PutRelatie):
    """Gedeelte van de put tussen regeling en de kamer."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schacht"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.breedte = KwantWrdInMillimeter()
        """De afmeting 1 (breedte) van het grondplan van de schacht in millimeter."""
        self.breedte.naam = "breedte"
        self.breedte.label = "breedte"
        self.breedte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schacht.breedte"
        self.breedte.definition = "De afmeting 1 (breedte) van het grondplan van de schacht in millimeter."
        self.breedte.constraints = ""
        self.breedte.usagenote = ""
        self.breedte.deprecated_version = ""

        self.diepte = KwantWrdInMeter()
        """De diepte vanaf het maaiveld tot onderkant van de afdekplaat in meter."""
        self.diepte.naam = "diepte"
        self.diepte.label = "diepte"
        self.diepte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schacht.diepte"
        self.diepte.definition = "De diepte vanaf het maaiveld tot onderkant van de afdekplaat in meter."
        self.diepte.constraints = ""
        self.diepte.usagenote = ""
        self.diepte.deprecated_version = ""

        self.heeftLadder = BooleanField(naam="heeftLadder",
                                        label="heeft ladder",
                                        objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schacht.heeftLadder",
                                        definition="Bepaling of er al dan niet een ladder aanwezig is in de schacht.",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """Bepaling of er al dan niet een ladder aanwezig is in de schacht."""

        self.hoogte = KwantWrdInMillimeter()
        """De afmeting 2 (hoogte) van het grondplan van de schacht in millimeter."""
        self.hoogte.naam = "hoogte"
        self.hoogte.label = "hoogte"
        self.hoogte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schacht.hoogte"
        self.hoogte.definition = "De afmeting 2 (hoogte) van het grondplan van de schacht in millimeter."
        self.hoogte.constraints = ""
        self.hoogte.usagenote = ""
        self.hoogte.deprecated_version = ""

        self.materiaal = KeuzelijstField(naam="materiaal",
                                         label="materiaal",
                                         lijst=KlPutMateriaal(),
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schacht.materiaal",
                                         definition="Het materiaal waaruit de schacht opgebouwd is.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Het materiaal waaruit de schacht opgebouwd is."""

        technischeFicheField = DtcDocument()
        technischeFicheField.naam = "technischeFiche"
        technischeFicheField.label = "technische fiche"
        technischeFicheField.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schacht.technischeFiche"
        technischeFicheField.definition = "De technische fiche van de schacht."
        technischeFicheField.constraints = ""
        technischeFicheField.usagenote = "Bestanden van het type xlsx, dwg of pdf."
        technischeFicheField.deprecated_version = ""
        self.technischeFiche = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=technischeFicheField)
        """De technische fiche van de schacht."""

        self.vorm = KeuzelijstField(naam="vorm",
                                    label="vorm",
                                    lijst=KlRioleringVorm(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schacht.vorm",
                                    definition="Vorm van het schachtgedeelte van de kamer.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Vorm van het schachtgedeelte van de kamer."""
