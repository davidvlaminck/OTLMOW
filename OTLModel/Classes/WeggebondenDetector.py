from OTLModel.Classes.Detectie import Detectie
from OTLModel.Classes.FirmwareObject import FirmwareObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlWeggebondendetectorDetectieprincipe import KlWeggebondendetectorDetectieprincipe
from OTLModel.Datatypes.KlWeggebondendetectorMerk import KlWeggebondendetectorMerk
from OTLModel.Datatypes.KlWeggebondendetectorModelnaam import KlWeggebondendetectorModelnaam


# Generated with OTLClassCreator
class WeggebondenDetector(Detectie, FirmwareObject):
    """Weggebonden detectoren zijn draadloze in het wegdek geïntegreerde radars of magnetische inductiesensoren. Ze zitten ingebed in een cilinder, die geplaatst wordt in het wegdek en die draadloos communiceert met een access point die met de verkeersregelaar verbonden is"""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WeggebondenDetector"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Detectie.__init__(self)
        FirmwareObject.__init__(self)
        self.detectieprincipe = KeuzelijstField(naam="detectieprincipe",
                                                label="detectieprincipe",
                                                lijst=KlWeggebondendetectorDetectieprincipe(),
                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WeggebondenDetector.detectieprincipe",
                                                definition="Het detectieprincipe geeft aan hoe de weggebonden detector voertuigen detecteert, bv. door gebruik te maken van inductie of doppler.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        """Het detectieprincipe geeft aan hoe de weggebonden detector voertuigen detecteert, bv. door gebruik te maken van inductie of doppler."""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlWeggebondendetectorMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WeggebondenDetector.merk",
                                    definition="Merknaam van een weggebonden detector.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Merknaam van een weggebonden detector."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlWeggebondendetectorModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WeggebondenDetector.modelnaam",
                                         definition="De modelnaam van een weggebonden detector.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van een weggebonden detector."""
