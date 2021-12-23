from OTLModel.Classes.Geluidsschermelement import Geluidsschermelement
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlVGOpstelling import KlVGOpstelling
from OTLModel.Datatypes.KlVGSchermelementtype import KlVGSchermelementtype
from OTLModel.Datatypes.KlVormSchermelement import KlVormSchermelement


# Generated with OTLClassCreator
class VlakGeluidsschermelement(Geluidsschermelement):
    """Een vlak scherm zijn alle schermtypes die getest kunnen worden volgens de normen NBN EN 1793-1 NBN EN 1793-2."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VlakGeluidsschermelement"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.opstelling = KeuzelijstField(naam="opstelling",
                                          label="opstelling",
                                          lijst=KlVGOpstelling(),
                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VlakGeluidsschermelement.opstelling",
                                          definition="Dit attribuut beschrijft de oriëntatie van het geplaatste schermelement t.o.v. de weg. De oriëntatie van vlakke schermen kan naast loodrecht op het maaiveld ook schuin naar achter hellend of schuin naar voor hellend zijn.",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        """Dit attribuut beschrijft de oriëntatie van het geplaatste schermelement t.o.v. de weg. De oriëntatie van vlakke schermen kan naast loodrecht op het maaiveld ook schuin naar achter hellend of schuin naar voor hellend zijn."""

        self.schermelementtype = KeuzelijstField(naam="schermelementtype",
                                                 label="schermelementtype",
                                                 lijst=KlVGSchermelementtype(),
                                                 uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VlakGeluidsschermelement.schermelementtype",
                                                 definition="Het type vlak-schermelement.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        """Het type vlak-schermelement."""

        self.vorm = KeuzelijstField(naam="vorm",
                                    label="vorm",
                                    lijst=KlVormSchermelement(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VlakGeluidsschermelement.vorm",
                                    definition="Dit attribuut geeft aan of het schermelement recht of gebogen is.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Dit attribuut geeft aan of het schermelement recht of gebogen is."""
