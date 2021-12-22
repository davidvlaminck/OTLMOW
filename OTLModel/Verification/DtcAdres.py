from OTLModel.Datatypes.ComplexField import ComplexField, ComplexAttributen
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.StringField import StringField
from OTLModel.Datatypes.KlAlgGemeente import KlAlgGemeente


# Generated with OTLComplexDatatypeCreatorTests
class DtcAdres(ComplexField):
    """Complex datatype voor de aanduiding van een bepaalde locatie, doorgaans van een huis, woning, gebouw of faciliteit, op de aarde."""

    def __init__(self):
        super().__init__(naam="DtcAdres",
                         label="Adres",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres",
                         definition="Complex datatype voor de aanduiding van een bepaalde locatie, doorgaans van een huis, woning, gebouw of faciliteit, op de aarde.",
                         usagenote="",
                         deprecated_version="")
        self.waarde = ComplexAttributen()

        self.waarde.bus = StringField(naam="bus",
                                      label="bus",
                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.bus",
                                      definition="Een nummer dat de postbus aanduidt.",
                                      constraints="",
                                      usagenote="",
                                      deprecated_version="")
        """Een nummer dat de postbus aanduidt."""
        self.bus = self.waarde.bus

        self.waarde.gemeente = KeuzelijstField(naam="gemeente",
                                               lijst=KlAlgGemeente(),
                                               label="gemeente",
                                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.gemeente",
                                               definition="De bestuurlijke eenheid waarin het adres gelegen is.",
                                               overerving=False,
                                               constraints="",
                                               usagenote="",
                                               deprecated_version="")
        """De bestuurlijke eenheid waarin het adres gelegen is."""
        self.gemeente = self.waarde.gemeente

        self.waarde.huisnummer = StringField(naam="huisnummer",
                                             label="huisnummer",
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.huisnummer",
                                             definition="Een nummer dat door de gemeente aan bv. een huis wordt toegekend.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Een nummer dat door de gemeente aan bv. een huis wordt toegekend."""
        self.huisnummer = self.waarde.huisnummer

        self.waarde.postcode = StringField(naam="postcode",
                                           label="postcode",
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.postcode",
                                           definition="Een korte reeks tekens die in het postadres wordt opgenomen.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """Een korte reeks tekens die in het postadres wordt opgenomen."""
        self.postcode = self.waarde.postcode

        self.waarde.straatnaam = StringField(naam="straatnaam",
                                             label="straatnaam",
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.straatnaam",
                                             definition="De naam van de straat.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """De naam van de straat."""
        self.straatnaam = self.waarde.straatnaam

