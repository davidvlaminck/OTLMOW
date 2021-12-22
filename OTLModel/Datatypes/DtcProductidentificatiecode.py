from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.StringField import StringField
from OTLModel.Datatypes.URIField import URIField


# Generated with OTLComplexDatatypeCreator
class DtcProductidentificatiecode(ComplexField):
    """Complex datatype dat alle nodige informatie van het product capteert."""

    def __init__(self):
        super().__init__(naam="DtcProductidentificatiecode",
                         label="Productidentificatiecode",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcProductidentificatiecode",
                         definition="Complex datatype dat alle nodige informatie van het product capteert.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.keuringsverslag = DtcDocument()
        self.waarde.keuringsverslag.naam = "keuringsverslag"
        self.waarde.keuringsverslag.label = "keuringsverslag"
        self.waarde.keuringsverslag.definition = "Een rapport met de resultaten van de keuring."
        self.waarde.keuringsverslag.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcProductidentificatiecode.keuringsverslag"
        self.waarde.keuringsverslag.overerving = 0
        self.waarde.keuringsverslag.constraints = ""
        self.waarde.keuringsverslag.readonly = 0
        self.waarde.keuringsverslag.usagenote = ""
        self.waarde.keuringsverslag.deprecated_version = ""
        self.keuringsverslag = self.waarde.keuringsverslag
        """Een rapport met de resultaten van de keuring."""

        self.waarde.linkTechnischeFiche = URIField(naam="linkTechnischeFiche",
                                                   label="link technische fiche",
                                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcProductidentificatiecode.linkTechnischeFiche",
                                                   definition="De link naar de technische fiche van het gerelateerd product.",
                                                   constraints="",
                                                   usagenote="",
                                                   deprecated_version="")
        self.linkTechnischeFiche = self.waarde.linkTechnischeFiche
        """De link naar de technische fiche van het gerelateerd product."""

        self.waarde.producent = StringField(naam="producent",
                                            label="producent",
                                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcProductidentificatiecode.producent",
                                            definition="De gerelateerde fabrikant.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        self.producent = self.waarde.producent
        """De gerelateerde fabrikant."""

        self.waarde.productidentificatiecode = StringField(naam="productidentificatiecode",
                                                           label="productidentificatiecode",
                                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcProductidentificatiecode.productidentificatiecode",
                                                           definition="De code van het gebruikte product (COPRO/BENOR).",
                                                           constraints="",
                                                           usagenote="",
                                                           deprecated_version="")
        self.productidentificatiecode = self.waarde.productidentificatiecode
        """De code van het gebruikte product (COPRO/BENOR)."""
