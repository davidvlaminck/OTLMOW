# coding=utf-8
from OTLModel.Classes.AIMToestand import AIMToestand
from OTLModel.Classes.AIMDBStatus import AIMDBStatus
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.DtcIdentificator import DtcIdentificator
from OTLModel.Datatypes.StringField import StringField
from OTLModel.Datatypes.URIField import URIField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Derdenobject(AIMToestand, AIMDBStatus):
    """Object niet in eigendom van de assetbeheerder dat zonder verdere typering bewaard wordt om relaties met getypeerde assets te kunnen beheren."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMToestand.__init__(self)
        AIMDBStatus.__init__(self)

        self.assetId = DtcIdentificator()
        """Unieke identificatie van de asset zoals toegekend door de assetbeheerder of n.a.v. eerste aanlevering door de leverancier."""
        self.assetId.naam = "assetId"
        self.assetId.label = "asset-id"
        self.assetId.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject.assetId"
        self.assetId.definition = "Unieke identificatie van de asset zoals toegekend door de assetbeheerder of n.a.v. eerste aanlevering door de leverancier."
        self.assetId.constraints = ""
        self.assetId.usagenote = ""
        self.assetId.deprecated_version = ""

        self.contactgegevens = StringField(naam="contactgegevens",
                                           label="contactgegevens",
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject.contactgegevens",
                                           definition="Naam, voornaam, telefoonnummer en/of e-mailadres van de contactpersoon.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """Naam, voornaam, telefoonnummer en/of e-mailadres van de contactpersoon."""

        fotoField = DtcDocument()
        fotoField.naam = "foto"
        fotoField.label = "foto"
        fotoField.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject.foto"
        fotoField.definition = "Een foto van het derdenobject die eventuele detailinformatie weergeeft."
        fotoField.constraints = ""
        fotoField.usagenote = "Enkel bestanden die een foto zijn."
        fotoField.deprecated_version = ""
        self.foto = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=fotoField)
        """Een foto van het derdenobject die eventuele detailinformatie weergeeft."""

        self.heeftAansluitkastGeintegreerd = BooleanField(naam="heeftAansluitkastGeintegreerd",
                                                          label="heeft aansluitkast geïntegreerd",
                                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject.heeftAansluitkastGeintegreerd",
                                                          definition="Aanduiding of de aansluitkast geïntegreerd is.",
                                                          constraints="",
                                                          usagenote="",
                                                          deprecated_version="")
        """Aanduiding of de aansluitkast geïntegreerd is."""

        self.omschrijving = StringField(naam="omschrijving",
                                        label="omschrijving",
                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject.omschrijving",
                                        definition="Omschrijving van het derdenobject.",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """Omschrijving van het derdenobject."""

        self.typeURI = URIField(naam="typeURI",
                                label="type URI",
                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject.typeURI",
                                definition="De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI .",
                                constraints="",
                                usagenote="",
                                deprecated_version="")
        """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI ."""
