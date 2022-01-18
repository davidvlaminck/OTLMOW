# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Geluidsschermelement import Geluidsschermelement
from OTLModel.Datatypes.KlBGSchermelementtype import KlBGSchermelementtype


# Generated with OTLClassCreator. To modify: extend, do not edit
class BijzonderGeluidsschermelement(Geluidsschermelement, AttributeInfo):
    """Dit zijn niet-vlakke schermelementen (waaronder L-elementen en bloembakelementen). Deze schermen kunnen niet getest worden volgens de normen NBN EN 1793-1 NBN EN 1793-2."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BijzonderGeluidsschermelement'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        Geluidsschermelement.__init__(self)

        self._schermelementtype = OTLAttribuut(field=KlBGSchermelementtype,
                                               naam='schermelementtype',
                                               label='schermelementtype',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BijzonderGeluidsschermelement.schermelementtype',
                                               definition='Het type bijzonder-schermelement.')

    @property
    def schermelementtype(self):
        """Het type bijzonder-schermelement."""
        return self._schermelementtype.waarde

    @schermelementtype.setter
    def schermelementtype(self, value):
        self._schermelementtype.set_waarde(value, owner=self)
