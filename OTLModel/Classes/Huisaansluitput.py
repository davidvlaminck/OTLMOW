# coding=utf-8
from OTLModel.Classes.Put import Put
from OTLModel.Classes.PutRelatie import PutRelatie
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlHuisaansluitputMateriaal import KlHuisaansluitputMateriaal


# Generated with OTLClassCreator. To modify: extend, do not edit
class Huisaansluitput(Put, PutRelatie):
    """Het constructieonderdeel (putje of T-stuk) dat de verbinding vormt tussen de private riolering en de 
 huisaansluiting."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Huisaansluitput"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Put.__init__(self)
        PutRelatie.__init__(self)

        self.aansluitingsfiche = DtcDocument()
        """De aansluitingsfiche van de huisaansluitput."""
        self.aansluitingsfiche.naam = "aansluitingsfiche"
        self.aansluitingsfiche.label = "aansluitingsfiche"
        self.aansluitingsfiche.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Huisaansluitput.aansluitingsfiche"
        self.aansluitingsfiche.definition = "De aansluitingsfiche van de huisaansluitput."
        self.aansluitingsfiche.constraints = ""
        self.aansluitingsfiche.usagenote = ""
        self.aansluitingsfiche.deprecated_version = ""

        self.heeftStankafsluiter = BooleanField(naam="heeftStankafsluiter",
                                                label="heeft stankafsluiter",
                                                objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Huisaansluitput.heeftStankafsluiter",
                                                definition="Aanduiding of een huisaansluitput een stankafsluiter heeft of niet.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        """Aanduiding of een huisaansluitput een stankafsluiter heeft of niet."""

        self.isInfiltrerend = BooleanField(naam="isInfiltrerend",
                                           label="is infiltrerend",
                                           objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Huisaansluitput.isInfiltrerend",
                                           definition="Wanneer de wanden van het putje poreus zijn (en het putje dus infiltrerend is), kan een deel van het water het water dat in het putje komt rechtstreeks in de grond infiltreren.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """Wanneer de wanden van het putje poreus zijn (en het putje dus infiltrerend is), kan een deel van het water het water dat in het putje komt rechtstreeks in de grond infiltreren."""

        self.materiaal = KeuzelijstField(naam="materiaal",
                                         label="materiaal",
                                         lijst=KlHuisaansluitputMateriaal(),
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Huisaansluitput.materiaal",
                                         definition="Bepaalt het materiaal waaruit de huisaansluitput is vervaardigd.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Bepaalt het materiaal waaruit de huisaansluitput is vervaardigd."""
