# coding=utf-8
from OTLModel.Classes.VRIDraagconstructie import VRIDraagconstructie
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlDraagconstructieDwarsdoorsnede import KlDraagconstructieDwarsdoorsnede
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Galgpaal(VRIDraagconstructie):
    """De galgpalen zijn bestemd voor het bevestigen van verkeerslichten, signaalborden, wegwijzers boven het wegdek. Bovendien laten zij het bevestigen toe van één of meerdere lantaarns van het type 200 op de paalschacht. De draagwijdte van de arm moet kunnen reiken tot 9 m. De galgpalen beantwoorden aan SB270-51-6.15"""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Galgpaal"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.aantalLiggers = DecimalFloatField(naam="aantalLiggers",
                                               label="aantal liggers",
                                               objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Galgpaal.aantalLiggers",
                                               definition="Het aantal liggers waarmee de arm van de galgpaal is uitgevoerd.",
                                               constraints="",
                                               usagenote="",
                                               deprecated_version="")
        """Het aantal liggers waarmee de arm van de galgpaal is uitgevoerd."""

        self.armlengte = KwantWrdInMeter()
        """Lengte van de arm van een galgpaal in meter."""
        self.armlengte.naam = "armlengte"
        self.armlengte.label = "armlengte"
        self.armlengte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Galgpaal.armlengte"
        self.armlengte.definition = "Lengte van de arm van een galgpaal in meter."
        self.armlengte.constraints = ""
        self.armlengte.usagenote = ""
        self.armlengte.deprecated_version = ""

        self.berekeningsnota = DtcDocument()
        """Een bijlage met daarin de berekeningsnota voor de galgpaal."""
        self.berekeningsnota.naam = "berekeningsnota"
        self.berekeningsnota.label = "berekeningsnota"
        self.berekeningsnota.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Galgpaal.berekeningsnota"
        self.berekeningsnota.definition = "Een bijlage met daarin de berekeningsnota voor de galgpaal."
        self.berekeningsnota.constraints = ""
        self.berekeningsnota.usagenote = ""
        self.berekeningsnota.deprecated_version = ""

        self.dwarsdoorsnede = KeuzelijstField(naam="dwarsdoorsnede",
                                              label="dwarsdoorsnede",
                                              lijst=KlDraagconstructieDwarsdoorsnede(),
                                              objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Galgpaal.dwarsdoorsnede",
                                              definition="De vorm van de dwarsdoorsnede van het opstaande deel van de galgpaal.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        """De vorm van de dwarsdoorsnede van het opstaande deel van de galgpaal."""
