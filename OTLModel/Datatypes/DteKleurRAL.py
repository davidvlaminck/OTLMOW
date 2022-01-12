# coding=utf-8
from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class DteKleurRAL(KwantWrd):
    """Beschrijft een kleur volgens het RAL classificatiesysteem. De waarde is een natuurlijk getal tussen 1000 en 9999."""

    def __init__(self, waarde=None):
        self.waardeVeld = StringField(naam="waarde",
                                      label="waarde",
                                      objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteKleurRAL.waarde",
                                      definition="Beschrijft een kleur volgens het RAL classificatiesysteem.",
                                      constraints="",
                                      usagenote="De waarde moet voldoen aan volgende regex: [1-9]\d{3}",
                                      deprecated_version="")
        """Beschrijft een kleur volgens het RAL classificatiesysteem."""

        super().__init__(naam="DteKleurRAL",
                         label="RAL-kleur",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteKleurRAL",
                         definition="Beschrijft een kleur volgens het RAL classificatiesysteem. De waarde is een natuurlijk getal tussen 1000 en 9999.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=self.waardeVeld,
                         eenheidVeld=None,
                         waarde=waarde)
