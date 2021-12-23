from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBVLaagtype import KlBVLaagtype
from OTLModel.Datatypes.KwantWrdInTon import KwantWrdInTon


# Generated with OTLComplexDatatypeCreator
class DtcProfileerlaag(ComplexField):
    """Complex datatype om extra informatie te capteren van de profilerende laag."""

    def __init__(self):
        super().__init__(naam="DtcProfileerlaag",
                         label="Profileerlaag",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcProfileerlaag",
                         definition="Complex datatype om extra informatie te capteren van de profilerende laag.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.gewicht = KwantWrdInTon()
        """Het gewicht van de profileerlaag in ton."""
        self.waarde.gewicht.naam = "gewicht"
        self.waarde.gewicht.label = "gewicht"
        self.waarde.gewicht.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcProfileerlaag.gewicht"
        self.waarde.gewicht.definition = "Het gewicht van de profileerlaag in ton."
        self.waarde.gewicht.constraints = ""
        self.waarde.gewicht.usagenote = ""
        self.waarde.gewicht.deprecated_version = ""
        self.gewicht = self.waarde.gewicht

        self.waarde.laagtype = KeuzelijstField(naam="laagtype",
                                               label="laagtype",
                                               lijst=KlBVLaagtype(),
                                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcProfileerlaag.laagtype",
                                               definition="Het type van de bitumineuze verharding.",
                                               constraints="",
                                               usagenote="",
                                               deprecated_version="")
        self.laagtype = self.waarde.laagtype
        """Het type van de bitumineuze verharding."""
