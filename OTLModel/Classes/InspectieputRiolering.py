# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Classes.Put import Put
from OTLModel.Datatypes.KlPutType import KlPutType
from OTLModel.Datatypes.KwantWrdInDecimaleGraden import KwantWrdInDecimaleGraden


# Generated with OTLClassCreator. To modify: extend, do not edit
class InspectieputRiolering(AIMObject, Put):
    """Dient om de aanwezige riolering te kunnen inspecteren, reinigen of onderhouden. """

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#InspectieputRiolering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        Put.__init__(self)

        self._hoekverdraaiing = OTLAttribuut(field=KwantWrdInDecimaleGraden,
                                             naam='hoekverdraaiing',
                                             label='hoekverdraaiing',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#InspectieputRiolering.hoekverdraaiing',
                                             definition='Verschil in richting tussen inkomende en uitgaande rioolbuis.')

        self._type = OTLAttribuut(field=KlPutType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#InspectieputRiolering.type',
                                  definition='Het type van de put zoals beschreven in hoofdstuk 7 van het standaardbestek 250.')

    @property
    def hoekverdraaiing(self):
        """Verschil in richting tussen inkomende en uitgaande rioolbuis."""
        return self._hoekverdraaiing.waarde

    @hoekverdraaiing.setter
    def hoekverdraaiing(self, value):
        self._hoekverdraaiing.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van de put zoals beschreven in hoofdstuk 7 van het standaardbestek 250."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
