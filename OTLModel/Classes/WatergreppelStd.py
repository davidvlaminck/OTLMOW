# coding=utf-8
from OTLModel.Classes.GestandaardiseerdeKantopsluiting import GestandaardiseerdeKantopsluiting
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcLENorm import DtcLENorm
from OTLModel.Datatypes.DtcTrottoirbandVorm import DtcTrottoirbandVorm
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLEWatergreppelType import KlLEWatergreppelType


# Generated with OTLClassCreator. To modify: extend, do not edit
class WatergreppelStd(GestandaardiseerdeKantopsluiting):
    """Gestandaardiseerde kantopsluiting, bestemd om water van de verharding op te vangen en af te voeren."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WatergreppelStd"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.isVerholen = BooleanField(naam="isVerholen",
                                       label="is verholen",
                                       objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WatergreppelStd.isVerholen",
                                       definition="Aanduiding of de watergreppel verholen is. Verholen goten hebben een kleine sleufopening en een grote afvoercapaciteit.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Aanduiding of de watergreppel verholen is. Verholen goten hebben een kleine sleufopening en een grote afvoercapaciteit."""

        self.norm = DtcLENorm()
        """De gestandaardiseerde watergreppel volgens aangeduide norm."""
        self.norm.naam = "norm"
        self.norm.label = "norm"
        self.norm.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WatergreppelStd.norm"
        self.norm.definition = "De gestandaardiseerde watergreppel volgens aangeduide norm."
        self.norm.constraints = ""
        self.norm.usagenote = ""
        self.norm.deprecated_version = ""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlLEWatergreppelType(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WatergreppelStd.type",
                                    definition="Het type van gestandaardiseerde watergreppel.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type van gestandaardiseerde watergreppel."""

        self.vorm = DtcTrottoirbandVorm()
        """De vorm van de watergreppel."""
        self.vorm.naam = "vorm"
        self.vorm.label = "vorm"
        self.vorm.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WatergreppelStd.vorm"
        self.vorm.definition = "De vorm van de watergreppel."
        self.vorm.constraints = ""
        self.vorm.usagenote = ""
        self.vorm.deprecated_version = ""
