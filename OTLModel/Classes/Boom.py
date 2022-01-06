# coding=utf-8
from OTLModel.Classes.VegetatieElement import VegetatieElement
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcAanlegBoomvorm import DtcAanlegBoomvorm
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBoomGroeifase import KlBoomGroeifase
from OTLModel.Datatypes.KlBoomspiegelInvulling import KlBoomspiegelInvulling
from OTLModel.Datatypes.KlEindbeeldOpgaandeBoom import KlEindbeeldOpgaandeBoom
from OTLModel.Datatypes.KlKlassePlantjaar import KlKlassePlantjaar
from OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter
from OTLModel.Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Boom(VegetatieElement):
    """Een opgaande boom is een boom waarvan de vorm van de kruin overeenkomt met zijn natuurlijke, soortgebonden habitus. Opgaande bomen kunnen een hoge, lage, brede, smalle of een afwijkende groeivorm hebben, zoals zuil- en treurvormen. De boom kan zich op volstrekt natuurlijke wijze uitgezaaid hebben en zijn groeivorm kan bepaald zijn door de natuurlijke groeiomstandigheden (bv. natuurlijke snoei). Ontstond de boom in kunstmatige omstandigheden, dan is de groeivorm bepaald door de jeugdsnoei in de kwekerij en is het eindbeeld van de boom bepaald door de begeleidingssnoei of vormsnoei die wordt uitgevoerd vanaf het planten."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.aanleg = DtcAanlegBoomvorm()
        """De manier van aanplanten van individuele bomen."""
        self.aanleg.naam = "aanleg"
        self.aanleg.label = "aanleg"
        self.aanleg.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom.aanleg"
        self.aanleg.definition = "De manier van aanplanten van individuele bomen."
        self.aanleg.constraints = ""
        self.aanleg.usagenote = ""
        self.aanleg.deprecated_version = ""

        boomspiegelField = KeuzelijstField(naam="boomspiegel",
                                           label="boomspiegel",
                                           lijst=KlBoomspiegelInvulling(),
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom.boomspiegel",
                                           definition="Het stuk grond rondom de stam van een boom. Dit is in de ideale situatie minstens zo groot is als de kruin van de boom.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        self.boomspiegel = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=boomspiegelField)
        """Het stuk grond rondom de stam van een boom. Dit is in de ideale situatie minstens zo groot is als de kruin van de boom."""

        self.boomverankeringszone = KwantWrdInMeter()
        """De straal van de cirkelvormige ruimte waarbinnen de wortels zich bevinden die instaan voor de stabiliteit van de boom uitgedrukt in meter."""
        self.boomverankeringszone.naam = "boomverankeringszone"
        self.boomverankeringszone.label = "boomverankeringszone"
        self.boomverankeringszone.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom.boomverankeringszone"
        self.boomverankeringszone.definition = "De straal van de cirkelvormige ruimte waarbinnen de wortels zich bevinden die instaan voor de stabiliteit van de boom uitgedrukt in meter."
        self.boomverankeringszone.constraints = ""
        self.boomverankeringszone.usagenote = ""
        self.boomverankeringszone.deprecated_version = ""

        self.doorwortelbaarVolume = KwantWrdInKubiekeMeter()
        """Het bodemvolume met voldoende mineralen, water en zuurstof die bereikbaar zijn voor een boom om erin te wortelen."""
        self.doorwortelbaarVolume.naam = "doorwortelbaarVolume"
        self.doorwortelbaarVolume.label = "doorwortelbaar volume"
        self.doorwortelbaarVolume.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom.doorwortelbaarVolume"
        self.doorwortelbaarVolume.definition = "Het bodemvolume met voldoende mineralen, water en zuurstof die bereikbaar zijn voor een boom om erin te wortelen."
        self.doorwortelbaarVolume.constraints = ""
        self.doorwortelbaarVolume.usagenote = ""
        self.doorwortelbaarVolume.deprecated_version = ""

        self.eindbeeld = KeuzelijstField(naam="eindbeeld",
                                         label="eindbeeld",
                                         lijst=KlEindbeeldOpgaandeBoom(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom.eindbeeld",
                                         definition="Het nagestreefde beeld van de volgroeide boom of struik op deze specifieke standplaats.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Het nagestreefde beeld van de volgroeide boom of struik op deze specifieke standplaats."""

        self.geschatteKlassePlantjaar = KeuzelijstField(naam="geschatteKlassePlantjaar",
                                                        label="geschatte klasse plantjaar",
                                                        lijst=KlKlassePlantjaar(),
                                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom.geschatteKlassePlantjaar",
                                                        definition="Dit attribuut geeft een interval weer van 20 jaar waarin de boom geplant werd.",
                                                        constraints="",
                                                        usagenote="",
                                                        deprecated_version="")
        """Dit attribuut geeft een interval weer van 20 jaar waarin de boom geplant werd."""

        self.groeifase = KeuzelijstField(naam="groeifase",
                                         label="groeifase",
                                         lijst=KlBoomGroeifase(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom.groeifase",
                                         definition="Fase van beheer volgens de verschillende levensfases van de boom.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Fase van beheer volgens de verschillende levensfases van de boom."""

        self.heeftBoomrooster = BooleanField(naam="heeftBoomrooster",
                                             label="heeft boomrooster",
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom.heeftBoomrooster",
                                             definition="Duidt aan of een horizontale structuur aanwezig is die zorgt voor een adequate bescherming van bomen tegen betreding van de boomspiegel door voetgangers of verkeer.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Duidt aan of een horizontale structuur aanwezig is die zorgt voor een adequate bescherming van bomen tegen betreding van de boomspiegel door voetgangers of verkeer."""

        self.heeftLuchtleiding = BooleanField(naam="heeftLuchtleiding",
                                              label="heeft luchtleiding",
                                              uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom.heeftLuchtleiding",
                                              definition="Bepaling of een bovengrondse nutsleiding aanwezig is die in conflict kan komen met de boom.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        """Bepaling of een bovengrondse nutsleiding aanwezig is die in conflict kan komen met de boom."""

        self.isVerplant = BooleanField(naam="isVerplant",
                                       label="is verplant",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom.isVerplant",
                                       definition="Aanduiding of de opgaande boom al dan niet van locatie veranderd is na een eerste aanplant binnen het openbaar domein.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Aanduiding of de opgaande boom al dan niet van locatie veranderd is na een eerste aanplant binnen het openbaar domein."""

        self.kroonDiameter = KwantWrdInMeter()
        """Diameter van de kroonprojectie in meter."""
        self.kroonDiameter.naam = "kroonDiameter"
        self.kroonDiameter.label = "kroon diameter"
        self.kroonDiameter.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom.kroonDiameter"
        self.kroonDiameter.definition = "Diameter van de kroonprojectie in meter."
        self.kroonDiameter.constraints = ""
        self.kroonDiameter.usagenote = ""
        self.kroonDiameter.deprecated_version = ""

        self.takvrijeStamlengte = KwantWrdInMeter()
        """Tot aan de hoogte van de gewenste takvrije stamlengte wordt de boom zodanig gesnoeid dat er één doorgaande stam is."""
        self.takvrijeStamlengte.naam = "takvrijeStamlengte"
        self.takvrijeStamlengte.label = "takvrije stamlengte"
        self.takvrijeStamlengte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom.takvrijeStamlengte"
        self.takvrijeStamlengte.definition = "Tot aan de hoogte van de gewenste takvrije stamlengte wordt de boom zodanig gesnoeid dat er één doorgaande stam is."
        self.takvrijeStamlengte.constraints = ""
        self.takvrijeStamlengte.usagenote = ""
        self.takvrijeStamlengte.deprecated_version = ""

        self.totaleBoombeschermingszone = KwantWrdInCentimeter()
        """De straal van de cirkelvormige ruimte rond de boom waar maatregelen genomen worden om de boom te beschermen tijdens projecten of manifestaties uitgedrukt in centimeters."""
        self.totaleBoombeschermingszone.naam = "totaleBoombeschermingszone"
        self.totaleBoombeschermingszone.label = "totale boombeschermingszone"
        self.totaleBoombeschermingszone.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom.totaleBoombeschermingszone"
        self.totaleBoombeschermingszone.definition = "De straal van de cirkelvormige ruimte rond de boom waar maatregelen genomen worden om de boom te beschermen tijdens projecten of manifestaties uitgedrukt in centimeters."
        self.totaleBoombeschermingszone.constraints = ""
        self.totaleBoombeschermingszone.usagenote = ""
        self.totaleBoombeschermingszone.deprecated_version = ""

        self.vrijeDoorrijhoogte = KwantWrdInMeter()
        """Vrij te houden hoogte in meter, voor het doorrijden van verkeer toe te laten."""
        self.vrijeDoorrijhoogte.naam = "vrijeDoorrijhoogte"
        self.vrijeDoorrijhoogte.label = "vrije doorrijhoogte"
        self.vrijeDoorrijhoogte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom.vrijeDoorrijhoogte"
        self.vrijeDoorrijhoogte.definition = "Vrij te houden hoogte in meter, voor het doorrijden van verkeer toe te laten."
        self.vrijeDoorrijhoogte.constraints = ""
        self.vrijeDoorrijhoogte.usagenote = ""
        self.vrijeDoorrijhoogte.deprecated_version = ""
