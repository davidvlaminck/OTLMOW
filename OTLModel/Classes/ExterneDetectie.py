from OTLModel.Classes.Detectie import Detectie
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcNatuurlijkPersoon import DtcNatuurlijkPersoon
from OTLModel.Datatypes.DtcRechtspersoon import DtcRechtspersoon
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlExternedetectieAangeslotentoestel import KlExternedetectieAangeslotentoestel
from OTLModel.Datatypes.KlExternedetectieCommunicatiewijze import KlExternedetectieCommunicatiewijze


# Generated with OTLClassCreator. To modify: extend, do not edit
class ExterneDetectie(Detectie):
    """Inputsignalen bv. van een brug of een overweg, die door een externe partij doorgegeven worden teneinde de verkeersregelaar aan te sturen. 
Dit object wordt niet gebruikt voor eigen lussen van een ander kruispunt."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ExterneDetectie"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.aangeslotenToestel = KeuzelijstField(naam="aangeslotenToestel",
                                                  label="aangesloten toestel",
                                                  lijst=KlExternedetectieAangeslotentoestel(),
                                                  uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ExterneDetectie.aangeslotenToestel",
                                                  definition="Type aangesloten toestel (trein, brug, FCD).",
                                                  constraints="",
                                                  usagenote="",
                                                  deprecated_version="")
        """Type aangesloten toestel (trein, brug, FCD)."""

        self.communicatiewijze = KeuzelijstField(naam="communicatiewijze",
                                                 label="communicatiewijze",
                                                 lijst=KlExternedetectieCommunicatiewijze(),
                                                 uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ExterneDetectie.communicatiewijze",
                                                 definition="De manier waarop de externe detectie communiceert met de verkeersregelaar.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        """De manier waarop de externe detectie communiceert met de verkeersregelaar."""

        self.contactpersoon = DtcNatuurlijkPersoon()
        """Naam, voornaam en telefoonnummer van de contactpersoon."""
        self.contactpersoon.naam = "contactpersoon"
        self.contactpersoon.label = "contactpersoon"
        self.contactpersoon.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ExterneDetectie.contactpersoon"
        self.contactpersoon.definition = "Naam, voornaam en telefoonnummer van de contactpersoon."
        self.contactpersoon.constraints = ""
        self.contactpersoon.usagenote = ""
        self.contactpersoon.deprecated_version = ""

        self.eigenaar = DtcRechtspersoon()
        """Eigenaar van het aangesloten toestel/systeem."""
        self.eigenaar.naam = "eigenaar"
        self.eigenaar.label = "eigenaar"
        self.eigenaar.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ExterneDetectie.eigenaar"
        self.eigenaar.definition = "Eigenaar van het aangesloten toestel/systeem."
        self.eigenaar.constraints = ""
        self.eigenaar.usagenote = ""
        self.eigenaar.deprecated_version = ""

        self.heeftHandshaking = BooleanField(naam="heeftHandshaking",
                                             label="heeft handshaking",
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ExterneDetectie.heeftHandshaking",
                                             definition="Bij handshaking wordt gebruikt gemaakt van 2 contacten (maak / verbreek) om zeker te zijn dat het een valide signaal betreft (en geen kabelbreuk of gelijkwaardig).",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Bij handshaking wordt gebruikt gemaakt van 2 contacten (maak / verbreek) om zeker te zijn dat het een valide signaal betreft (en geen kabelbreuk of gelijkwaardig)."""
