from OTLModel.Classes.NaampadObject import NaampadObject
from OTLModel.Datatypes.IntegerField import IntegerField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlZpadType import KlZpadType
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Zpad(NaampadObject):
    """End-to-end gebruikersverbinding over het transport netwerk."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Zpad"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.netwerkklant = StringField(naam="netwerkklant",
                                        label="netwerkklant",
                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Zpad.netwerkklant",
                                        definition="Naam van de organisatie van de gebruiker.",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """Naam van de organisatie van de gebruiker."""

        self.omschrijving = StringField(naam="omschrijving",
                                        label="omschrijving",
                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Zpad.omschrijving",
                                        definition="Beschrijving van de aard en/of doel van de verbinding.",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """Beschrijving van de aard en/of doel van de verbinding."""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlZpadType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Zpad.type",
                                    definition="De soort verbinding, gebaseerd op het gebruikte protocol.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De soort verbinding, gebaseerd op het gebruikte protocol."""

        self.WANCapaciteit = IntegerField(naam="WANCapaciteit",
                                          label="wan capaciteit",
                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Zpad.WANCapaciteit",
                                          definition="Capaciteit van de verbinding vanuit het standpunt van de gebruiker.",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        """Capaciteit van de verbinding vanuit het standpunt van de gebruiker."""
