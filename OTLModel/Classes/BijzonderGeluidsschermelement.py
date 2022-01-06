# coding=utf-8
from OTLModel.Classes.Geluidsschermelement import Geluidsschermelement
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBGSchermelementtype import KlBGSchermelementtype


# Generated with OTLClassCreator. To modify: extend, do not edit
class BijzonderGeluidsschermelement(Geluidsschermelement):
    """Dit zijn niet-vlakke schermelementen (waaronder L-elementen en bloembakelementen). Deze schermen kunnen niet getest worden volgens de normen NBN EN 1793-1 NBN EN 1793-2."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BijzonderGeluidsschermelement"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.schermelementtype = KeuzelijstField(naam="schermelementtype",
                                                 label="schermelementtype",
                                                 lijst=KlBGSchermelementtype(),
                                                 uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BijzonderGeluidsschermelement.schermelementtype",
                                                 definition="Het type bijzonder-schermelement.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        """Het type bijzonder-schermelement."""
