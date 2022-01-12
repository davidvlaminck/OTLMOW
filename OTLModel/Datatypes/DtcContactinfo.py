# coding=utf-8
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.DtcAdres import DtcAdres
from OTLModel.Datatypes.DtcOpeningsurenSpecificatie import DtcOpeningsurenSpecificatie
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcContactinfo(ComplexField):
    """Complex datatype voor de informatie zoals email, telefoon, adres die toelaat om iemand of iets te contacteren."""

    def __init__(self):
        super().__init__(naam="DtcContactinfo",
                         label="Contactinfo",
                         objectUri="https://schema.org/ContactPoint",
                         definition="Complex datatype voor de informatie zoals email, telefoon, adres die toelaat om iemand of iets te contacteren.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.adres = DtcAdres()
        """Adres dat men kan aanschrijven of bezoeken."""
        self.waarde.adres.naam = "adres"
        self.waarde.adres.label = "adres"
        self.waarde.adres.objectUri = "https://schema.org/ContactPoint.adres"
        self.waarde.adres.definition = "Adres dat men kan aanschrijven of bezoeken."
        self.waarde.adres.constraints = ""
        self.waarde.adres.usagenote = ""
        self.waarde.adres.deprecated_version = ""
        self.adres = self.waarde.adres

        beschikbaarheidField = DtcOpeningsurenSpecificatie()
        beschikbaarheidField.naam = "beschikbaarheid"
        beschikbaarheidField.label = "beschikbaarheid"
        beschikbaarheidField.objectUri = "https://schema.org/ContactPoint.beschikbaarheid"
        beschikbaarheidField.definition = "Periode waarin contact kan worden opgenomen."
        beschikbaarheidField.constraints = ""
        beschikbaarheidField.usagenote = ""
        beschikbaarheidField.deprecated_version = ""
        self.waarde.beschikbaarheid = KardinaliteitField(minKardinaliteit="0", maxKardinaliteit="*", fieldToMultiply=beschikbaarheidField)
        self.beschikbaarheid = self.waarde.beschikbaarheid
        """Periode waarin contact kan worden opgenomen."""

        self.waarde.contactnaam = StringField(naam="contactnaam",
                                              label="contactnaam",
                                              objectUri="https://schema.org/ContactPoint.contactnaam",
                                              definition="Naam van bv. de persoon die men kan contacteren.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        self.contactnaam = self.waarde.contactnaam
        """Naam van bv. de persoon die men kan contacteren."""

        self.waarde.email = StringField(naam="email",
                                        label="email",
                                        objectUri="https://schema.org/ContactPoint.email",
                                        definition="Email-adres waarnaar men kan mailen.",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        self.email = self.waarde.email
        """Email-adres waarnaar men kan mailen."""

        self.waarde.fax = StringField(naam="fax",
                                      label="fax",
                                      objectUri="https://schema.org/ContactPoint.fax",
                                      definition="Faxnummer waarnaar men kan faxen.",
                                      constraints="",
                                      usagenote="",
                                      deprecated_version="")
        self.fax = self.waarde.fax
        """Faxnummer waarnaar men kan faxen."""

        self.waarde.opmerkingen = StringField(naam="opmerkingen",
                                              label="opmerkingen",
                                              objectUri="https://schema.org/ContactPoint.opmerkingen",
                                              definition="Bijkomende informatie met betrekking tot het gebruik van de contactgegevens.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        self.opmerkingen = self.waarde.opmerkingen
        """Bijkomende informatie met betrekking tot het gebruik van de contactgegevens."""

        self.waarde.telefoon = StringField(naam="telefoon",
                                           label="telefoon",
                                           objectUri="https://schema.org/ContactPoint.telefoon",
                                           definition="Telefoonnummer waarop men kan bellen.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        self.telefoon = self.waarde.telefoon
        """Telefoonnummer waarop men kan bellen."""

        self.waarde.website = StringField(naam="website",
                                          label="website",
                                          objectUri="https://schema.org/ContactPoint.website",
                                          definition="Website waarnaar men kan surfen.",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        self.website = self.waarde.website
        """Website waarnaar men kan surfen."""
