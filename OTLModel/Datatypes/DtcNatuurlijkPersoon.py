from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.DtcAdres import DtcAdres
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLComplexDatatypeCreator
class DtcNatuurlijkPersoon(ComplexField):
    """Complex datatype dat een natuurlijk persoon beschrijft."""

    def __init__(self):
        super().__init__(naam="DtcNatuurlijkPersoon",
                         label="Natuurlijk persoon",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcNatuurlijkPersoon",
                         definition="Complex datatype dat een natuurlijk persoon beschrijft.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.achternaam = StringField(naam="achternaam",
                                             label="achternaam",
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcNatuurlijkPersoon.achternaam",
                                             definition="De achternaam.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        self.achternaam = self.waarde.achternaam
        """De achternaam."""

        adresField = DtcAdres()
        adresField.naam = "adres"
        adresField.label = "adres"
        adresField.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcNatuurlijkPersoon.adres"
        adresField.definition = "Het adres."
        adresField.constraints = ""
        adresField.usagenote = ""
        adresField.deprecated_version = ""
        self.waarde.adres = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=adresField)
        self.adres = self.waarde.adres
        """Het adres."""

        emailadresField = StringField(naam="emailadres",
                                      label="emailadres",
                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcNatuurlijkPersoon.emailadres",
                                      definition="Het emailadres.",
                                      constraints="",
                                      usagenote="",
                                      deprecated_version="")
        self.waarde.emailadres = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=emailadresField)
        self.emailadres = self.waarde.emailadres
        """Het emailadres."""

        faxField = StringField(naam="fax",
                               label="fax",
                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcNatuurlijkPersoon.fax",
                               definition="De faxnummer.",
                               constraints="",
                               usagenote="",
                               deprecated_version="")
        self.waarde.fax = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=faxField)
        self.fax = self.waarde.fax
        """De faxnummer."""

        self.waarde.heeftEmailVoorkeur = BooleanField(naam="heeftEmailVoorkeur",
                                                      label="heeft email voorkeur",
                                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcNatuurlijkPersoon.heeftEmailVoorkeur",
                                                      definition="Aanduiding of een persoon de voorkeur heeft om via email gecontacteerd te worden.",
                                                      constraints="",
                                                      usagenote="",
                                                      deprecated_version="")
        self.heeftEmailVoorkeur = self.waarde.heeftEmailVoorkeur
        """Aanduiding of een persoon de voorkeur heeft om via email gecontacteerd te worden."""

        self.waarde.heeftFaxVoorkeur = BooleanField(naam="heeftFaxVoorkeur",
                                                    label="heeft fax voorkeur",
                                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcNatuurlijkPersoon.heeftFaxVoorkeur",
                                                    definition="Aanduiding of een persoon een voorkeur heeft om via fax gegevens te ontvangen.",
                                                    constraints="",
                                                    usagenote="",
                                                    deprecated_version="")
        self.heeftFaxVoorkeur = self.waarde.heeftFaxVoorkeur
        """Aanduiding of een persoon een voorkeur heeft om via fax gegevens te ontvangen."""

        telefoonnnummerField = StringField(naam="telefoonnnummer",
                                           label="telefoonnnummer",
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcNatuurlijkPersoon.telefoonnnummer",
                                           definition="Het telefoonnummer.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        self.waarde.telefoonnnummer = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=telefoonnnummerField)
        self.telefoonnnummer = self.waarde.telefoonnnummer
        """Het telefoonnummer."""

        self.waarde.voornaam = StringField(naam="voornaam",
                                           label="voornaam",
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcNatuurlijkPersoon.voornaam",
                                           definition="De voornaam.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        self.voornaam = self.waarde.voornaam
        """De voornaam."""
