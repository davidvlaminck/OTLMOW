# coding=utf-8
from OTLModel.Datatypes.UnionTypeField import UnionTypeField
from OTLModel.Datatypes.DtcProfileerlaag import DtcProfileerlaag
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBVLaagtype import KlBVLaagtype


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuBVLaagtypes(UnionTypeField):
    """Union datatype voor een laagtype anders dan de profileerlaag. Bij een profileerlaag kan men het gewicht toelichten."""

    def __init__(self):
        super().__init__(naam="DtuBVLaagtypes",
                         label="Laagtype van de bitumineuze verharding",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuBVLaagtypes",
                         definition="Union datatype voor een laagtype anders dan de profileerlaag. Bij een profileerlaag kan men het gewicht toelichten.",
                         usagenote="",
                         deprecated_version="")

        field_laagtype = KeuzelijstField(naam="laagtype",
                                         label="laagtype",
                                         lijst=KlBVLaagtype(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuBVLaagtypes.laagtype",
                                         definition="Het type van de bitumineuze verharding.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Het type van de bitumineuze verharding."""

        field_profileerlaag = DtcProfileerlaag()
        """De laag die het profiel verbetert van de verharding."""
        field_profileerlaag.naam = "profileerlaag"
        field_profileerlaag.label = "profileerlaag"
        field_profileerlaag.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuBVLaagtypes.profileerlaag"
        field_profileerlaag.definition = "De laag die het profiel verbetert van de verharding."
        field_profileerlaag.constraints = ""
        field_profileerlaag.usagenote = ""
        field_profileerlaag.deprecated_version = ""

        self.fieldsTuple = (field_laagtype, field_profileerlaag)
