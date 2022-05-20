# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Detectielus import Detectielus
from OTLMOW.OTLModel.Datatypes.KlVriLusFunctie import KlVriLusFunctie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class VRIVirtueleDetectiezone(Detectielus, VlakGeometrie):
    """Een virtuele detectiezone is een draadloos alternatief voor een traditionele lus. Op basis van GPS gegevens wordt een zone of traject vastgelegd waarbinnen er (al dan niet selectieve) input dient geleverd te worden aan de verkeersregelaar. De virtuele detectiezone kan ook gebruikt worden om de detectiezones van detectiecamera's en radars te inventariseren.
"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRIVirtueleDetectiezone'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Detectielus.__init__(self)
        VlakGeometrie.__init__(self)

        self._functie = OTLAttribuut(field=KlVriLusFunctie,
                                     naam='functie',
                                     label='functie',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRIVirtueleDetectiezone.functie',
                                     definition='Functie van de VRI detectiezone.',
                                     owner=self)

    @property
    def functie(self):
        """Functie van de VRI detectiezone."""
        return self._functie.get_waarde()

    @functie.setter
    def functie(self, value):
        self._functie.set_waarde(value, owner=self)
