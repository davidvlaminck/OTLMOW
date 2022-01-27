# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.DwarseMarkeringToegang import DwarseMarkeringToegang
from src.OTLMOW.OTLModel.Datatypes.KlDwarseMarkeringVerschuindCode import KlDwarseMarkeringVerschuindCode
from src.OTLMOW.OTLModel.Datatypes.KlDwarseMarkeringVerschuindSoort import KlDwarseMarkeringVerschuindSoort
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInDecimaleGraden import KwantWrdInDecimaleGraden
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class DwarseMarkeringVerschuind(DwarseMarkeringToegang):
    """Een schuine markering dwars op de weg aangebracht om het verkeer te waarschuwen, informeren of regelen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DwarseMarkeringVerschuind'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._basisoppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                              naam='basisoppervlakte',
                                              label='oppervlakte',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DwarseMarkeringVerschuind.basisoppervlakte',
                                              definition='De basisoppervlakte van de dwarse markering in vierkante meter.')

        self._code = OTLAttribuut(field=KlDwarseMarkeringVerschuindCode,
                                  naam='code',
                                  label='code',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DwarseMarkeringVerschuind.code',
                                  definition='De (COPRO/BENOR)  code van dwarse markering.')

        self._hoek = OTLAttribuut(field=KwantWrdInDecimaleGraden,
                                  naam='hoek',
                                  label='hoek',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DwarseMarkeringVerschuind.hoek',
                                  definition='De hoek van de verschuinde dwarsmarkering in decimale graden.')

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DwarseMarkeringVerschuind.oppervlakte',
                                         definition='De oppervlakte van een dwarsmarkering na verschuining.')

        self._soortOmschrijving = OTLAttribuut(field=KlDwarseMarkeringVerschuindSoort,
                                               naam='soortOmschrijving',
                                               label='soort omschrijving',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DwarseMarkeringVerschuind.soortOmschrijving',
                                               definition='De soort en tevens de omschrijving van dwarse markering.')

    @property
    def basisoppervlakte(self):
        """De basisoppervlakte van de dwarse markering in vierkante meter."""
        return self._basisoppervlakte.waarde

    @basisoppervlakte.setter
    def basisoppervlakte(self, value):
        self._basisoppervlakte.set_waarde(value, owner=self)

    @property
    def code(self):
        """De (COPRO/BENOR)  code van dwarse markering."""
        return self._code.waarde

    @code.setter
    def code(self, value):
        self._code.set_waarde(value, owner=self)

    @property
    def hoek(self):
        """De hoek van de verschuinde dwarsmarkering in decimale graden."""
        return self._hoek.waarde

    @hoek.setter
    def hoek(self, value):
        self._hoek.set_waarde(value, owner=self)

    @property
    def oppervlakte(self):
        """De oppervlakte van een dwarsmarkering na verschuining."""
        return self._oppervlakte.waarde

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)

    @property
    def soortOmschrijving(self):
        """De soort en tevens de omschrijving van dwarse markering."""
        return self._soortOmschrijving.waarde

    @soortOmschrijving.setter
    def soortOmschrijving(self, value):
        self._soortOmschrijving.set_waarde(value, owner=self)
