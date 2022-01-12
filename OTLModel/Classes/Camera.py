# coding=utf-8
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.DteIPv4Adres import DteIPv4Adres
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlCameraMerk import KlCameraMerk
from OTLModel.Datatypes.KlCameraModelnaam import KlCameraModelnaam
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Camera(AIMNaamObject):
    """Een CCTV-camera, closed-circuit television camera, kortweg camera, produceert beelden of opnames voor bewaking van een regio vanop afstand. Het is een element dat beelden neemt van een locatie en deze doorgeeft naar verschillende partijen om zo de werkelijke situatie te kunnen inschatten vanop afstand. Deze camera kan van het analoge type zijn of digitaal."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.configBestandAid = DtcDocument()
        """Het bestand met de configuratie van de AID component die deel is van de camera."""
        self.configBestandAid.naam = "configBestandAid"
        self.configBestandAid.label = "configuratie bestand AID"
        self.configBestandAid.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera.configBestandAid"
        self.configBestandAid.definition = "Het bestand met de configuratie van de AID component die deel is van de camera."
        self.configBestandAid.constraints = ""
        self.configBestandAid.usagenote = "Enkel in te gebruiken wanneer de camera zelf een AID component bevat (attribuut heeftAid van Camera is 1). Voor camera's met een externe AID module maakt het configuratiebestand deel uit van die aparte AID module. "
        self.configBestandAid.deprecated_version = ""

        self.dnsNaam = StringField(naam="dnsNaam",
                                   label="DNS naam",
                                   objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera.dnsNaam",
                                   definition="De DNSNaam (ook \"volledige domein naam\" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be.",
                                   constraints="",
                                   usagenote="",
                                   deprecated_version="")
        """De DNSNaam (ook \"volledige domein naam\" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be."""

        self.heeftAid = BooleanField(naam="heeftAid",
                                     label="heeft AID",
                                     objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera.heeftAid",
                                     definition="Een AID-camera is een CCTV-camera met geintegreerde AID-module. Deze camera genereert naast een camerabeeld ook metadata ivm wat zich afspeelt op het beeld. Een voorbeeld hiervan is gestopte voertuigen.",
                                     constraints="",
                                     usagenote="",
                                     deprecated_version="")
        """Een AID-camera is een CCTV-camera met geintegreerde AID-module. Deze camera genereert naast een camerabeeld ook metadata ivm wat zich afspeelt op het beeld. Een voorbeeld hiervan is gestopte voertuigen."""

        self.heeftSpitsstrook = BooleanField(naam="heeftSpitsstrook",
                                             label="heeft spitsstrook",
                                             objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera.heeftSpitsstrook",
                                             definition="Locatie-eigenschap van een camera. Dit attribuut geeft aan of de camera ingezet wordt om een spitsstrook te schouwen.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Locatie-eigenschap van een camera. Dit attribuut geeft aan of de camera ingezet wordt om een spitsstrook te schouwen."""

        self.ipAdres = DteIPv4Adres()
        """Het IP-adres van de camera."""
        self.ipAdres.naam = "ipAdres"
        self.ipAdres.label = "ip adres"
        self.ipAdres.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera.ipAdres"
        self.ipAdres.definition = "Het IP-adres van de camera."
        self.ipAdres.constraints = ""
        self.ipAdres.usagenote = ""
        self.ipAdres.deprecated_version = ""

        self.isPtz = BooleanField(naam="isPtz",
                                  label="is PTZ",
                                  objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera.isPtz",
                                  definition="Een PTZ-camera is een CCTV-camera met bijhorend de mogelijkheid om te pannen, tilten en zoomen. Dit vanop afstand met behulp van een verstelbare lens en een motor die in twee assen draaibeweging toelaat.",
                                  constraints="",
                                  usagenote="",
                                  deprecated_version="")
        """Een PTZ-camera is een CCTV-camera met bijhorend de mogelijkheid om te pannen, tilten en zoomen. Dit vanop afstand met behulp van een verstelbare lens en een motor die in twee assen draaibeweging toelaat."""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlCameraMerk(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera.merk",
                                    definition="Het merk van de camera.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van de camera."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlCameraModelnaam(),
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera.modelnaam",
                                         definition="De modelnaam van de camera.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van de camera."""

        self.opstelhoogte = KwantWrdInMeter()
        """De hoogte waarop de camera bevestigd is, gemeten ten opzichte van het maaiveld waarin de draagconstructie voor de camera verankerd is."""
        self.opstelhoogte.naam = "opstelhoogte"
        self.opstelhoogte.label = "opstelhoogte"
        self.opstelhoogte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera.opstelhoogte"
        self.opstelhoogte.definition = "De hoogte waarop de camera bevestigd is, gemeten ten opzichte van het maaiveld waarin de draagconstructie voor de camera verankerd is."
        self.opstelhoogte.constraints = ""
        self.opstelhoogte.usagenote = "De plaats waar de draagconstructie in de grond bevestigd is, bepaalt van waar gemeten wordt voor het bepalen van de opstelhoogte. Wanneer een camera die een brugdek overziet, bevestigd is aan een paal die naast de brug staat, wordt de hoogte gemeten vanaf de basis van de paal en niet vanaf het brugdek. "
        self.opstelhoogte.deprecated_version = ""

        self.technischeFiche = DtcDocument()
        """Technische fiche van dit element met opsplitsing tussen CCTV, AID en PTZ-camera's."""
        self.technischeFiche.naam = "technischeFiche"
        self.technischeFiche.label = "technische fiche"
        self.technischeFiche.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera.technischeFiche"
        self.technischeFiche.definition = "Technische fiche van dit element met opsplitsing tussen CCTV, AID en PTZ-camera's."
        self.technischeFiche.constraints = ""
        self.technischeFiche.usagenote = "Bestanden van het type pdf."
        self.technischeFiche.deprecated_version = ""
