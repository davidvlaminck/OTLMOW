# coding=utf-8
from OTLModel.Classes.GestandaardiseerdeKantopsluiting import GestandaardiseerdeKantopsluiting
from OTLModel.Datatypes.DtcLENorm import DtcLENorm
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLESchampkantType import KlLESchampkantType
from OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class SchampkantStd(GestandaardiseerdeKantopsluiting):
    """Gestandaardiseerde kantopsluiting, die zones van voertuigenverkeer onderling of voertuigenzones van andere verkeerszones scheidt en de overschrijding door voertuigen bemoeilijkt maar geen voertuigkerende functie heeft."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SchampkantStd"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.breedte = KwantWrdInCentimeter()
        """De breedte van de gestandaardiseerde schampkant in centimeter."""
        self.breedte.naam = "breedte"
        self.breedte.label = "breedte"
        self.breedte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SchampkantStd.breedte"
        self.breedte.definition = "De breedte van de gestandaardiseerde schampkant in centimeter."
        self.breedte.constraints = ""
        self.breedte.usagenote = ""
        self.breedte.deprecated_version = ""

        self.dikte = KwantWrdInCentimeter()
        """De dikte van de gestandaardiseerde schampkant in centimeter."""
        self.dikte.naam = "dikte"
        self.dikte.label = "dikte"
        self.dikte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SchampkantStd.dikte"
        self.dikte.definition = "De dikte van de gestandaardiseerde schampkant in centimeter."
        self.dikte.constraints = ""
        self.dikte.usagenote = ""
        self.dikte.deprecated_version = ""

        self.norm = DtcLENorm()
        """De gestandaardiseerde schampkant volgens aangeduide norm."""
        self.norm.naam = "norm"
        self.norm.label = "norm"
        self.norm.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SchampkantStd.norm"
        self.norm.definition = "De gestandaardiseerde schampkant volgens aangeduide norm."
        self.norm.constraints = ""
        self.norm.usagenote = ""
        self.norm.deprecated_version = ""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlLESchampkantType(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SchampkantStd.type",
                                    definition="Het type van gestandaardiseerde schampkant.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type van gestandaardiseerde schampkant."""
