# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.LinkendElement import LinkendElement
from OTLModel.Datatypes.KlAfsluiterType import KlAfsluiterType
from OTLModel.Datatypes.KlTsklepAfsluiterMateriaal import KlTsklepAfsluiterMateriaal
from OTLModel.Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Afsluiter(LinkendElement):
    """Een afsluiter dient om rioolstrengen af te sluiten bij bv. gebreken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluiter'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._actueleHoogte = OTLAttribuut(field=KwantWrdInMillimeter,
                                           naam='actueleHoogte',
                                           label='actuele hoogte',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluiter.actueleHoogte',
                                           definition='De afstand tussen het vloeipeil van de opening en de laagste positie van de schuif.')

        self._breedte = OTLAttribuut(field=KwantWrdInMillimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluiter.breedte',
                                     definition='De afstand tussen de uiterste zijden van de afsluiter in millimeter.')

        self._hoogte = OTLAttribuut(field=KwantWrdInMillimeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluiter.hoogte',
                                    definition='De afstand tussen het hoogste en laagste punt van de afsluiter met uitzondering van de spindel in millimeter.')

        self._materiaal = OTLAttribuut(field=KlTsklepAfsluiterMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluiter.materiaal',
                                       definition='Materiaal waaruit de afsluiter is vervaardigd.')

        self._peil = OTLAttribuut(field=KwantWrdInMeterTAW,
                                  naam='peil',
                                  label='peil',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluiter.peil',
                                  definition='BOK-peil in meter-TAW van de onderkant van de doorlaat van de afsluiter.')

        self._type = OTLAttribuut(field=KlAfsluiterType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluiter.type',
                                  definition='Bepaalt het type van de afsluiter.')

    @property
    def actueleHoogte(self):
        """De afstand tussen het vloeipeil van de opening en de laagste positie van de schuif."""
        return self._actueleHoogte.waarde

    @actueleHoogte.setter
    def actueleHoogte(self, value):
        self._actueleHoogte.set_waarde(value, owner=self)

    @property
    def breedte(self):
        """De afstand tussen de uiterste zijden van de afsluiter in millimeter."""
        return self._breedte.waarde

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def hoogte(self):
        """De afstand tussen het hoogste en laagste punt van de afsluiter met uitzondering van de spindel in millimeter."""
        return self._hoogte.waarde

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self)

    @property
    def materiaal(self):
        """Materiaal waaruit de afsluiter is vervaardigd."""
        return self._materiaal.waarde

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def peil(self):
        """BOK-peil in meter-TAW van de onderkant van de doorlaat van de afsluiter."""
        return self._peil.waarde

    @peil.setter
    def peil(self, value):
        self._peil.set_waarde(value, owner=self)

    @property
    def type(self):
        """Bepaalt het type van de afsluiter."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
