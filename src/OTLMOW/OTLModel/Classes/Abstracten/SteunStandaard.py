# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.Abstracten.EMDraagconstructie import EMDraagconstructie
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.DteKleurRAL import DteKleurRAL
from OTLMOW.OTLModel.Datatypes.KlDraagConstrBeschermlaag import KlDraagConstrBeschermlaag
from OTLMOW.OTLModel.Datatypes.KlDraagConstrBijzondertransport import KlDraagConstrBijzondertransport
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class SteunStandaard(EMDraagconstructie, AIMNaamObject):
    """Abstracte voor de standaard steunen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMNaamObject.__init__(self)
        EMDraagconstructie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Betonfundering', deprecated='2.0.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlassiekeFundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verankering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingsmassief')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingsplaat')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sokkel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verankeringsmassief')

        self._beschermlaag = OTLAttribuut(field=KlDraagConstrBeschermlaag,
                                          naam='beschermlaag',
                                          label='beschermlaag',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard.beschermlaag',
                                          definition='Type bescherming van de steun, bv. geschilderd of gegalvaniseerd.',
                                          owner=self)

        self._bijzonderTransport = OTLAttribuut(field=KlDraagConstrBijzondertransport,
                                                naam='bijzonderTransport',
                                                label='bijzonder transport',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard.bijzonderTransport',
                                                definition='Wijze waarop het object eventueel geschikt is om bijzonder transport mogelijk te maken.',
                                                owner=self)

        self._fabrikant = OTLAttribuut(field=StringField,
                                       naam='fabrikant',
                                       label='fabrikant',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard.fabrikant',
                                       definition='De fabrikant van de steun.',
                                       owner=self)

        self._hoogteBovenkant = OTLAttribuut(field=KwantWrdInMeter,
                                             naam='hoogteBovenkant',
                                             label='hoogte bovenkant',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard.hoogteBovenkant',
                                             definition='Hoogte (in meter) van de bovenkant van de steun.',
                                             owner=self)

        self._kleur = OTLAttribuut(field=DteKleurRAL,
                                   naam='kleur',
                                   label='kleur',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard.kleur',
                                   definition='De RAL kleur van het uitwendig zichtbare gedeelte.',
                                   owner=self)

    @property
    def beschermlaag(self):
        """Type bescherming van de steun, bv. geschilderd of gegalvaniseerd."""
        return self._beschermlaag.get_waarde()

    @beschermlaag.setter
    def beschermlaag(self, value):
        self._beschermlaag.set_waarde(value, owner=self)

    @property
    def bijzonderTransport(self):
        """Wijze waarop het object eventueel geschikt is om bijzonder transport mogelijk te maken."""
        return self._bijzonderTransport.get_waarde()

    @bijzonderTransport.setter
    def bijzonderTransport(self, value):
        self._bijzonderTransport.set_waarde(value, owner=self)

    @property
    def fabrikant(self):
        """De fabrikant van de steun."""
        return self._fabrikant.get_waarde()

    @fabrikant.setter
    def fabrikant(self, value):
        self._fabrikant.set_waarde(value, owner=self)

    @property
    def hoogteBovenkant(self):
        """Hoogte (in meter) van de bovenkant van de steun."""
        return self._hoogteBovenkant.get_waarde()

    @hoogteBovenkant.setter
    def hoogteBovenkant(self, value):
        self._hoogteBovenkant.set_waarde(value, owner=self)

    @property
    def kleur(self):
        """De RAL kleur van het uitwendig zichtbare gedeelte."""
        return self._kleur.get_waarde()

    @kleur.setter
    def kleur(self, value):
        self._kleur.set_waarde(value, owner=self)
