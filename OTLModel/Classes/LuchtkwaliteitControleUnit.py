# coding=utf-8
from OTLModel.Classes.Luchtkwaliteittoestel import Luchtkwaliteittoestel
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlAlgIngressProtectionCode import KlAlgIngressProtectionCode


# Generated with OTLClassCreator. To modify: extend, do not edit
class LuchtkwaliteitControleUnit(Luchtkwaliteittoestel):
    """Onderdeel voor de aansturing en interpretatie van het signaal tussen de LuchtkwaliteitZenderOntvanger en de LuchtkwaliteitSensor."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LuchtkwaliteitControleUnit"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.ipKlasse = KeuzelijstField(naam="ipKlasse",
                                        label="ingress protection klasse",
                                        lijst=KlAlgIngressProtectionCode(),
                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LuchtkwaliteitControleUnit.ipKlasse",
                                        definition="De IP-codering als een aanduiding voor de mate van beveiliging van de constructie van elektrische of elektronische apparatuur tegen eigen schade door gebruik in \"vijandige omgevingen\" en tegen eventueel gevaar voor de gebruiker volgens IEC 60529.",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """De IP-codering als een aanduiding voor de mate van beveiliging van de constructie van elektrische of elektronische apparatuur tegen eigen schade door gebruik in \"vijandige omgevingen\" en tegen eventueel gevaar voor de gebruiker volgens IEC 60529."""
