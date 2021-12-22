from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlAlgGemeente import KlAlgGemeente
from OTLModel.Datatypes.KlAlgProvincie import KlAlgProvincie
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLComplexDatatypeCreator
class DtcAdres(ComplexField):
    """Complex datatype voor de aanduiding van een bepaalde locatie, doorgaans van een huis, woning, gebouw of faciliteit, op de aarde."""

    def __init__(self):
        super().__init__(naam="DtcAdres",
                         label="Adres",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres",
                         definition="Complex datatype voor de aanduiding van een bepaalde locatie, doorgaans van een huis, woning, gebouw of faciliteit, op de aarde.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.bus = StringField(naam="bus",
                                      label="bus",
                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.bus",
                                      definition="Een nummer dat de postbus aanduidt.",
                                      constraints="",
                                      usagenote="",
                                      deprecated_version="")
        self.bus = self.waarde.bus
        """Een nummer dat de postbus aanduidt."""

        self.waarde.gemeente = KeuzelijstField(naam="gemeente",
                                               lijst=KlAlgGemeente(),
                                               overerving=0,
                                               label="gemeente",
                                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.gemeente",
                                               definition="De bestuurlijke eenheid waarin het adres gelegen is.",
                                               constraints="",
                                               usagenote="",
                                               deprecated_version="")
        self.gemeente = self.waarde.gemeente
        """De bestuurlijke eenheid waarin het adres gelegen is."""

        self.waarde.huisnummer = StringField(naam="huisnummer",
                                             label="huisnummer",
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.huisnummer",
                                             definition="Een nummer dat door de gemeente aan bv. een huis wordt toegekend.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        self.huisnummer = self.waarde.huisnummer
        """Een nummer dat door de gemeente aan bv. een huis wordt toegekend."""

        self.waarde.postcode = StringField(naam="postcode",
                                           label="postcode",
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.postcode",
                                           definition="Een korte reeks tekens die in het postadres wordt opgenomen.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        self.postcode = self.waarde.postcode
        """Een korte reeks tekens die in het postadres wordt opgenomen."""

        self.waarde.provincie = KeuzelijstField(naam="provincie",
                                                lijst=KlAlgProvincie(),
                                                overerving=0,
                                                label="provincie",
                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.provincie",
                                                definition="Het deelgebied waarin het adres gelegen is.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        self.provincie = self.waarde.provincie
        """Het deelgebied waarin het adres gelegen is."""

        self.waarde.straatnaam = StringField(naam="straatnaam",
                                             label="straatnaam",
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.straatnaam",
                                             definition="De naam van de straat.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        self.straatnaam = self.waarde.straatnaam
        """De naam van de straat."""
