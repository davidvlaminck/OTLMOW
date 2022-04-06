# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.KlNetwerkType import KlNetwerkType
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ActivityComplex(AIMNaamObject, VlakGeometrie):
    """Het gehele gebied dat door dezelfde exploitant op dezelfde locatie of op verschillende geografische locaties wordt beheerd, inclusief alle infrastructuur, apparatuur en materialen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#ActivityComplex'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        VlakGeometrie.__init__(self)

        self._netwerk = OTLAttribuut(field=KlNetwerkType,
                                     naam='netwerk',
                                     label='netwerk',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#ActivityComplex.netwerk',
                                     definition='Geeft aan bij welk type nutsvoorzieningennet de kabelmof hoort volgens de types uit IMKL en Inspire.',
                                     owner=self)

    @property
    def netwerk(self):
        """Geeft aan bij welk type nutsvoorzieningennet de kabelmof hoort volgens de types uit IMKL en Inspire."""
        return self._netwerk.waarde

    @netwerk.setter
    def netwerk(self, value):
        self._netwerk.set_waarde(value, owner=self)
