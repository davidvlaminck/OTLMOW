# coding=utf-8
from OTLModel.Datatypes.UnionTypeField import UnionTypeField
from OTLModel.Datatypes.DtcAfmetingBxlxhInMm import DtcAfmetingBxlxhInMm
from OTLModel.Datatypes.DtcAfmetingDiameterInMm import DtcAfmetingDiameterInMm


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuDwarsafmetingen(UnionTypeField):
    """Union datatype voor de dwarsafmetingen van een object volgens zijn vorm."""

    def __init__(self):
        super().__init__(naam="DtuDwarsafmetingen",
                         label="Dwarsafmetingen",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuDwarsafmetingen",
                         definition="Union datatype voor de dwarsafmetingen van een object volgens zijn vorm.",
                         usagenote="",
                         deprecated_version="")

        field_rechthoekig = DtcAfmetingBxlxhInMm()
        """Afmetingen voor breedte, lengte en hoogte van een rechthoekig object."""
        field_rechthoekig.naam = "rechthoekig"
        field_rechthoekig.label = "rechthoekig"
        field_rechthoekig.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuDwarsafmetingen.rechthoekig"
        field_rechthoekig.definition = "Afmetingen voor breedte, lengte en hoogte van een rechthoekig object."
        field_rechthoekig.constraints = ""
        field_rechthoekig.usagenote = ""
        field_rechthoekig.deprecated_version = ""

        field_rond = DtcAfmetingDiameterInMm()
        """Afmeting van de diameter in milimeter van een rond object."""
        field_rond.naam = "rond"
        field_rond.label = "rond"
        field_rond.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuDwarsafmetingen.rond"
        field_rond.definition = "Afmeting van de diameter in milimeter van een rond object."
        field_rond.constraints = ""
        field_rond.usagenote = ""
        field_rond.deprecated_version = ""

        self.fieldsTuple = (field_rechthoekig, field_rond)
