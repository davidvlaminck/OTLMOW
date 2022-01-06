# coding=utf-8
from abc import abstractmethod
from OTLModel.Classes.AIMToestand import AIMToestand
from OTLModel.Classes.AIMDBStatus import AIMDBStatus
from OTLModel.BaseClasses.OTLAsset import OTLAsset
from OTLModel.BaseClasses.RelatieInteractor import RelatieInteractor
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.DateField import DateField
from OTLModel.Datatypes.DtcIdentificator import DtcIdentificator
from OTLModel.Datatypes.KwantWrdInMaand import KwantWrdInMaand
from OTLModel.Datatypes.StringField import StringField
from OTLModel.Datatypes.URIField import URIField


# Generated with OTLClassCreator. To modify: extend, do not edit
class AIMObject(AIMToestand, AIMDBStatus, OTLAsset, RelatieInteractor):
    """Abstracte als de basisklasse voor alle uniek geïdentificeerde OTL objecten met de basiseigenschappen die elk OTL object minstens heeft."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMToestand.__init__(self)
        AIMDBStatus.__init__(self)
        OTLAsset.__init__(self)
        RelatieInteractor.__init__(self)

        self.assetId = DtcIdentificator()
        """Unieke identificatie van de asset zoals toegekend door de assetbeheerder of n.a.v. eerste aanlevering door de leverancier."""
        self.assetId.naam = "assetId"
        self.assetId.label = "asset-id"
        self.assetId.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.assetId"
        self.assetId.definition = "Unieke identificatie van de asset zoals toegekend door de assetbeheerder of n.a.v. eerste aanlevering door de leverancier."
        self.assetId.constraints = ""
        self.assetId.usagenote = ""
        self.assetId.deprecated_version = ""

        bestekPostNummerField = StringField(naam="bestekPostNummer",
                                            label="bestekpostnummer",
                                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.bestekPostNummer",
                                            definition="Een verwijzing naar een postnummer uit het specifieke bestek waar het object mee verband houdt.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        self.bestekPostNummer = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=bestekPostNummerField)
        """Een verwijzing naar een postnummer uit het specifieke bestek waar het object mee verband houdt."""

        self.datumOprichtingObject = DateField(naam="datumOprichtingObject",
                                               label="datum oprichting object",
                                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.datumOprichtingObject",
                                               definition="Datum van de oprichting van het object.",
                                               constraints="",
                                               usagenote="",
                                               deprecated_version="")
        """Datum van de oprichting van het object."""

        self.notitie = StringField(naam="notitie",
                                   label="notitie",
                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.notitie",
                                   definition="Extra notitie voor het object.",
                                   constraints="",
                                   usagenote="",
                                   deprecated_version="")
        """Extra notitie voor het object."""

        standaardBestekPostNummerField = StringField(naam="standaardBestekPostNummer",
                                                     label="standaardbestekpostnummer",
                                                     uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.standaardBestekPostNummer",
                                                     definition="Een verwijzing naar een postnummer uit het standaardbestek waar het object mee verband houdt. De notatie van het postnummer moet overeenkomen met de notatie die gebruikt is in de catalogi van standaardbestekken, bijvoorbeeld postnummer 0701.20404G.",
                                                     constraints="",
                                                     usagenote="",
                                                     deprecated_version="")
        self.standaardBestekPostNummer = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=standaardBestekPostNummerField)
        """Een verwijzing naar een postnummer uit het standaardbestek waar het object mee verband houdt. De notatie van het postnummer moet overeenkomen met de notatie die gebruikt is in de catalogi van standaardbestekken, bijvoorbeeld postnummer 0701.20404G."""

        self.theoretischeLevensduur = KwantWrdInMaand()
        """ De levensduur in aantal maanden die theoretisch mag verwacht worden voor een object."""
        self.theoretischeLevensduur.naam = "theoretischeLevensduur"
        self.theoretischeLevensduur.label = "theoretische levensduur"
        self.theoretischeLevensduur.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.theoretischeLevensduur"
        self.theoretischeLevensduur.definition = " De levensduur in aantal maanden die theoretisch mag verwacht worden voor een object."
        self.theoretischeLevensduur.constraints = ""
        self.theoretischeLevensduur.usagenote = ""
        self.theoretischeLevensduur.deprecated_version = ""

        uri = self.typeURI
        self.typeURI = URIField(naam="typeURI",
                                label="type URI",
                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.typeURI",
                                definition="De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI .",
                                constraints="",
                                usagenote="",
                                deprecated_version="")
        """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI ."""
