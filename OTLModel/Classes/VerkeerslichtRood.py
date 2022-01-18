# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Verkeerslicht import Verkeerslicht
from OTLModel.Datatypes.KlVriBewaking import KlVriBewaking


# Generated with OTLClassCreator. To modify: extend, do not edit
class VerkeerslichtRood(Verkeerslicht, AttributeInfo):
    """Een lichtbron met rode kleur om de weggebruikers aan te geven dat het verboden is de stopstreep of, zo er geen stopstreep is, het verkeerslicht zelf, voorbij te rijden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerkeerslichtRood'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        Verkeerslicht.__init__(self)

        self._typeBewaking = OTLAttribuut(field=KlVriBewaking,
                                          naam='typeBewaking',
                                          label='type bewaking',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerkeerslichtRood.typeBewaking',
                                          definition='Type bewaking van het rode verkeerslicht.')

    @property
    def typeBewaking(self):
        """Type bewaking van het rode verkeerslicht."""
        return self._typeBewaking.waarde

    @typeBewaking.setter
    def typeBewaking(self, value):
        self._typeBewaking.set_waarde(value, owner=self)
