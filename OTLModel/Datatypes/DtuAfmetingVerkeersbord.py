# coding=utf-8
from OTLModel.Datatypes.UnionTypeField import UnionTypeField
from OTLModel.Datatypes.DtcAfmetingBxhInMm import DtcAfmetingBxhInMm
from OTLModel.Datatypes.DtcAfmetingDiameterInMm import DtcAfmetingDiameterInMm
from OTLModel.Datatypes.DtcAfmetingZijdeInMm import DtcAfmetingZijdeInMm


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuAfmetingVerkeersbord(UnionTypeField):
    """Union datatype voor de afmeting van het verkeersbord."""

    def __init__(self):
        super().__init__(naam="DtuAfmetingVerkeersbord",
                         label="Afmeting verkeersbord",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuAfmetingVerkeersbord",
                         definition="Union datatype voor de afmeting van het verkeersbord.",
                         usagenote="",
                         deprecated_version="")

        field_achthoekig = DtcAfmetingZijdeInMm()
        """De afmeting voor een achthoekig verkeersbord (zijde in millimeter)."""
        field_achthoekig.naam = "achthoekig"
        field_achthoekig.label = "achthoekig"
        field_achthoekig.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuAfmetingVerkeersbord.achthoekig"
        field_achthoekig.definition = "De afmeting voor een achthoekig verkeersbord (zijde in millimeter)."
        field_achthoekig.constraints = ""
        field_achthoekig.usagenote = ""
        field_achthoekig.deprecated_version = ""

        field_driehoekig = DtcAfmetingZijdeInMm()
        """De afmeting van een driehoekig verkeersbord (zijde in millimeter)."""
        field_driehoekig.naam = "driehoekig"
        field_driehoekig.label = "driehoekig"
        field_driehoekig.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuAfmetingVerkeersbord.driehoekig"
        field_driehoekig.definition = "De afmeting van een driehoekig verkeersbord (zijde in millimeter)."
        field_driehoekig.constraints = ""
        field_driehoekig.usagenote = ""
        field_driehoekig.deprecated_version = ""

        field_rond = DtcAfmetingDiameterInMm()
        """De afmeting voor een rond verkeersbord (diameter in millimeter)."""
        field_rond.naam = "rond"
        field_rond.label = "rond"
        field_rond.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuAfmetingVerkeersbord.rond"
        field_rond.definition = "De afmeting voor een rond verkeersbord (diameter in millimeter)."
        field_rond.constraints = ""
        field_rond.usagenote = ""
        field_rond.deprecated_version = ""

        field_vierhoekig = DtcAfmetingBxhInMm()
        """De afmeting voor een vierhoekig verkeersbord (breedte en hoogte in millimeter)."""
        field_vierhoekig.naam = "vierhoekig"
        field_vierhoekig.label = "vierhoekig"
        field_vierhoekig.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuAfmetingVerkeersbord.vierhoekig"
        field_vierhoekig.definition = "De afmeting voor een vierhoekig verkeersbord (breedte en hoogte in millimeter)."
        field_vierhoekig.constraints = ""
        field_vierhoekig.usagenote = ""
        field_vierhoekig.deprecated_version = ""

        field_zeshoekig = DtcAfmetingZijdeInMm()
        """De afmeting voor een zeshoekig verkeersbord (zijde in millimeter)."""
        field_zeshoekig.naam = "zeshoekig"
        field_zeshoekig.label = "zeshoekig"
        field_zeshoekig.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuAfmetingVerkeersbord.zeshoekig"
        field_zeshoekig.definition = "De afmeting voor een zeshoekig verkeersbord (zijde in millimeter)."
        field_zeshoekig.constraints = ""
        field_zeshoekig.usagenote = ""
        field_zeshoekig.deprecated_version = ""

        self.fieldsTuple = (field_achthoekig, field_driehoekig, field_rond, field_vierhoekig, field_zeshoekig)
