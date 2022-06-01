# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.NaampadObject import NaampadObject
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Slagboom(NaampadObject, VlakGeometrie):
    """Een afsluitingsmechanisme met slagboomarmen dat dient om controle uit te kunnen oefenen over het gebruik van een doorgang of een toegang."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Slagboom'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        NaampadObject.__init__(self)
        VlakGeometrie.__init__(self)

        self._isManueel = OTLAttribuut(field=BooleanField,
                                       naam='isManueel',
                                       label='is manueel',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Slagboom.isManueel',
                                       usagenote='Voor een manuele slagboom zijn geen instanties van de onderliggende onderdelen Slagboomkolom en Slagboomarm vereist.',
                                       definition='Geeft aan of de slagboom (uitsluitend) manueel bediend wordt of door een aangestuurde motor in de slagboomkolom.',
                                       owner=self)

    @property
    def isManueel(self):
        """Geeft aan of de slagboom (uitsluitend) manueel bediend wordt of door een aangestuurde motor in de slagboomkolom."""
        return self._isManueel.get_waarde()

    @isManueel.setter
    def isManueel(self, value):
        self._isManueel.set_waarde(value, owner=self)
