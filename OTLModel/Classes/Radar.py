from OTLModel.Classes.NietWeggebondenDetectie import NietWeggebondenDetectie
from OTLModel.Classes.TypeWeggebruiker import TypeWeggebruiker
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlRadarMerk import KlRadarMerk
from OTLModel.Datatypes.KlRadarModelnaam import KlRadarModelnaam


# Generated with OTLClassCreator
class Radar(NietWeggebondenDetectie, TypeWeggebruiker):
    """Een detector die werkt volgens het Doppler-effect. De detectie gebeurt met behulp van een microgolfbundel die in de richting van het wegdek wordt uitgezonden. Gebruikt voor het detecteren van voertuigen, voetgangers en fietsers."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Radar"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        NietWeggebondenDetectie.__init__(self)
        TypeWeggebruiker.__init__(self)
        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlRadarMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Radar.merk",
                                    definition="Merknaam van de radar.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Merknaam van de radar."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlRadarModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Radar.modelnaam",
                                         definition="De modelnaam van de radar.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van de radar."""
