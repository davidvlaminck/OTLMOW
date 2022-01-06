from OTLModel.Classes.GestandaardiseerdeKantopsluiting import GestandaardiseerdeKantopsluiting
from OTLModel.Datatypes.DtcLENorm import DtcLENorm
from OTLModel.Datatypes.DtcTrottoirbandVorm import DtcTrottoirbandVorm
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLETrottoirbandType import KlLETrottoirbandType


# Generated with OTLClassCreator. To modify: extend, do not edit
class TrottoirbandStd(GestandaardiseerdeKantopsluiting):
    """Gestandaardiseerde kantopsluiting,bestemd om de rand van de verharding te beschermen en te versterken."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandStd"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.norm = DtcLENorm()
        """De gestandaardiseerde trottoirband volgens aangeduide norm."""
        self.norm.naam = "norm"
        self.norm.label = "norm"
        self.norm.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandStd.norm"
        self.norm.definition = "De gestandaardiseerde trottoirband volgens aangeduide norm."
        self.norm.constraints = ""
        self.norm.usagenote = ""
        self.norm.deprecated_version = ""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlLETrottoirbandType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandStd.type",
                                    definition="Bepaling van het type van trottoirband.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Bepaling van het type van trottoirband."""

        self.vorm = DtcTrottoirbandVorm()
        """Bepaling van de vorm van de trottoirband."""
        self.vorm.naam = "vorm"
        self.vorm.label = "vorm"
        self.vorm.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandStd.vorm"
        self.vorm.definition = "Bepaling van de vorm van de trottoirband."
        self.vorm.constraints = ""
        self.vorm.usagenote = ""
        self.vorm.deprecated_version = ""
