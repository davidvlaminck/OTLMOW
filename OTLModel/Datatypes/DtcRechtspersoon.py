from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.DtcAdres import DtcAdres
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLComplexDatatypeCreator
class DtcRechtspersoon(ComplexField):
    """Complex datatype voor een rechtspersoon."""

    def __init__(self):
        super().__init__(naam="DtcRechtspersoon",
                         label="Rechtspersoon",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcRechtspersoon",
                         definition="Complex datatype voor een rechtspersoon.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.adres = DtcAdres()
        """Het adres."""
        self.waarde.adres.naam = "adres"
        self.waarde.adres.label = "adres"
        self.waarde.adres.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcRechtspersoon.adres"
        self.waarde.adres.definition = "Het adres."
        self.waarde.adres.constraints = ""
        self.waarde.adres.usagenote = ""
        self.waarde.adres.deprecated_version = ""
        self.adres = self.waarde.adres

        self.waarde.afdeling = StringField(naam="afdeling",
                                           label="afdeling",
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcRechtspersoon.afdeling",
                                           definition="De afdeling waartoe een rechtspersoon behoort.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        self.afdeling = self.waarde.afdeling
        """De afdeling waartoe een rechtspersoon behoort."""

        self.waarde.organisatie = StringField(naam="organisatie",
                                              label="organisatie",
                                              uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcRechtspersoon.organisatie",
                                              definition="De naam van de organisatie of rechtspersoon.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        self.organisatie = self.waarde.organisatie
        """De naam van de organisatie of rechtspersoon."""

        self.waarde.telefoonnnummer = StringField(naam="telefoonnnummer",
                                                  label="telefoonnnummer",
                                                  uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcRechtspersoon.telefoonnnummer",
                                                  definition="Het telefoonnummer.",
                                                  constraints="",
                                                  usagenote="",
                                                  deprecated_version="")
        self.telefoonnnummer = self.waarde.telefoonnnummer
        """Het telefoonnummer."""
