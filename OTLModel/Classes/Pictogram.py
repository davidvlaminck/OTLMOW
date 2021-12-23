from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Classes.BevestigingGC import BevestigingGC
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlPictogramSymbool import KlPictogramSymbool
from OTLModel.Datatypes.KwantWrdInMinuut import KwantWrdInMinuut
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator
class Pictogram(AIMObject, BevestigingGC):
    """Een bord dat een symbool of afbeelding bevat dat de plaats inneemt van een tekst."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pictogram"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        BevestigingGC.__init__(self)
        self.nalichtingstijd = KwantWrdInMinuut()
        """De tijd dat het opgeslagen licht (bij bv. fosforen) in een andere lichtfrequentie (met minder energie) weer wordt uitgezonden."""
        self.nalichtingstijd.naam = "nalichtingstijd"
        self.nalichtingstijd.label = "nalichtingstijd"
        self.nalichtingstijd.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pictogram.nalichtingstijd"
        self.nalichtingstijd.definition = "De tijd dat het opgeslagen licht (bij bv. fosforen) in een andere lichtfrequentie (met minder energie) weer wordt uitgezonden."
        self.nalichtingstijd.constraints = ""
        self.nalichtingstijd.usagenote = ""
        self.nalichtingstijd.deprecated_version = ""

        self.opschrift = StringField(naam="opschrift",
                                     label="opschrift",
                                     uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pictogram.opschrift",
                                     definition="Eventueel begeleidende tekst bij het symbool.",
                                     constraints="",
                                     usagenote="",
                                     deprecated_version="")
        """Eventueel begeleidende tekst bij het symbool."""

        self.symbool = KeuzelijstField(naam="symbool",
                                       label="symbool",
                                       lijst=KlPictogramSymbool(),
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pictogram.symbool",
                                       definition="Het symbool op het pictogram.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Het symbool op het pictogram."""
