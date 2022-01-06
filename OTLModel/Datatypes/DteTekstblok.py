# coding=utf-8
from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class DteTekstblok(KwantWrd):
    """Een tekst welke uit meerdere zinnen bestaat, en ook regeleindes kan bevatten. Een tekstblok bevat maximaal 65.000 karakters."""

    def __init__(self, waarde=None):
        self.waardeVeld = StringField(naam="waarde",
                                      label="waarde",
                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTekstblok.waarde",
                                      definition="De string welke uit meerdere zinnen bestaat, en ook regeleindes kan bevatten. Een tekstblok bevat maximaal 65.000 karakters.",
                                      constraints="",
                                      usagenote="",
                                      deprecated_version="")
        """De string welke uit meerdere zinnen bestaat, en ook regeleindes kan bevatten. Een tekstblok bevat maximaal 65.000 karakters."""

        super().__init__(naam="DteTekstblok",
                         label="Tekstblok",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTekstblok",
                         definition="Een tekst welke uit meerdere zinnen bestaat, en ook regeleindes kan bevatten. Een tekstblok bevat maximaal 65.000 karakters.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=self.waardeVeld,
                         eenheidVeld=None,
                         waarde=waarde)
