# coding=utf-8
from OTLModel.Classes.LaagBouwklasse import LaagBouwklasse
from OTLModel.Datatypes.DtcSupplementenCBV import DtcSupplementenCBV
from OTLModel.Datatypes.IntegerField import IntegerField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlCBVAardVerharding import KlCBVAardVerharding
from OTLModel.Datatypes.KlCBVLaagtype import KlCBVLaagtype
from OTLModel.Datatypes.KlCBVOppervlaktebehandeling import KlCBVOppervlaktebehandeling
from OTLModel.Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Cementbetonverharding(LaagBouwklasse):
    """Stijve verharding met of zonder wapening verkregen door cementbeton te spreiden en mechanisch te verdichten."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.aantalAnkerstaven = IntegerField(naam="aantalAnkerstaven",
                                              label="aantal ankerstaven",
                                              objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding.aantalAnkerstaven",
                                              definition="Aantal ankerstaven waarmee de voegen verankerd zijn.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        """Aantal ankerstaven waarmee de voegen verankerd zijn."""

        self.aardVerharding = KeuzelijstField(naam="aardVerharding",
                                              label="aard verharding",
                                              lijst=KlCBVAardVerharding(),
                                              objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding.aardVerharding",
                                              definition="De uitvoeringswijze van de cementbetonverharding.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        """De uitvoeringswijze van de cementbetonverharding."""

        self.krimpvoegFrequentie = KwantWrdInMeter()
        """De afstand tussen de krimpvoegen in meter."""
        self.krimpvoegFrequentie.naam = "krimpvoegFrequentie"
        self.krimpvoegFrequentie.label = "krimpvoeg frequentie"
        self.krimpvoegFrequentie.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding.krimpvoegFrequentie"
        self.krimpvoegFrequentie.definition = "De afstand tussen de krimpvoegen in meter."
        self.krimpvoegFrequentie.constraints = ""
        self.krimpvoegFrequentie.usagenote = ""
        self.krimpvoegFrequentie.deprecated_version = ""

        self.laagtype = KeuzelijstField(naam="laagtype",
                                        label="laagtype",
                                        lijst=KlCBVLaagtype(),
                                        objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding.laagtype",
                                        definition="Het type van de cementbetonverhardingslaag.",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """Het type van de cementbetonverhardingslaag."""

        self.oppervlakbehandeling = KeuzelijstField(naam="oppervlakbehandeling",
                                                    label="oppervlakbehandeling",
                                                    lijst=KlCBVOppervlaktebehandeling(),
                                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding.oppervlakbehandeling",
                                                    definition="Behandeling die wordt toegepast op het oppervlak van een laag, met of zonder toevoeging van materialen, en bestemd is om de eigenschappen van de laag te verbeteren, hetzij bij de uitvoering, hetzij achteraf. ",
                                                    constraints="",
                                                    usagenote="",
                                                    deprecated_version="")
        """Behandeling die wordt toegepast op het oppervlak van een laag, met of zonder toevoeging van materialen, en bestemd is om de eigenschappen van de laag te verbeteren, hetzij bij de uitvoering, hetzij achteraf. """

        self.supplementen = DtcSupplementenCBV()
        """Additionele toevoegingen aan de verharding."""
        self.supplementen.naam = "supplementen"
        self.supplementen.label = "supplementen van de verharding"
        self.supplementen.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding.supplementen"
        self.supplementen.definition = "Additionele toevoegingen aan de verharding."
        self.supplementen.constraints = ""
        self.supplementen.usagenote = ""
        self.supplementen.deprecated_version = ""

        self.volume = KwantWrdInKubiekeMeter()
        """Het volume van cementbetonverharding in kubieke meter."""
        self.volume.naam = "volume"
        self.volume.label = "volume"
        self.volume.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding.volume"
        self.volume.definition = "Het volume van cementbetonverharding in kubieke meter."
        self.volume.constraints = ""
        self.volume.usagenote = ""
        self.volume.deprecated_version = ""
