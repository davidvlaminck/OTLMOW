# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.BooleanField import BooleanField


# Generated with OTLClassCreator. To modify: extend, do not edit
class VentilatieAfsluitklep(AIMObject, AttributeInfo):
    """Constructie voor het fysiek afsluiten van een ventilatieschacht die verhindert dat luchtstromen van de (dwars)ventilatie door de schachten gaan."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VentilatieAfsluitklep'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        AttributeInfo.__init__(self)

        self._heeftManueleBediening = OTLAttribuut(field=BooleanField,
                                                   naam='heeftManueleBediening',
                                                   label='Heeft manuele bediening',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VentilatieAfsluitklep.heeftManueleBediening',
                                                   definition='Geeft aan of de afsluitklep manueel kan bediend worden.')

    @property
    def heeftManueleBediening(self):
        """Geeft aan of de afsluitklep manueel kan bediend worden."""
        return self._heeftManueleBediening.waarde

    @heeftManueleBediening.setter
    def heeftManueleBediening(self, value):
        self._heeftManueleBediening.set_waarde(value, owner=self)
