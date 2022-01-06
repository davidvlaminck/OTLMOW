# coding=utf-8
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlIOBitSnelheid import KlIOBitSnelheid
from OTLModel.Datatypes.KlIOKaartMerk import KlIOKaartMerk
from OTLModel.Datatypes.KlIOKaartModelnaam import KlIOKaartModelnaam
from OTLModel.Datatypes.KlIORichting import KlIORichting
from OTLModel.Datatypes.KlIOSignaaltype import KlIOSignaaltype
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class IOKaart(AIMObject):
    """Een kaart of module die gebruikt wordt voor de ingang of uitgang van een verwerkingseenheid (bv. een PLC). Op de IO-kaart worden perifere toestellen en sensoren aangesloten."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.bitsnelheid = KeuzelijstField(naam="bitsnelheid",
                                           label="bitsnelheid",
                                           lijst=KlIOBitSnelheid(),
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart.bitsnelheid",
                                           definition="De snelheid (hoeveel bits per seconde) waarmee data doorgestuurd kan worden.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """De snelheid (hoeveel bits per seconde) waarmee data doorgestuurd kan worden."""

        self.firmwareversie = StringField(naam="firmwareversie",
                                          label="firmwareversie",
                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart.firmwareversie",
                                          definition="Versie van de firmware.",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        """Versie van de firmware."""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlIOKaartMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart.merk",
                                    definition="Het merk van de IO-kaart.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van de IO-kaart."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlIOKaartModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart.modelnaam",
                                         definition="De modelnaam van de IO-kaart.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van de IO-kaart."""

        self.poortadres = StringField(naam="poortadres",
                                      label="poortadres",
                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart.poortadres",
                                      definition="Het IO-kaart poortadres wordt gebruikt om data uit te wisselen met een perifere component. Elke component krijgt een uniek poortadres toegekend, dit adres is een hexadecimaal getal.",
                                      constraints="",
                                      usagenote="",
                                      deprecated_version="")
        """Het IO-kaart poortadres wordt gebruikt om data uit te wisselen met een perifere component. Elke component krijgt een uniek poortadres toegekend, dit adres is een hexadecimaal getal."""

        self.richting = KeuzelijstField(naam="richting",
                                        label="richting",
                                        lijst=KlIORichting(),
                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart.richting",
                                        definition="Geeft aan of de IO-kaart dient voor input of output.",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """Geeft aan of de IO-kaart dient voor input of output."""

        self.signaalType = KeuzelijstField(naam="signaalType",
                                           label="signaalType",
                                           lijst=KlIOSignaaltype(),
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart.signaalType",
                                           definition="Geeft aan of de IO-kaart werkt met een digitaal of met een analoog signaal.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """Geeft aan of de IO-kaart werkt met een digitaal of met een analoog signaal."""
