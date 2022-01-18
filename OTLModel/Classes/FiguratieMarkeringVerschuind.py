# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.FiguratieMarkeringToegang import FiguratieMarkeringToegang
from OTLModel.Datatypes.KlFiguratieCodeVerschuind import KlFiguratieCodeVerschuind
from OTLModel.Datatypes.KlFiguratieSoortVerschuind import KlFiguratieSoortVerschuind
from OTLModel.Datatypes.KlFiguratieTypeVerschuind import KlFiguratieTypeVerschuind
from OTLModel.Datatypes.KwantWrdInDecimaleGraden import KwantWrdInDecimaleGraden
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class FiguratieMarkeringVerschuind(FiguratieMarkeringToegang, AttributeInfo):
    """Een schuine markering als figuratie op de weg aangebracht om het verkeer te waarschuwen, informeren of regelen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FiguratieMarkeringVerschuind'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        FiguratieMarkeringToegang.__init__(self)

        self._basisOppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                              naam='basisOppervlakte',
                                              label='basisoppervlakte',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FiguratieMarkeringVerschuind.basisOppervlakte',
                                              definition='De (basis) oppervlakte van de markering zoals beschreven in de algemene omzendbrief.')

        self._code = OTLAttribuut(field=KlFiguratieCodeVerschuind,
                                  naam='code',
                                  label='code',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FiguratieMarkeringVerschuind.code',
                                  definition='De code van de verschuinde figuratie markering.')

        self._hoek = OTLAttribuut(field=KwantWrdInDecimaleGraden,
                                  naam='hoek',
                                  label='hoek',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FiguratieMarkeringVerschuind.hoek',
                                  definition='De hoek van de verschuinde figuratiemarkering in decimale graden.')

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FiguratieMarkeringVerschuind.oppervlakte',
                                         definition='De oppervlakte van de figuratie markering na verschuining.')

        self._soortOmschrijving = OTLAttribuut(field=KlFiguratieSoortVerschuind,
                                               naam='soortOmschrijving',
                                               label='soort omschrijving',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FiguratieMarkeringVerschuind.soortOmschrijving',
                                               definition='De soort en tevens de omschrijving van de verschuinde figuratie markering.')

        self._type = OTLAttribuut(field=KlFiguratieTypeVerschuind,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FiguratieMarkeringVerschuind.type',
                                  definition='Het type van de verschuinde figuratie markering.')

    @property
    def basisOppervlakte(self):
        """De (basis) oppervlakte van de markering zoals beschreven in de algemene omzendbrief."""
        return self._basisOppervlakte.waarde

    @basisOppervlakte.setter
    def basisOppervlakte(self, value):
        self._basisOppervlakte.set_waarde(value, owner=self)

    @property
    def code(self):
        """De code van de verschuinde figuratie markering."""
        return self._code.waarde

    @code.setter
    def code(self, value):
        self._code.set_waarde(value, owner=self)

    @property
    def hoek(self):
        """De hoek van de verschuinde figuratiemarkering in decimale graden."""
        return self._hoek.waarde

    @hoek.setter
    def hoek(self, value):
        self._hoek.set_waarde(value, owner=self)

    @property
    def oppervlakte(self):
        """De oppervlakte van de figuratie markering na verschuining."""
        return self._oppervlakte.waarde

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)

    @property
    def soortOmschrijving(self):
        """De soort en tevens de omschrijving van de verschuinde figuratie markering."""
        return self._soortOmschrijving.waarde

    @soortOmschrijving.setter
    def soortOmschrijving(self, value):
        self._soortOmschrijving.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van de verschuinde figuratie markering."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
