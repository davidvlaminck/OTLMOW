# coding=utf-8
from OTLModel.Datatypes.UnionTypeField import UnionTypeField
from OTLModel.Datatypes.DtcAfmetingBxlInCm import DtcAfmetingBxlInCm
from OTLModel.Datatypes.DtcAfmetingDiameterInCm import DtcAfmetingDiameterInCm


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuAfmetingGrondvlak(UnionTypeField):
    """Datatype voor de afmeting van een (grond)vlak volgens zijn vorm."""

    def __init__(self):
        super().__init__(naam="DtuAfmetingGrondvlak",
                         label="afmeting grondvlak",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuAfmetingGrondvlak",
                         definition="Datatype voor de afmeting van een (grond)vlak volgens zijn vorm.",
                         usagenote="",
                         deprecated_version="")

        field_rechthoekig = DtcAfmetingBxlInCm()
        """Afmetingen voor breedte en lengte of diepte. De breedte meet van links naar rechts in vooraanzicht, de lengte van voor naar achter."""
        field_rechthoekig.naam = "rechthoekig"
        field_rechthoekig.label = "rechthoekig"
        field_rechthoekig.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuAfmetingGrondvlak.rechthoekig"
        field_rechthoekig.definition = "Afmetingen voor breedte en lengte of diepte. De breedte meet van links naar rechts in vooraanzicht, de lengte van voor naar achter."
        field_rechthoekig.constraints = ""
        field_rechthoekig.usagenote = ""
        field_rechthoekig.deprecated_version = ""

        field_rond = DtcAfmetingDiameterInCm()
        """Afmeting van de diameter in centimeter van een rond (grond)vlak."""
        field_rond.naam = "rond"
        field_rond.label = "rond"
        field_rond.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuAfmetingGrondvlak.rond"
        field_rond.definition = "Afmeting van de diameter in centimeter van een rond (grond)vlak."
        field_rond.constraints = ""
        field_rond.usagenote = ""
        field_rond.deprecated_version = ""

        self.fieldsTuple = (field_rechthoekig, field_rond)
