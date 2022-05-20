# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Bebakening import Bebakening
from OTLMOW.OTLModel.Datatypes.KlWegbebakeningType import KlWegbebakeningType
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class WegbebakeningAfschermendeConstructies(Bebakening, PuntGeometrie):
    """Een houder met reflector op een constructie met als doel het verkeer te geleiden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WegbebakeningAfschermendeConstructies'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Bebakening.__init__(self)
        PuntGeometrie.__init__(self)

        self._type = OTLAttribuut(field=KlWegbebakeningType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WegbebakeningAfschermendeConstructies.type',
                                  definition='De vorm van wegbebakening voor afschermende constructies.',
                                  owner=self)

    @property
    def type(self):
        """De vorm van wegbebakening voor afschermende constructies."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
