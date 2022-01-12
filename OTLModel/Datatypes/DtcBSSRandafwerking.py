# coding=utf-8
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBSSRandafwerking import KlBSSRandafwerking
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcBSSRandafwerking(ComplexField):
    """Complex datatype voor de afwerking van de rand van een betonstraatsteenverharding."""

    def __init__(self):
        super().__init__(naam="DtcBSSRandafwerking",
                         label="Betonstraatsteenafwerking",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcBSSRandafwerking",
                         definition="Complex datatype voor de afwerking van de rand van een betonstraatsteenverharding.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.lengteRandafwerking = KwantWrdInMeter()
        """De lengte in meter van de randafwerking."""
        self.waarde.lengteRandafwerking.naam = "lengteRandafwerking"
        self.waarde.lengteRandafwerking.label = "lengte randafwerking"
        self.waarde.lengteRandafwerking.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcBSSRandafwerking.lengteRandafwerking"
        self.waarde.lengteRandafwerking.definition = "De lengte in meter van de randafwerking."
        self.waarde.lengteRandafwerking.constraints = ""
        self.waarde.lengteRandafwerking.usagenote = ""
        self.waarde.lengteRandafwerking.deprecated_version = ""
        self.lengteRandafwerking = self.waarde.lengteRandafwerking

        self.waarde.randafwerking = KeuzelijstField(naam="randafwerking",
                                                    label="randafwerking",
                                                    lijst=KlBSSRandafwerking(),
                                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcBSSRandafwerking.randafwerking",
                                                    definition="De mogelijke wijzen van randafwerking van de verharding.",
                                                    constraints="",
                                                    usagenote="",
                                                    deprecated_version="")
        self.randafwerking = self.waarde.randafwerking
        """De mogelijke wijzen van randafwerking van de verharding."""
