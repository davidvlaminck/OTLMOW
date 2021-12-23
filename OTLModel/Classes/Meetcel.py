from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlMeetcelNauwkeurigheidsklasse import KlMeetcelNauwkeurigheidsklasse
from OTLModel.Datatypes.KlMeetcelNauwkeurigheidsvermogen import KlMeetcelNauwkeurigheidsvermogen
from OTLModel.Datatypes.KlMeetcelVeiligheidsfactor import KlMeetcelVeiligheidsfactor
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator
class Meetcel(AIMNaamObject):
    """Een cel voorzien met uitrusting voor het meten van het energieverbruik aan de hoogspanningszijde van de transformator."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetcel"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.nauwkeurigheidsklasse = KeuzelijstField(naam="nauwkeurigheidsklasse",
                                                     label="nauwkeurigheidsklasse",
                                                     lijst=KlMeetcelNauwkeurigheidsklasse(),
                                                     uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetcel.nauwkeurigheidsklasse",
                                                     definition="Nauwkeurigheidsklasse van de meetcel (vb 0,2; 0,2s; 0,5; ...).",
                                                     constraints="",
                                                     usagenote="",
                                                     deprecated_version="")
        """Nauwkeurigheidsklasse van de meetcel (vb 0,2; 0,2s; 0,5; ...)."""

        self.nauwkeurigheidsvermogen = KeuzelijstField(naam="nauwkeurigheidsvermogen",
                                                       label="nauwkeurigheidsvermogen",
                                                       lijst=KlMeetcelNauwkeurigheidsvermogen(),
                                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetcel.nauwkeurigheidsvermogen",
                                                       definition="Nauwkeurigheidsvermogen van de meetcel (vb 5;15).",
                                                       constraints="",
                                                       usagenote="",
                                                       deprecated_version="")
        """Nauwkeurigheidsvermogen van de meetcel (vb 5;15)."""

        self.transformatieverhouding = StringField(naam="transformatieverhouding",
                                                   label="transformatieverhouding",
                                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetcel.transformatieverhouding",
                                                   definition="Verhouding van de transformatie (vb 25/5;50/5; (5500/v3)/( 110/v3);...).",
                                                   constraints="",
                                                   usagenote="",
                                                   deprecated_version="")
        """Verhouding van de transformatie (vb 25/5;50/5; (5500/v3)/( 110/v3);...)."""

        self.veiligheidsfactor = KeuzelijstField(naam="veiligheidsfactor",
                                                 label="veiligheidsfactor",
                                                 lijst=KlMeetcelVeiligheidsfactor(),
                                                 uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetcel.veiligheidsfactor",
                                                 definition="Verhouding tussen de toegekende primaire limietstroom van de meetcel en de toegekende primaire stroom.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        """Verhouding tussen de toegekende primaire limietstroom van de meetcel en de toegekende primaire stroom."""
