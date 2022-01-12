# coding=utf-8
from abc import abstractmethod
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Classes.EMDraagconstructie import EMDraagconstructie
from OTLModel.Datatypes.DteKleurRAL import DteKleurRAL
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlDraagConstrBeschermlaag import KlDraagConstrBeschermlaag
from OTLModel.Datatypes.KlDraagConstrBijzondertransport import KlDraagConstrBijzondertransport
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class SteunStandaard(AIMNaamObject, EMDraagconstructie):
    """Abstracte voor de standaard steunen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMNaamObject.__init__(self)
        EMDraagconstructie.__init__(self)

        self.beschermlaag = KeuzelijstField(naam="beschermlaag",
                                            label="beschermlaag",
                                            lijst=KlDraagConstrBeschermlaag(),
                                            objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard.beschermlaag",
                                            definition="Type bescherming van de steun, bv. geschilderd of gegalvaniseerd.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Type bescherming van de steun, bv. geschilderd of gegalvaniseerd."""

        self.bijzonderTransport = KeuzelijstField(naam="bijzonderTransport",
                                                  label="bijzonder transport",
                                                  lijst=KlDraagConstrBijzondertransport(),
                                                  objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard.bijzonderTransport",
                                                  definition="Wijze waarop het object eventueel geschikt is om bijzonder transport mogelijk te maken.",
                                                  constraints="",
                                                  usagenote="",
                                                  deprecated_version="")
        """Wijze waarop het object eventueel geschikt is om bijzonder transport mogelijk te maken."""

        self.fabrikant = StringField(naam="fabrikant",
                                     label="fabrikant",
                                     objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard.fabrikant",
                                     definition="De fabrikant van de steun.",
                                     constraints="",
                                     usagenote="",
                                     deprecated_version="")
        """De fabrikant van de steun."""

        self.hoogteBovenkant = KwantWrdInMeter()
        """Hoogte (in meter) van de bovenkant van de steun."""
        self.hoogteBovenkant.naam = "hoogteBovenkant"
        self.hoogteBovenkant.label = "hoogte bovenkant"
        self.hoogteBovenkant.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard.hoogteBovenkant"
        self.hoogteBovenkant.definition = "Hoogte (in meter) van de bovenkant van de steun."
        self.hoogteBovenkant.constraints = ""
        self.hoogteBovenkant.usagenote = ""
        self.hoogteBovenkant.deprecated_version = ""

        self.kleur = DteKleurRAL()
        """De RAL kleur van het uitwendig zichtbare gedeelte."""
        self.kleur.naam = "kleur"
        self.kleur.label = "kleur"
        self.kleur.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard.kleur"
        self.kleur.definition = "De RAL kleur van het uitwendig zichtbare gedeelte."
        self.kleur.constraints = ""
        self.kleur.usagenote = ""
        self.kleur.deprecated_version = ""
