# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.VegetatieElement import VegetatieElement
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcAanlegBoomvorm import DtcAanlegBoomvorm
from OTLModel.Datatypes.KlBoomGroeifase import KlBoomGroeifase
from OTLModel.Datatypes.KlBoomspiegelInvulling import KlBoomspiegelInvulling
from OTLModel.Datatypes.KlEindbeeldOpgaandeBoom import KlEindbeeldOpgaandeBoom
from OTLModel.Datatypes.KlKlassePlantjaar import KlKlassePlantjaar
from OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter
from OTLModel.Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Boom(VegetatieElement, AttributeInfo):
    """Een opgaande boom is een boom waarvan de vorm van de kruin overeenkomt met zijn natuurlijke, soortgebonden habitus. Opgaande bomen kunnen een hoge, lage, brede, smalle of een afwijkende groeivorm hebben, zoals zuil- en treurvormen. De boom kan zich op volstrekt natuurlijke wijze uitgezaaid hebben en zijn groeivorm kan bepaald zijn door de natuurlijke groeiomstandigheden (bv. natuurlijke snoei). Ontstond de boom in kunstmatige omstandigheden, dan is de groeivorm bepaald door de jeugdsnoei in de kwekerij en is het eindbeeld van de boom bepaald door de begeleidingssnoei of vormsnoei die wordt uitgevoerd vanaf het planten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        VegetatieElement.__init__(self)

        self._aanleg = OTLAttribuut(field=DtcAanlegBoomvorm,
                                    naam='aanleg',
                                    label='aanleg',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom.aanleg',
                                    definition='De manier van aanplanten van individuele bomen.')

        self._boomspiegel = OTLAttribuut(field=KlBoomspiegelInvulling,
                                         naam='boomspiegel',
                                         label='boomspiegel',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom.boomspiegel',
                                         kardinaliteit_max='*',
                                         definition='Het stuk grond rondom de stam van een boom. Dit is in de ideale situatie minstens zo groot is als de kruin van de boom.')

        self._boomverankeringszone = OTLAttribuut(field=KwantWrdInMeter,
                                                  naam='boomverankeringszone',
                                                  label='boomverankeringszone',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom.boomverankeringszone',
                                                  definition='De straal van de cirkelvormige ruimte waarbinnen de wortels zich bevinden die instaan voor de stabiliteit van de boom uitgedrukt in meter.')

        self._doorwortelbaarVolume = OTLAttribuut(field=KwantWrdInKubiekeMeter,
                                                  naam='doorwortelbaarVolume',
                                                  label='doorwortelbaar volume',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom.doorwortelbaarVolume',
                                                  definition='Het bodemvolume met voldoende mineralen, water en zuurstof die bereikbaar zijn voor een boom om erin te wortelen.')

        self._eindbeeld = OTLAttribuut(field=KlEindbeeldOpgaandeBoom,
                                       naam='eindbeeld',
                                       label='eindbeeld',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom.eindbeeld',
                                       definition='Het nagestreefde beeld van de volgroeide boom of struik op deze specifieke standplaats.')

        self._geschatteKlassePlantjaar = OTLAttribuut(field=KlKlassePlantjaar,
                                                      naam='geschatteKlassePlantjaar',
                                                      label='geschatte klasse plantjaar',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom.geschatteKlassePlantjaar',
                                                      definition='Dit attribuut geeft een interval weer van 20 jaar waarin de boom geplant werd.')

        self._groeifase = OTLAttribuut(field=KlBoomGroeifase,
                                       naam='groeifase',
                                       label='groeifase',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom.groeifase',
                                       definition='Fase van beheer volgens de verschillende levensfases van de boom.')

        self._heeftBoomrooster = OTLAttribuut(field=BooleanField,
                                              naam='heeftBoomrooster',
                                              label='heeft boomrooster',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom.heeftBoomrooster',
                                              definition='Duidt aan of een horizontale structuur aanwezig is die zorgt voor een adequate bescherming van bomen tegen betreding van de boomspiegel door voetgangers of verkeer.')

        self._heeftLuchtleiding = OTLAttribuut(field=BooleanField,
                                               naam='heeftLuchtleiding',
                                               label='heeft luchtleiding',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom.heeftLuchtleiding',
                                               definition='Bepaling of een bovengrondse nutsleiding aanwezig is die in conflict kan komen met de boom.')

        self._isVerplant = OTLAttribuut(field=BooleanField,
                                        naam='isVerplant',
                                        label='is verplant',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom.isVerplant',
                                        definition='Aanduiding of de opgaande boom al dan niet van locatie veranderd is na een eerste aanplant binnen het openbaar domein.')

        self._kroonDiameter = OTLAttribuut(field=KwantWrdInMeter,
                                           naam='kroonDiameter',
                                           label='kroon diameter',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom.kroonDiameter',
                                           definition='Diameter van de kroonprojectie in meter.')

        self._takvrijeStamlengte = OTLAttribuut(field=KwantWrdInMeter,
                                                naam='takvrijeStamlengte',
                                                label='takvrije stamlengte',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom.takvrijeStamlengte',
                                                definition='Tot aan de hoogte van de gewenste takvrije stamlengte wordt de boom zodanig gesnoeid dat er één doorgaande stam is.')

        self._totaleBoombeschermingszone = OTLAttribuut(field=KwantWrdInCentimeter,
                                                        naam='totaleBoombeschermingszone',
                                                        label='totale boombeschermingszone',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom.totaleBoombeschermingszone',
                                                        definition='De straal van de cirkelvormige ruimte rond de boom waar maatregelen genomen worden om de boom te beschermen tijdens projecten of manifestaties uitgedrukt in centimeters.
')

        self._vrijeDoorrijhoogte = OTLAttribuut(field=KwantWrdInMeter,
                                                naam='vrijeDoorrijhoogte',
                                                label='vrije doorrijhoogte',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom.vrijeDoorrijhoogte',
                                                definition='Vrij te houden hoogte in meter, voor het doorrijden van verkeer toe te laten.')

    @property
    def aanleg(self):
        """De manier van aanplanten van individuele bomen."""
        return self._aanleg.waarde

    @aanleg.setter
    def aanleg(self, value):
        self._aanleg.set_waarde(value, owner=self)

    @property
    def boomspiegel(self):
        """Het stuk grond rondom de stam van een boom. Dit is in de ideale situatie minstens zo groot is als de kruin van de boom."""
        return self._boomspiegel.waarde

    @boomspiegel.setter
    def boomspiegel(self, value):
        self._boomspiegel.set_waarde(value, owner=self)

    @property
    def boomverankeringszone(self):
        """De straal van de cirkelvormige ruimte waarbinnen de wortels zich bevinden die instaan voor de stabiliteit van de boom uitgedrukt in meter."""
        return self._boomverankeringszone.waarde

    @boomverankeringszone.setter
    def boomverankeringszone(self, value):
        self._boomverankeringszone.set_waarde(value, owner=self)

    @property
    def doorwortelbaarVolume(self):
        """Het bodemvolume met voldoende mineralen, water en zuurstof die bereikbaar zijn voor een boom om erin te wortelen."""
        return self._doorwortelbaarVolume.waarde

    @doorwortelbaarVolume.setter
    def doorwortelbaarVolume(self, value):
        self._doorwortelbaarVolume.set_waarde(value, owner=self)

    @property
    def eindbeeld(self):
        """Het nagestreefde beeld van de volgroeide boom of struik op deze specifieke standplaats."""
        return self._eindbeeld.waarde

    @eindbeeld.setter
    def eindbeeld(self, value):
        self._eindbeeld.set_waarde(value, owner=self)

    @property
    def geschatteKlassePlantjaar(self):
        """Dit attribuut geeft een interval weer van 20 jaar waarin de boom geplant werd."""
        return self._geschatteKlassePlantjaar.waarde

    @geschatteKlassePlantjaar.setter
    def geschatteKlassePlantjaar(self, value):
        self._geschatteKlassePlantjaar.set_waarde(value, owner=self)

    @property
    def groeifase(self):
        """Fase van beheer volgens de verschillende levensfases van de boom."""
        return self._groeifase.waarde

    @groeifase.setter
    def groeifase(self, value):
        self._groeifase.set_waarde(value, owner=self)

    @property
    def heeftBoomrooster(self):
        """Duidt aan of een horizontale structuur aanwezig is die zorgt voor een adequate bescherming van bomen tegen betreding van de boomspiegel door voetgangers of verkeer."""
        return self._heeftBoomrooster.waarde

    @heeftBoomrooster.setter
    def heeftBoomrooster(self, value):
        self._heeftBoomrooster.set_waarde(value, owner=self)

    @property
    def heeftLuchtleiding(self):
        """Bepaling of een bovengrondse nutsleiding aanwezig is die in conflict kan komen met de boom."""
        return self._heeftLuchtleiding.waarde

    @heeftLuchtleiding.setter
    def heeftLuchtleiding(self, value):
        self._heeftLuchtleiding.set_waarde(value, owner=self)

    @property
    def isVerplant(self):
        """Aanduiding of de opgaande boom al dan niet van locatie veranderd is na een eerste aanplant binnen het openbaar domein."""
        return self._isVerplant.waarde

    @isVerplant.setter
    def isVerplant(self, value):
        self._isVerplant.set_waarde(value, owner=self)

    @property
    def kroonDiameter(self):
        """Diameter van de kroonprojectie in meter."""
        return self._kroonDiameter.waarde

    @kroonDiameter.setter
    def kroonDiameter(self, value):
        self._kroonDiameter.set_waarde(value, owner=self)

    @property
    def takvrijeStamlengte(self):
        """Tot aan de hoogte van de gewenste takvrije stamlengte wordt de boom zodanig gesnoeid dat er één doorgaande stam is."""
        return self._takvrijeStamlengte.waarde

    @takvrijeStamlengte.setter
    def takvrijeStamlengte(self, value):
        self._takvrijeStamlengte.set_waarde(value, owner=self)

    @property
    def totaleBoombeschermingszone(self):
        """De straal van de cirkelvormige ruimte rond de boom waar maatregelen genomen worden om de boom te beschermen tijdens projecten of manifestaties uitgedrukt in centimeters.
"""
        return self._totaleBoombeschermingszone.waarde

    @totaleBoombeschermingszone.setter
    def totaleBoombeschermingszone(self, value):
        self._totaleBoombeschermingszone.set_waarde(value, owner=self)

    @property
    def vrijeDoorrijhoogte(self):
        """Vrij te houden hoogte in meter, voor het doorrijden van verkeer toe te laten."""
        return self._vrijeDoorrijhoogte.waarde

    @vrijeDoorrijhoogte.setter
    def vrijeDoorrijhoogte(self, value):
        self._vrijeDoorrijhoogte.set_waarde(value, owner=self)
