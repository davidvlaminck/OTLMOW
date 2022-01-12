# coding=utf-8
from OTLModel.Classes.LaagBouwklasse import LaagBouwklasse
from OTLModel.Datatypes.DtuBVLaagtypes import DtuBVLaagtypes
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBVBindmiddel import KlBVBindmiddel
from OTLModel.Datatypes.KlBVMengseltype import KlBVMengseltype
from OTLModel.Datatypes.KlKleurSupp import KlKleurSupp


# Generated with OTLClassCreator. To modify: extend, do not edit
class BitumineuzeLaag(LaagBouwklasse):
    """Flexibele verharding die meestal uit bitumineus gebonden materialen (asfalt of gietasfalt) bestaat en laagsgewijs wordt aangelegd. ."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.bindmiddelType = KeuzelijstField(naam="bindmiddelType",
                                              label="bindmiddel type",
                                              lijst=KlBVBindmiddel(),
                                              objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag.bindmiddelType",
                                              definition="Het bindmiddeltype van de bitumineuze laag.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        """Het bindmiddeltype van de bitumineuze laag."""

        self.kleur = KeuzelijstField(naam="kleur",
                                     label="kleur",
                                     lijst=KlKleurSupp(),
                                     objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag.kleur",
                                     definition="De kleur van de bitumineuze laag.",
                                     constraints="",
                                     usagenote="",
                                     deprecated_version="")
        """De kleur van de bitumineuze laag."""

        self.laagtype = DtuBVLaagtypes()
        """Het type van bitumineuze laag."""
        self.laagtype.naam = "laagtype"
        self.laagtype.label = "laagtype"
        self.laagtype.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag.laagtype"
        self.laagtype.definition = "Het type van bitumineuze laag."
        self.laagtype.constraints = ""
        self.laagtype.usagenote = ""
        self.laagtype.deprecated_version = ""

        self.mengseltype = KeuzelijstField(naam="mengseltype",
                                           label="mengseltype",
                                           lijst=KlBVMengseltype(),
                                           objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag.mengseltype",
                                           definition="Het type van het (giet)asfaltmengsel.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """Het type van het (giet)asfaltmengsel."""
