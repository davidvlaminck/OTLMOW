# coding=utf-8
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.IntegerField import IntegerField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlPoortconfiguratieRichting import KlPoortconfiguratieRichting
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcSoftwarePoortconfiguratie(ComplexField):
    """Complex datatype dat beschrijft welke poort voor welke service gebruikt wordt."""

    def __init__(self):
        super().__init__(naam="DtcSoftwarePoortconfiguratie",
                         label="Software poortconfiguratie",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSoftwarePoortconfiguratie",
                         definition="Complex datatype dat beschrijft welke poort voor welke service gebruikt wordt.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.poortnummer = IntegerField(naam="poortnummer",
                                               label="poortnummer",
                                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSoftwarePoortconfiguratie.poortnummer",
                                               definition="Het nummer dat werd toegekend aan de (netwerk)poort.",
                                               constraints="",
                                               usagenote="",
                                               deprecated_version="")
        self.poortnummer = self.waarde.poortnummer
        """Het nummer dat werd toegekend aan de (netwerk)poort."""

        self.waarde.richting = KeuzelijstField(naam="richting",
                                               label="richting",
                                               lijst=KlPoortconfiguratieRichting(),
                                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSoftwarePoortconfiguratie.richting",
                                               definition="De richting waarin de poort openstaat.",
                                               constraints="",
                                               usagenote="",
                                               deprecated_version="")
        self.richting = self.waarde.richting
        """De richting waarin de poort openstaat."""

        self.waarde.service = StringField(naam="service",
                                          label="service",
                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSoftwarePoortconfiguratie.service",
                                          definition="De service die op een bepaalde poort is aangesloten.",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        self.service = self.waarde.service
        """De service die op een bepaalde poort is aangesloten."""
