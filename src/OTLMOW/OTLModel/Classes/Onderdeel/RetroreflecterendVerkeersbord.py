# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Verkeersbord import Verkeersbord
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.DteKleurRAL import DteKleurRAL
from OTLMOW.OTLModel.Datatypes.KlRetroreflecterendVerkeersbordAfwerkingsgraad import KlRetroreflecterendVerkeersbordAfwerkingsgraad
from OTLMOW.OTLModel.Datatypes.KlRetroreflecterendVerkeersbordGrootteorde import KlRetroreflecterendVerkeersbordGrootteorde
from OTLMOW.OTLModel.Datatypes.KlRetroreflecterendVerkeersbordMerk import KlRetroreflecterendVerkeersbordMerk
from OTLMOW.OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class RetroreflecterendVerkeersbord(Verkeersbord, AIMObject, PuntGeometrie):
    """Verkeersbord met op het beeldvlak een tekening en/of tekst die worden weergegeven met een geëigend bekledingsmateriaal."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        Verkeersbord.__init__(self)
        PuntGeometrie.__init__(self)

        self._afwerkingsgraad = OTLAttribuut(field=KlRetroreflecterendVerkeersbordAfwerkingsgraad,
                                             naam='afwerkingsgraad',
                                             label='afwerkingsgraad',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord.afwerkingsgraad',
                                             definition='De afwerkingsgraad van het retroreflecterend verkeersbord, volgens een keuzelijst op basis van SB250.',
                                             owner=self)

        self._grootteorde = OTLAttribuut(field=KlRetroreflecterendVerkeersbordGrootteorde,
                                         naam='grootteorde',
                                         label='grootteorde',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord.grootteorde',
                                         kardinaliteit_min='0',
                                         definition='De classificatie naar grootteorde van het verkeersbord, zoals gedefinieerd in SB250 hoofdstuk 10.',
                                         owner=self)

        self._kleurAchterkant = OTLAttribuut(field=DteKleurRAL,
                                             naam='kleurAchterkant',
                                             label='kleur achterkant',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord.kleurAchterkant',
                                             definition='De kleur van de achterkant van het retroreflecterend verkeersbord.',
                                             owner=self)

        self._merk = OTLAttribuut(field=KlRetroreflecterendVerkeersbordMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord.merk',
                                  usagenote='Te selecteren uit een keuzelijst.',
                                  definition='De merknaam van het verkeersbord; duidt op de leverancier of producent van het verkeersbord.',
                                  owner=self)

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord.oppervlakte',
                                         kardinaliteit_min='0',
                                         definition='De oppervlakte van het beeldvlak van een verkeersbord.',
                                         owner=self)

    @property
    def afwerkingsgraad(self):
        """De afwerkingsgraad van het retroreflecterend verkeersbord, volgens een keuzelijst op basis van SB250."""
        return self._afwerkingsgraad.get_waarde()

    @afwerkingsgraad.setter
    def afwerkingsgraad(self, value):
        self._afwerkingsgraad.set_waarde(value, owner=self)

    @property
    def grootteorde(self):
        """De classificatie naar grootteorde van het verkeersbord, zoals gedefinieerd in SB250 hoofdstuk 10."""
        return self._grootteorde.get_waarde()

    @grootteorde.setter
    def grootteorde(self, value):
        self._grootteorde.set_waarde(value, owner=self)

    @property
    def kleurAchterkant(self):
        """De kleur van de achterkant van het retroreflecterend verkeersbord."""
        return self._kleurAchterkant.get_waarde()

    @kleurAchterkant.setter
    def kleurAchterkant(self, value):
        self._kleurAchterkant.set_waarde(value, owner=self)

    @property
    def merk(self):
        """De merknaam van het verkeersbord; duidt op de leverancier of producent van het verkeersbord."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def oppervlakte(self):
        """De oppervlakte van het beeldvlak van een verkeersbord."""
        return self._oppervlakte.get_waarde()

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)
