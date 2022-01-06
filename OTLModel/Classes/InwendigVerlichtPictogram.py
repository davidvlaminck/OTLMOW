from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.DtcAfmetingBxlxhInMm import DtcAfmetingBxlxhInMm
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBinnenverlichtingstoestelSoortLamp import KlBinnenverlichtingstoestelSoortLamp
from OTLModel.Datatypes.KlPictogramSymbool import KlPictogramSymbool
from OTLModel.Datatypes.KwantWrdInMinuut import KwantWrdInMinuut


# Generated with OTLClassCreator. To modify: extend, do not edit
class InwendigVerlichtPictogram(AIMObject):
    """Verlichtingstoestel om de aandacht te vestigen op een pictogram dat erop bevestigd is."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#InwendigVerlichtPictogram"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.afmeting = DtcAfmetingBxlxhInMm()
        """Geeft de buitenafmeting van het toestel mee."""
        self.afmeting.naam = "afmeting"
        self.afmeting.label = "afmeting"
        self.afmeting.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#InwendigVerlichtPictogram.afmeting"
        self.afmeting.definition = "Geeft de buitenafmeting van het toestel mee."
        self.afmeting.constraints = ""
        self.afmeting.usagenote = ""
        self.afmeting.deprecated_version = ""

        self.nalichtingstijd = KwantWrdInMinuut()
        """De tijd tussen het uitschakelen van de interne lichtbron en het volledig duister worden van het toestel."""
        self.nalichtingstijd.naam = "nalichtingstijd"
        self.nalichtingstijd.label = "nalichtingstijd"
        self.nalichtingstijd.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#InwendigVerlichtPictogram.nalichtingstijd"
        self.nalichtingstijd.definition = "De tijd tussen het uitschakelen van de interne lichtbron en het volledig duister worden van het toestel."
        self.nalichtingstijd.constraints = ""
        self.nalichtingstijd.usagenote = ""
        self.nalichtingstijd.deprecated_version = ""

        self.symbool = KeuzelijstField(naam="symbool",
                                       label="symbool",
                                       lijst=KlPictogramSymbool(),
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#InwendigVerlichtPictogram.symbool",
                                       definition="Het symbool afgebeeld op het toestel.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Het symbool afgebeeld op het toestel."""

        self.typeLamp = KeuzelijstField(naam="typeLamp",
                                        label="type lamp",
                                        lijst=KlBinnenverlichtingstoestelSoortLamp(),
                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#InwendigVerlichtPictogram.typeLamp",
                                        definition="Het soort lamp waarmee het toestel verlicht wordt.",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """Het soort lamp waarmee het toestel verlicht wordt."""
