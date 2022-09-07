# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.BevestigingGC import BevestigingGC
from OTLMOW.OTLModel.Classes.Abstracten.Signalisatie import Signalisatie
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.DteTekstblok import DteTekstblok
from OTLMOW.OTLModel.Datatypes.KlSignalisatieReferentiepuntType import KlSignalisatieReferentiepuntType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Referentiepunt(BevestigingGC, Signalisatie, AIMObject):
    """Een kilometer- of hectometerpaal."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Referentiepunt'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        BevestigingGC.__init__(self)
        Signalisatie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#StalenProfiel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie', deprecated='2.0.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WegbebakeningAfschermendeConstructies')

        self._opschrift = OTLAttribuut(field=DteTekstblok,
                                       naam='opschrift',
                                       label='opschrift',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Referentiepunt.opschrift',
                                       definition='De notatie van het referentiepunt.',
                                       owner=self)

        self._type = OTLAttribuut(field=KlSignalisatieReferentiepuntType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Referentiepunt.type',
                                  definition='Het type van referentiepunt.',
                                  owner=self)

    @property
    def opschrift(self):
        """De notatie van het referentiepunt."""
        return self._opschrift.get_waarde()

    @opschrift.setter
    def opschrift(self, value):
        self._opschrift.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van referentiepunt."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
