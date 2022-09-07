# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Geluidsschermelement import Geluidsschermelement
from OTLMOW.OTLModel.Datatypes.KlBGSchermelementtype import KlBGSchermelementtype


# Generated with OTLClassCreator. To modify: extend, do not edit
class BijzonderGeluidsschermelement(Geluidsschermelement):
    """Dit zijn niet-vlakke schermelementen (waaronder L-elementen en bloembakelementen). Deze schermen kunnen niet getest worden volgens de normen NBN EN 1793-1 NBN EN 1793-2."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BijzonderGeluidsschermelement'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BevestigingGC')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElementenGC')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VegetatieElement')

        self._schermelementtype = OTLAttribuut(field=KlBGSchermelementtype,
                                               naam='schermelementtype',
                                               label='schermelementtype',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BijzonderGeluidsschermelement.schermelementtype',
                                               definition='Het type bijzonder-schermelement.',
                                               owner=self)

    @property
    def schermelementtype(self):
        """Het type bijzonder-schermelement."""
        return self._schermelementtype.get_waarde()

    @schermelementtype.setter
    def schermelementtype(self, value):
        self._schermelementtype.set_waarde(value, owner=self)
