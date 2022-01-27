# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.DwarseMarkeringToegang import DwarseMarkeringToegang
from OTLMOW.OTLModel.Datatypes.KlDwarseMarkeringCode import KlDwarseMarkeringCode
from OTLMOW.OTLModel.Datatypes.KlDwarseMarkeringSoort import KlDwarseMarkeringSoort
from OTLMOW.OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class DwarseMarkering(DwarseMarkeringToegang):
    """Een markering dwars op de weg aangebracht om het verkeer te waarschuwen, informeren of regelen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DwarseMarkering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._code = OTLAttribuut(field=KlDwarseMarkeringCode,
                                  naam='code',
                                  label='code',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DwarseMarkering.code',
                                  definition='De (COPRO/BENOR)  code van dwarse markering.')

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DwarseMarkering.oppervlakte',
                                         definition='De oppervlakte van de dwarse markering in vierkante meter.')

        self._soortOmschrijving = OTLAttribuut(field=KlDwarseMarkeringSoort,
                                               naam='soortOmschrijving',
                                               label='soort omschrijving',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DwarseMarkering.soortOmschrijving',
                                               definition='De soort en tevens de omschrijving van dwarse markering.')

    @property
    def code(self):
        """De (COPRO/BENOR)  code van dwarse markering."""
        return self._code.waarde

    @code.setter
    def code(self, value):
        self._code.set_waarde(value, owner=self)

    @property
    def oppervlakte(self):
        """De oppervlakte van de dwarse markering in vierkante meter."""
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
