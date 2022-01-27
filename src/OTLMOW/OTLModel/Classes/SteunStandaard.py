# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from src.OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from src.OTLMOW.OTLModel.Classes.EMDraagconstructie import EMDraagconstructie
from src.OTLMOW.OTLModel.Datatypes.DteKleurRAL import DteKleurRAL
from src.OTLMOW.OTLModel.Datatypes.KlDraagConstrBeschermlaag import KlDraagConstrBeschermlaag
from src.OTLMOW.OTLModel.Datatypes.KlDraagConstrBijzondertransport import KlDraagConstrBijzondertransport
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from src.OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class SteunStandaard(AIMNaamObject, EMDraagconstructie):
    """Abstracte voor de standaard steunen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMNaamObject.__init__(self)
        EMDraagconstructie.__init__(self)

        self._beschermlaag = OTLAttribuut(field=KlDraagConstrBeschermlaag,
                                          naam='beschermlaag',
                                          label='beschermlaag',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard.beschermlaag',
                                          definition='Type bescherming van de steun, bv. geschilderd of gegalvaniseerd.')

        self._bijzonderTransport = OTLAttribuut(field=KlDraagConstrBijzondertransport,
                                                naam='bijzonderTransport',
                                                label='bijzonder transport',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard.bijzonderTransport',
                                                definition='Wijze waarop het object eventueel geschikt is om bijzonder transport mogelijk te maken.')

        self._fabrikant = OTLAttribuut(field=StringField,
                                       naam='fabrikant',
                                       label='fabrikant',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard.fabrikant',
                                       definition='De fabrikant van de steun.')

        self._hoogteBovenkant = OTLAttribuut(field=KwantWrdInMeter,
                                             naam='hoogteBovenkant',
                                             label='hoogte bovenkant',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard.hoogteBovenkant',
                                             definition='Hoogte (in meter) van de bovenkant van de steun.')

        self._kleur = OTLAttribuut(field=DteKleurRAL,
                                   naam='kleur',
                                   label='kleur',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard.kleur',
                                   definition='De RAL kleur van het uitwendig zichtbare gedeelte.')

    @property
    def beschermlaag(self):
        """Type bescherming van de steun, bv. geschilderd of gegalvaniseerd."""
        return self._beschermlaag.waarde

    @beschermlaag.setter
    def beschermlaag(self, value):
        self._beschermlaag.set_waarde(value, owner=self)

    @property
    def bijzonderTransport(self):
        """Wijze waarop het object eventueel geschikt is om bijzonder transport mogelijk te maken."""
        return self._bijzonderTransport.waarde

    @bijzonderTransport.setter
    def bijzonderTransport(self, value):
        self._bijzonderTransport.set_waarde(value, owner=self)

    @property
    def fabrikant(self):
        """De fabrikant van de steun."""
        return self._fabrikant.waarde

    @fabrikant.setter
    def fabrikant(self, value):
        self._fabrikant.set_waarde(value, owner=self)

    @property
    def hoogteBovenkant(self):
        """Hoogte (in meter) van de bovenkant van de steun."""
        return self._hoogteBovenkant.waarde

    @hoogteBovenkant.setter
    def hoogteBovenkant(self, value):
        self._hoogteBovenkant.set_waarde(value, owner=self)

    @property
    def kleur(self):
        """De RAL kleur van het uitwendig zichtbare gedeelte."""
        return self._kleur.waarde

    @kleur.setter
    def kleur(self, value):
        self._kleur.set_waarde(value, owner=self)
