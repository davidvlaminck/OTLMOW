# coding=utf-8
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.IntegerField import IntegerField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlNetwerkMerk import KlNetwerkMerk
from OTLModel.Datatypes.KlNetwerkTechnologie import KlNetwerkTechnologie
from OTLModel.Datatypes.KlNetwerkpoortConfig import KlNetwerkpoortConfig
from OTLModel.Datatypes.KlNetwerkpoortGolflengte import KlNetwerkpoortGolflengte
from OTLModel.Datatypes.KlNetwerkpoortType import KlNetwerkpoortType
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Netwerkpoort(AIMNaamObject):
    """De ingang van het toestel samen met component die erop zit,bv. SFP of XFP."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.beschrijvingFabrikant = StringField(naam="beschrijvingFabrikant",
                                                 label="beschrijving fabrikant",
                                                 uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort.beschrijvingFabrikant",
                                                 definition="Bijkomende specificaties over het apparaat of onderdeel type van de fabrikant.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        """Bijkomende specificaties over het apparaat of onderdeel type van de fabrikant."""

        self.code = StringField(naam="code",
                                label="code",
                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort.code",
                                definition="Bestelcode van dit toestel of onderdeel bij de fabrikant.",
                                constraints="",
                                usagenote="",
                                deprecated_version="")
        """Bestelcode van dit toestel of onderdeel bij de fabrikant."""

        self.config = KeuzelijstField(naam="config",
                                      label="config",
                                      lijst=KlNetwerkpoortConfig(),
                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort.config",
                                      definition="Soort verbinding aangeboden aan de klant.",
                                      constraints="",
                                      usagenote="",
                                      deprecated_version="")
        """Soort verbinding aangeboden aan de klant."""

        self.golflengte = KeuzelijstField(naam="golflengte",
                                          label="golflengte",
                                          lijst=KlNetwerkpoortGolflengte(),
                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort.golflengte",
                                          definition="De golflengte waarop deze poort communiceert.",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        """De golflengte waarop deze poort communiceert."""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlNetwerkMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort.merk",
                                    definition="Merk waarmee de fabrikant de netwerkpoort identificeert.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Merk waarmee de fabrikant de netwerkpoort identificeert."""

        self.nNILANCapaciteit = IntegerField(naam="nNILANCapaciteit",
                                             label="NNI LAN-capaciteit",
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort.nNILANCapaciteit",
                                             definition="Bandbreedte via deze poort, uitgedrukt in Mb/s, enkel van toepassing indien NNI poort.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Bandbreedte via deze poort, uitgedrukt in Mb/s, enkel van toepassing indien NNI poort."""

        self.serienummer = StringField(naam="serienummer",
                                       label="serienummer",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort.serienummer",
                                       definition="Unieke identificatiecode van het toestel, toegekend door de fabrikant.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Unieke identificatiecode van het toestel, toegekend door de fabrikant."""

        self.technologie = KeuzelijstField(naam="technologie",
                                           label="technologie",
                                           lijst=KlNetwerkTechnologie(),
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort.technologie",
                                           definition="Intern gebruikt netwerk protocol.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """Intern gebruikt netwerk protocol."""

        self.type = KeuzelijstField(naam="type",
                                    label="model",
                                    lijst=KlNetwerkpoortType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort.type",
                                    definition="Geeft het soort netwerk interface weer.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Geeft het soort netwerk interface weer."""
