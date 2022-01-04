from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLPrimitiveDatatypeCreator
class DteIPv4Adres(KwantWrd):
    """Beschrijft een ip-adres volgens de ipv4 specificatie."""

    def __init__(self, waarde=None):
        self.waardeVeld = StringField(naam="waarde",
                                      label="waarde",
                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteIPv4Adres.waarde",
                                      definition="De string die het IPv4 adres representeert.",
                                      constraints="",
                                      usagenote="Het formaat is een decimale notatie bv. 91.198.174.232",
                                      deprecated_version="")
        """De string die het IPv4 adres representeert."""

        super().__init__(naam="DteIPv4Adres",
                         label="IPv4-adres",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteIPv4Adres",
                         definition="Beschrijft een ip-adres volgens de ipv4 specificatie.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=self.waardeVeld,
                         eenheidVeld=None,
                         waarde=waarde)
