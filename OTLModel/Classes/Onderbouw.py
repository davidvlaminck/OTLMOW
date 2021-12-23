from OTLModel.Classes.LaagDikte import LaagDikte
from OTLModel.Classes.Laag import Laag
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcKrimpvoeg import DtcKrimpvoeg
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlOnderbouwType import KlOnderbouwType
from OTLModel.Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter


# Generated with OTLClassCreator
class Onderbouw(LaagDikte, Laag):
    """Gedeelte van het baanlichaam dat tussen het baanbed en de verharding ligt. Deze omvat onderfundering, fundering en de straatlaag."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        LaagDikte.__init__(self)
        Laag.__init__(self)
        self.isHerstel = BooleanField(naam="isHerstel",
                                      label="is herstel",
                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw.isHerstel",
                                      definition="Aanduiding of de onderbouw laag is of wordt hersteld.",
                                      constraints="",
                                      usagenote="",
                                      deprecated_version="")
        """Aanduiding of de onderbouw laag is of wordt hersteld."""

        self.krimpvoegen = DtcKrimpvoeg()
        """Een gedeeltelijke insnijding in een constructiedeel die uitzetting en krimp in de constructie toelaat."""
        self.krimpvoegen.naam = "krimpvoegen"
        self.krimpvoegen.label = "Krimpvoegen"
        self.krimpvoegen.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw.krimpvoegen"
        self.krimpvoegen.definition = "Een gedeeltelijke insnijding in een constructiedeel die uitzetting en krimp in de constructie toelaat."
        self.krimpvoegen.constraints = ""
        self.krimpvoegen.usagenote = ""
        self.krimpvoegen.deprecated_version = ""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlOnderbouwType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw.type",
                                    definition="Het type van onderbouw.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type van onderbouw."""

        self.volume = KwantWrdInKubiekeMeter()
        """Het volume van onderbouw in kubieke meter."""
        self.volume.naam = "volume"
        self.volume.label = "volume"
        self.volume.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw.volume"
        self.volume.definition = "Het volume van onderbouw in kubieke meter."
        self.volume.constraints = ""
        self.volume.usagenote = ""
        self.volume.deprecated_version = ""
