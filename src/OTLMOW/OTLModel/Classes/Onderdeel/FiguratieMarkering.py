# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.FiguratieMarkeringToegang import FiguratieMarkeringToegang
from OTLMOW.OTLModel.Datatypes.KlFiguratieCode import KlFiguratieCode
from OTLMOW.OTLModel.Datatypes.KlFiguratieSoort import KlFiguratieSoort
from OTLMOW.OTLModel.Datatypes.KlFiguratieType import KlFiguratieType
from OTLMOW.OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class FiguratieMarkering(FiguratieMarkeringToegang, PuntGeometrie):
    """Een markering als figuratie op de weg aangebracht om het verkeer te waarschuwen, informeren of regelen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FiguratieMarkering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        FiguratieMarkeringToegang.__init__(self)
        PuntGeometrie.__init__(self)

        self._code = OTLAttribuut(field=KlFiguratieCode,
                                  naam='code',
                                  label='code',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FiguratieMarkering.code',
                                  definition='De code van de figuratie markering.',
                                  owner=self)

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FiguratieMarkering.oppervlakte',
                                         definition='De oppervlakte van de markering zoals beschreven in de algemene omzendbrief.',
                                         owner=self)

        self._soortOmschrijving = OTLAttribuut(field=KlFiguratieSoort,
                                               naam='soortOmschrijving',
                                               label='soort omschrijving',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FiguratieMarkering.soortOmschrijving',
                                               definition='De soort en tevens de omschrijving van de figuratie markering.',
                                               owner=self)

        self._type = OTLAttribuut(field=KlFiguratieType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FiguratieMarkering.type',
                                  definition='Het type van figuratie markering.',
                                  owner=self)

    @property
    def code(self):
        """De code van de figuratie markering."""
        return self._code.get_waarde()

    @code.setter
    def code(self, value):
        self._code.set_waarde(value, owner=self)

    @property
    def oppervlakte(self):
        """De oppervlakte van de markering zoals beschreven in de algemene omzendbrief."""
        return self._oppervlakte.get_waarde()

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)

    @property
    def soortOmschrijving(self):
        """De soort en tevens de omschrijving van de figuratie markering."""
        return self._soortOmschrijving.get_waarde()

    @soortOmschrijving.setter
    def soortOmschrijving(self, value):
        self._soortOmschrijving.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van figuratie markering."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
