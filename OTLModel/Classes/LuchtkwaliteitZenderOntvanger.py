# coding=utf-8
from OTLModel.Classes.Luchtkwaliteittoestel import Luchtkwaliteittoestel
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlAlgIngressProtectionCode import KlAlgIngressProtectionCode


# Generated with OTLClassCreator. To modify: extend, do not edit
class LuchtkwaliteitZenderOntvanger(Luchtkwaliteittoestel):
    """Onderdeel van de luchtkwaliteitsensor dat het signaal uitstuurt en ontvangt op basis waarvan de luchtkwaliteit gemeten wordt."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LuchtkwaliteitZenderOntvanger"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.ipKlasse = KeuzelijstField(naam="ipKlasse",
                                        label="ingress protection klasse",
                                        lijst=KlAlgIngressProtectionCode(),
                                        objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LuchtkwaliteitZenderOntvanger.ipKlasse",
                                        definition="De IP-codering als een aanduiding voor de mate van beveiliging van de constructie van elektrische of elektronische apparatuur tegen eigen schade door gebruik in \"vijandige omgevingen\" en tegen eventueel gevaar voor de gebruiker volgens IEC 60529.",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """De IP-codering als een aanduiding voor de mate van beveiliging van de constructie van elektrische of elektronische apparatuur tegen eigen schade door gebruik in \"vijandige omgevingen\" en tegen eventueel gevaar voor de gebruiker volgens IEC 60529."""

        self.isBeschermd = BooleanField(naam="isBeschermd",
                                        label="is beschermd",
                                        objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LuchtkwaliteitZenderOntvanger.isBeschermd",
                                        definition="Geeft aan of het toestel beschermd wordt tegen aanrijdingen of niet.",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """Geeft aan of het toestel beschermd wordt tegen aanrijdingen of niet."""

        self.meetCO = BooleanField(naam="meetCO",
                                   label="meet CO",
                                   objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LuchtkwaliteitZenderOntvanger.meetCO",
                                   definition="Geeft aan of het meettoestel CO in de lucht meet of niet.",
                                   constraints="",
                                   usagenote="",
                                   deprecated_version="")
        """Geeft aan of het meettoestel CO in de lucht meet of niet."""

        self.meetNoX = BooleanField(naam="meetNoX",
                                    label="meet NOx",
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LuchtkwaliteitZenderOntvanger.meetNoX",
                                    definition="Geeft aan of het meettoestel NOx in de lucht meet of niet.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Geeft aan of het meettoestel NOx in de lucht meet of niet."""

        self.meetTemperatuur = BooleanField(naam="meetTemperatuur",
                                            label="meet temperatuur",
                                            objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LuchtkwaliteitZenderOntvanger.meetTemperatuur",
                                            definition="Geeft aan of het meettoestel de omgevingstemperatuur meet of niet.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Geeft aan of het meettoestel de omgevingstemperatuur meet of niet."""

        self.meetZicht = BooleanField(naam="meetZicht",
                                      label="meet zicht",
                                      objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LuchtkwaliteitZenderOntvanger.meetZicht",
                                      definition="Geeft aan of het meettoestel zichtbaarheid meet of niet.",
                                      constraints="",
                                      usagenote="",
                                      deprecated_version="")
        """Geeft aan of het meettoestel zichtbaarheid meet of niet."""
