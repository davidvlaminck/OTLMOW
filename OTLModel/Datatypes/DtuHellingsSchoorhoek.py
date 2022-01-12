# coding=utf-8
from OTLModel.Datatypes.UnionTypeField import UnionTypeField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlSchoorhoek import KlSchoorhoek
from OTLModel.Datatypes.KwantWrdInDecimaleGraden import KwantWrdInDecimaleGraden


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuHellingsSchoorhoek(UnionTypeField):
    """Union datatype voor de hellings- of de schoorhoek."""

    def __init__(self):
        super().__init__(naam="DtuHellingsSchoorhoek",
                         label="Hellings- of schoorhoek",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuHellingsSchoorhoek",
                         definition="Union datatype voor de hellings- of de schoorhoek.",
                         usagenote="",
                         deprecated_version="")

        field_hellingshoek = KwantWrdInDecimaleGraden()
        """Hoek die het object maakt ten opzichte van de verticale, uitgedrukt in decimale graden."""
        field_hellingshoek.naam = "hellingshoek"
        field_hellingshoek.label = "hellingshoek"
        field_hellingshoek.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuHellingsSchoorhoek.hellingshoek"
        field_hellingshoek.definition = "Hoek die het object maakt ten opzichte van de verticale, uitgedrukt in decimale graden."
        field_hellingshoek.constraints = ""
        field_hellingshoek.usagenote = ""
        field_hellingshoek.deprecated_version = ""

        field_schoorhoek = KeuzelijstField(naam="schoorhoek",
                                           label="schoorhoek",
                                           lijst=KlSchoorhoek(),
                                           objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuHellingsSchoorhoek.schoorhoek",
                                           definition="Hoek die het object maakt ten opzichte van de verticale, uitgedrukt in 1 op x (vb.: 1/4).",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """Hoek die het object maakt ten opzichte van de verticale, uitgedrukt in 1 op x (vb.: 1/4)."""

        self.fieldsTuple = (field_hellingshoek, field_schoorhoek)
