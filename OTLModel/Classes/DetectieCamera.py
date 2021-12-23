from OTLModel.Classes.NietWeggebondenDetectie import NietWeggebondenDetectie
from OTLModel.Classes.TypeWeggebruiker import TypeWeggebruiker
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlDetectiecameraDetectieprincipe import KlDetectiecameraDetectieprincipe
from OTLModel.Datatypes.KlDetectiecameraMerk import KlDetectiecameraMerk
from OTLModel.Datatypes.KlDetectiecameraModelnaam import KlDetectiecameraModelnaam


# Generated with OTLClassCreator
class DetectieCamera(NietWeggebondenDetectie, TypeWeggebruiker):
    """Deze camera's worden onder andere opgesteld op kruispunten om de aanwezigheid van voertuigen te detecteren. De detectie kan optisch en/of thermografisch gebeuren. """

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DetectieCamera"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        NietWeggebondenDetectie.__init__(self)
        TypeWeggebruiker.__init__(self)
        detectieprincipeField = KeuzelijstField(naam="detectieprincipe",
                                                label="detectieprincipe",
                                                lijst=KlDetectiecameraDetectieprincipe(),
                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DetectieCamera.detectieprincipe",
                                                definition="Geeft aan of de camera optisch en/of thermografisch werkt.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        self.detectieprincipe = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=detectieprincipeField)
        """Geeft aan of de camera optisch en/of thermografisch werkt."""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlDetectiecameraMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DetectieCamera.merk",
                                    definition="Merknaam van de detectiecamera.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Merknaam van de detectiecamera."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlDetectiecameraModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DetectieCamera.modelnaam",
                                         definition="De modelnaam van de detectiecamera.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van de detectiecamera."""
