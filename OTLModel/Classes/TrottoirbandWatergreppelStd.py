# coding=utf-8
from OTLModel.Classes.GestandaardiseerdeKantopsluiting import GestandaardiseerdeKantopsluiting
from OTLModel.Datatypes.DtcLENorm import DtcLENorm
from OTLModel.Datatypes.DtcTrottoirbandVorm import DtcTrottoirbandVorm
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLETrottoirbandWatergreppelType import KlLETrottoirbandWatergreppelType


# Generated with OTLClassCreator. To modify: extend, do not edit
class TrottoirbandWatergreppelStd(GestandaardiseerdeKantopsluiting):
    """Gestandaardiseerde kantopsluiting, die een trottoirband en een watergreppel combineert in een geheel."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandWatergreppelStd"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.norm = DtcLENorm()
        """De gestandaardiseerde trottoirband_watergreppel volgens aangeduide norm."""
        self.norm.naam = "norm"
        self.norm.label = "norm"
        self.norm.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandWatergreppelStd.norm"
        self.norm.definition = "De gestandaardiseerde trottoirband_watergreppel volgens aangeduide norm."
        self.norm.constraints = ""
        self.norm.usagenote = ""
        self.norm.deprecated_version = ""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlLETrottoirbandWatergreppelType(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandWatergreppelStd.type",
                                    definition="Het type van gestandaardiseerde trottoirband_watergreppel.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type van gestandaardiseerde trottoirband_watergreppel."""

        self.vorm = DtcTrottoirbandVorm()
        """De vorm van de gestandaardiseerde trottoirband_watergreppel."""
        self.vorm.naam = "vorm"
        self.vorm.label = "vorm"
        self.vorm.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandWatergreppelStd.vorm"
        self.vorm.definition = "De vorm van de gestandaardiseerde trottoirband_watergreppel."
        self.vorm.constraints = ""
        self.vorm.usagenote = ""
        self.vorm.deprecated_version = ""
