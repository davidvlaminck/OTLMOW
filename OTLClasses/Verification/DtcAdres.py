from ModelGenerator.BaseClasses.OTLField import OTLField
from ModelGenerator.BaseClasses.StringField import StringField
from OTLClasses.Verification.KlAlgGemeente import KlAlgGemeente


class DtcAdres(OTLField):
    """Complex datatype voor de aanduiding van een bepaalde locatie, doorgaans van een huis, woning, gebouw of
    faciliteit, op de aarde. """

    def __init__(self):
        super().__init__("DtcAdres", "Adres", "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres", "Complex datatype voor de aanduiding van een bepaalde locatie, doorgaans van een huis, woning, gebouw of faciliteit, op de aarde.", None, "", "")

        self.bus = StringField(naam="bus", label="bus", uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres"
                                                       ".bus", definition="Een nummer dat de postbus aanduidt.", constraints="",
                          usagenote="", deprecated_version="")
        """Een nummer dat de postbus aanduidt."""

        self.gemeente = KlAlgGemeente()
        """De bestuurlijke eenheid waarin het adres gelegen is."""

        self.huisnummer = StringField(naam="huisnummer", label="huisnummer", uri="https://wegenenverkeer.data.vlaanderen.be/ns"
                                                                            "/implementatieelement#DtcAdres.huisnummer",
                                 definition="Een nummer dat door de gemeente aan bv. een huis wordt toegekend.", constraints="",
                                 usagenote="", deprecated_version="")
        """Een nummer dat door de gemeente aan bv. een huis wordt toegekend."""

        self.postcode = StringField(naam="postcode", label="postcode",
                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.postcode",
                               definition="Een korte reeks tekens die in het postadres wordt opgenomen.", constraints="",
                               usagenote="", deprecated_version="")
        """Een korte reeks tekens die in het postadres wordt opgenomen."""

        self.straatnaam = StringField(naam="straatnaam", label="straatnaam",
                                 uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.straatnaam",
                                 definition="De naam van de straat.", constraints="",
                                 usagenote="", deprecated_version="")
        """De naam van de straat."""

    # TODO provincie

    uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres'
