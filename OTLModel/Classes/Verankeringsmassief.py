# coding=utf-8
from OTLModel.Classes.Betonfundering import Betonfundering
from OTLModel.Classes.KlassiekeFundering import KlassiekeFundering
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verankeringsmassief(Betonfundering, KlassiekeFundering):
    """Een fundering waarin ankers zijn aangebracht en die zorgen voor bevestiging en stabilisatie van een object."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verankeringsmassief"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Betonfundering.__init__(self)
        KlassiekeFundering.__init__(self)

        self.isAfgedektMetBitumen = BooleanField(naam="isAfgedektMetBitumen",
                                                 label="is afgedekt met bitumen",
                                                 objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verankeringsmassief.isAfgedektMetBitumen",
                                                 definition="Geeft aan of de fundering afgedekt is met een waterbestendige laag die regenwater en vuil wegvoert van de fundering.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        """Geeft aan of de fundering afgedekt is met een waterbestendige laag die regenwater en vuil wegvoert van de fundering."""

        self.volume = KwantWrdInKubiekeMeter()
        """Het volume in kubieke meter van het verankeringsmassief."""
        self.volume.naam = "volume"
        self.volume.label = "volume"
        self.volume.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verankeringsmassief.volume"
        self.volume.definition = "Het volume in kubieke meter van het verankeringsmassief."
        self.volume.constraints = ""
        self.volume.usagenote = ""
        self.volume.deprecated_version = ""
