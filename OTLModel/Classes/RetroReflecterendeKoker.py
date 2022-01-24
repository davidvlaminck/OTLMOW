# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KlRetroreflecterendeKokerFolieType import KlRetroreflecterendeKokerFolieType


# Generated with OTLClassCreator. To modify: extend, do not edit
class RetroReflecterendeKoker(AIMObject):
    """Een kunststoffen koker bevestigd rond een steun om de zichtbaarheid van verkeerseilanden te verhogen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroReflecterendeKoker'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._folieType = OTLAttribuut(field=KlRetroreflecterendeKokerFolieType,
                                       naam='folieType',
                                       label='folie type',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroReflecterendeKoker.folieType',
                                       definition='Een keuzelijst het folietype van reflecterende koker te bepalen.')

    @property
    def folieType(self):
        """Een keuzelijst het folietype van reflecterende koker te bepalen."""
        return self._folieType.waarde

    @folieType.setter
    def folieType(self, value):
        self._folieType.set_waarde(value, owner=self)
