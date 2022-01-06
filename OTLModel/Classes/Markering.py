# coding=utf-8
from abc import abstractmethod
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Classes.Signalisatie import Signalisatie
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcMarkeringOpvatting import DtcMarkeringOpvatting
from OTLModel.Datatypes.DtcProductidentificatiecode import DtcProductidentificatiecode
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlKleurMarkering import KlKleurMarkering
from OTLModel.Datatypes.KlMarkeringSoort import KlMarkeringSoort


# Generated with OTLClassCreator. To modify: extend, do not edit
class Markering(AIMObject, Signalisatie):
    """Abstracte als noemer voor de verschillende types van markeringen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMObject.__init__(self)
        Signalisatie.__init__(self)

        self.isHandwerk = BooleanField(naam="isHandwerk",
                                       label="is handwerk",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering.isHandwerk",
                                       definition="Boolean om te bepalen of de markering machinaal of handmatig is aangebracht.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Boolean om te bepalen of de markering machinaal of handmatig is aangebracht."""

        self.isTijdelijk = BooleanField(naam="isTijdelijk",
                                        label="is tijdelijk",
                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering.isTijdelijk",
                                        definition="Aanduiding of de wegmarkering al dan niet tot de werfsignalisatie behoort.",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """Aanduiding of de wegmarkering al dan niet tot de werfsignalisatie behoort."""

        self.kleur = KeuzelijstField(naam="kleur",
                                     label="kleur",
                                     lijst=KlKleurMarkering(),
                                     uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering.kleur",
                                     definition="De kleur van de gebruikte markering.",
                                     constraints="",
                                     usagenote="",
                                     deprecated_version="")
        """De kleur van de gebruikte markering."""

        self.markeringsoort = KeuzelijstField(naam="markeringsoort",
                                              label="markeringsoort",
                                              lijst=KlMarkeringSoort(),
                                              uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering.markeringsoort",
                                              definition="De soort van markering (verf, thermopast,...).",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        """De soort van markering (verf, thermopast,...)."""

        self.markeringsysteemCopro = DtcProductidentificatiecode()
        """De product informatie van de markering via COPRO codes."""
        self.markeringsysteemCopro.naam = "markeringsysteemCopro"
        self.markeringsysteemCopro.label = "markeringsysteem COPRO"
        self.markeringsysteemCopro.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering.markeringsysteemCopro"
        self.markeringsysteemCopro.definition = "De product informatie van de markering via COPRO codes."
        self.markeringsysteemCopro.constraints = ""
        self.markeringsysteemCopro.usagenote = ""
        self.markeringsysteemCopro.deprecated_version = ""

        self.opvatting = DtcMarkeringOpvatting()
        """De opvatting van de markering, zijnde middelenverbintenis of resultaatsverbintenis met een minimale levensduur."""
        self.opvatting.naam = "opvatting"
        self.opvatting.label = "opvatting"
        self.opvatting.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering.opvatting"
        self.opvatting.definition = "De opvatting van de markering, zijnde middelenverbintenis of resultaatsverbintenis met een minimale levensduur."
        self.opvatting.constraints = ""
        self.opvatting.usagenote = ""
        self.opvatting.deprecated_version = ""
