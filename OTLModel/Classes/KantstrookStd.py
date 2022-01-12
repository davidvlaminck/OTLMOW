# coding=utf-8
from OTLModel.Classes.GestandaardiseerdeKantopsluiting import GestandaardiseerdeKantopsluiting
from OTLModel.Datatypes.DtcLENorm import DtcLENorm
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLEKantstrookType import KlLEKantstrookType
from OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class KantstrookStd(GestandaardiseerdeKantopsluiting):
    """Gestandaardiseerde kantopsluiting, bestemd om de verharding steun te geven."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KantstrookStd"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.breedte = KwantWrdInCentimeter()
        """De breedte van de gestandaardiseerde kantstrook in centimeter."""
        self.breedte.naam = "breedte"
        self.breedte.label = "breedte"
        self.breedte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KantstrookStd.breedte"
        self.breedte.definition = "De breedte van de gestandaardiseerde kantstrook in centimeter."
        self.breedte.constraints = ""
        self.breedte.usagenote = ""
        self.breedte.deprecated_version = ""

        self.dikte = KwantWrdInCentimeter()
        """De dikte van de gestandaardiseerde kantstrook in centimeter."""
        self.dikte.naam = "dikte"
        self.dikte.label = "dikte"
        self.dikte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KantstrookStd.dikte"
        self.dikte.definition = "De dikte van de gestandaardiseerde kantstrook in centimeter."
        self.dikte.constraints = ""
        self.dikte.usagenote = ""
        self.dikte.deprecated_version = ""

        self.norm = DtcLENorm()
        """De gestandaardiseerd kantstrook volgens aangeduide norm."""
        self.norm.naam = "norm"
        self.norm.label = "norm"
        self.norm.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KantstrookStd.norm"
        self.norm.definition = "De gestandaardiseerd kantstrook volgens aangeduide norm."
        self.norm.constraints = ""
        self.norm.usagenote = ""
        self.norm.deprecated_version = ""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlLEKantstrookType(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KantstrookStd.type",
                                    definition="Het type van gestandaardiseerde kantstrook.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type van gestandaardiseerde kantstrook."""
