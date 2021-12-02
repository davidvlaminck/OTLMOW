from ModelGenerator.BaseClasses.KeuzelijstField import KeuzelijstField
from ModelGenerator.BaseClasses.StringField import StringField
from OTLClasses.Verification.KlAlgGemeente import KlAlgGemeente


class DtcAdres:
    """Complex datatype voor de aanduiding van een bepaalde locatie, doorgaans van een huis, woning, gebouw of faciliteit, op de aarde."""

    bus = StringField()
    """Een nummer dat de postbus aanduidt."""

    gemeente = KeuzelijstField(KlAlgGemeente())
    """De bestuurlijke eenheid waarin het adres gelegen is."""

    huisnummer = StringField()
    """Een nummer dat door de gemeente aan bv. een huis wordt toegekend."""

    postcode = StringField()
    """Een korte reeks tekens die in het postadres wordt opgenomen."""

    straatnaam = StringField()
    """De naam van de straat."""

     # TODO provincie

    uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres'

