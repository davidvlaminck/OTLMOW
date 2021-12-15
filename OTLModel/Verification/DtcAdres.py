from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.StringField import StringField
from OTLModel.Verification.KlAlgGemeente import KlAlgGemeente


class DtcAdres(ComplexField):
    """Complex datatype voor de aanduiding van een bepaalde locatie, doorgaans van een huis, woning, gebouw of
    faciliteit, op de aarde. """

    def __init__(self):
        super().__init__("DtcAdres", "Adres", "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres",
                         "Complex datatype voor de aanduiding van een bepaalde locatie, doorgaans van een huis, woning, "
                         "gebouw of faciliteit, op de aarde.",
                         None, "", "")

        self.waarde.bus = StringField(naam="bus", label="bus",
                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres"
                                   ".bus", definition="Een nummer dat de postbus aanduidt.", constraints="",
                               usagenote="", deprecated_version="")
        """Een nummer dat de postbus aanduidt."""

        self.waarde.gemeente = KlAlgGemeente()
        """De bestuurlijke eenheid waarin het adres gelegen is."""

        self.waarde.huisnummer = StringField(naam="huisnummer", label="huisnummer", uri="https://wegenenverkeer.data.vlaanderen.be/ns"
                                                                                 "/implementatieelement#DtcAdres.huisnummer",
                                      definition="Een nummer dat door de gemeente aan bv. een huis wordt toegekend.",
                                      constraints="",
                                      usagenote="", deprecated_version="")
        """Een nummer dat door de gemeente aan bv. een huis wordt toegekend."""

        self.waarde.postcode = StringField(naam="postcode", label="postcode",
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.postcode",
                                    definition="Een korte reeks tekens die in het postadres wordt opgenomen.", constraints="",
                                    usagenote="", deprecated_version="")
        """Een korte reeks tekens die in het postadres wordt opgenomen."""

        self.waarde.straatnaam = StringField(naam="straatnaam", label="straatnaam",
                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.straatnaam",
                                      definition="De naam van de straat.", constraints="",
                                      usagenote="", deprecated_version="")
        """De naam van de straat."""

        self.bus = self.waarde.bus
        self.gemeente = self.waarde.gemeente
        self.huisnummer = self.waarde.huisnummer
        self.postcode = self.waarde.postcode
        self.straatnaam = self.waarde.straatnaam

    # TODO provincie

    uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres'
