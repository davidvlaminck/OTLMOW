from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBSSRandafwerking import KlBSSRandafwerking
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLComplexDatatypeCreator
class DtcBSSRandafwerking(ComplexField):
    """Complex datatype voor de afwerking van de rand van een betonstraatsteenverharding."""

    def __init__(self):
        super().__init__(naam="DtcBSSRandafwerking",
                         label="Betonstraatsteenafwerking",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcBSSRandafwerking",
                         definition="Complex datatype voor de afwerking van de rand van een betonstraatsteenverharding.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.lengteRandafwerking = KwantWrdInMeter()
        self.waarde.lengteRandafwerking.naam = "lengteRandafwerking"
        self.waarde.lengteRandafwerking.label = "lengte randafwerking"
        self.waarde.lengteRandafwerking.definition = "De lengte in meter van de randafwerking."
        self.waarde.lengteRandafwerking.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcBSSRandafwerking.lengteRandafwerking"
        self.waarde.lengteRandafwerking.overerving = 0
        self.waarde.lengteRandafwerking.constraints = ""
        self.waarde.lengteRandafwerking.readonly = 0
        self.waarde.lengteRandafwerking.usagenote = ""
        self.waarde.lengteRandafwerking.deprecated_version = ""
        self.lengteRandafwerking = self.waarde.lengteRandafwerking
        """De lengte in meter van de randafwerking."""

        self.waarde.randafwerking = KeuzelijstField(naam="randafwerking",
                                                    lijst=KlBSSRandafwerking(),
                                                    overerving=0,
                                                    label="randafwerking",
                                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcBSSRandafwerking.randafwerking",
                                                    definition="De mogelijke wijzen van randafwerking van de verharding.",
                                                    constraints="",
                                                    usagenote="",
                                                    deprecated_version="")
        self.randafwerking = self.waarde.randafwerking
        """De mogelijke wijzen van randafwerking van de verharding."""
