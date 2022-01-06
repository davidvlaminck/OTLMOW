# coding=utf-8
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLEDDriverMerk import KlLEDDriverMerk
from OTLModel.Datatypes.KlLEDDriverModelnaam import KlLEDDriverModelnaam
from OTLModel.Datatypes.KlLEDDriverProtocol import KlLEDDriverProtocol
from OTLModel.Datatypes.KwantWrdInMilliAmpere import KwantWrdInMilliAmpere
from OTLModel.Datatypes.KwantWrdInWatt import KwantWrdInWatt


# Generated with OTLClassCreator. To modify: extend, do not edit
class LEDDriver(AIMObject):
    """Een LED-driver is een elektronisch toestel dat de stroomtoevoer naar de LED's dimensioneert om de goede werking te verzekeren. Via de instelparameters van de driver kan uiteindelijk de lichtsterkte van de LED verlichting aangepast worden."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LEDDriver"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.maximaalVermogen = KwantWrdInWatt()
        """Maximaal afgenomen vermogen van de driver en lamp samen (incl. verlies/verbruik van de driver zelf)."""
        self.maximaalVermogen.naam = "maximaalVermogen"
        self.maximaalVermogen.label = "maximaal vermogen"
        self.maximaalVermogen.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LEDDriver.maximaalVermogen"
        self.maximaalVermogen.definition = "Maximaal afgenomen vermogen van de driver en lamp samen (incl. verlies/verbruik van de driver zelf)."
        self.maximaalVermogen.constraints = ""
        self.maximaalVermogen.usagenote = ""
        self.maximaalVermogen.deprecated_version = ""

        self.maximaleAanstuurstroom = KwantWrdInMilliAmpere()
        """Maximale aanstuurstroom die de LED driver kan leveren."""
        self.maximaleAanstuurstroom.naam = "maximaleAanstuurstroom"
        self.maximaleAanstuurstroom.label = "maximale aanstuurstroom"
        self.maximaleAanstuurstroom.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LEDDriver.maximaleAanstuurstroom"
        self.maximaleAanstuurstroom.definition = "Maximale aanstuurstroom die de LED driver kan leveren."
        self.maximaleAanstuurstroom.constraints = ""
        self.maximaleAanstuurstroom.usagenote = ""
        self.maximaleAanstuurstroom.deprecated_version = ""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlLEDDriverMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LEDDriver.merk",
                                    definition="Het merk van de LED-driver.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van de LED-driver."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlLEDDriverModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LEDDriver.modelnaam",
                                         definition="De modelnaam van de LED-driver.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van de LED-driver."""

        self.protocol = KeuzelijstField(naam="protocol",
                                        label="protocol",
                                        lijst=KlLEDDriverProtocol(),
                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LEDDriver.protocol",
                                        definition="Protocol gebruikt door de LED driver voor het aansturen van de LED's.",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """Protocol gebruikt door de LED driver voor het aansturen van de LED's."""
