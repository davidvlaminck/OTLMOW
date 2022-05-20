# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.FiguratieMarkeringToegang import FiguratieMarkeringToegang
from OTLMOW.OTLModel.Datatypes.KlLetterCijfer import KlLetterCijfer
from OTLMOW.OTLModel.Datatypes.KlLetterCijferType import KlLetterCijferType
from OTLMOW.OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class LetterCijferMarkering(FiguratieMarkeringToegang, PuntGeometrie):
    """Een markering bestaande uit individuele letters en/of cijfers."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LetterCijferMarkering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        FiguratieMarkeringToegang.__init__(self)
        PuntGeometrie.__init__(self)

        self._letterCijfer = OTLAttribuut(field=KlLetterCijfer,
                                          naam='letterCijfer',
                                          label='letter-cijfer',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LetterCijferMarkering.letterCijfer',
                                          definition='De individuele letter of cijfer gebruikt bij de wegmarkering.',
                                          owner=self)

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='basisoppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LetterCijferMarkering.oppervlakte',
                                         definition='De oppervlakte van de individuele letter- of cijfermarkering zoals beschreven in de algemene omzendbrief.',
                                         owner=self)

        self._type = OTLAttribuut(field=KlLetterCijferType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LetterCijferMarkering.type',
                                  definition='Het type van de individuele letter- of cijfermarkering.',
                                  owner=self)

    @property
    def letterCijfer(self):
        """De individuele letter of cijfer gebruikt bij de wegmarkering."""
        return self._letterCijfer.get_waarde()

    @letterCijfer.setter
    def letterCijfer(self, value):
        self._letterCijfer.set_waarde(value, owner=self)

    @property
    def oppervlakte(self):
        """De oppervlakte van de individuele letter- of cijfermarkering zoals beschreven in de algemene omzendbrief."""
        return self._oppervlakte.get_waarde()

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van de individuele letter- of cijfermarkering."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
