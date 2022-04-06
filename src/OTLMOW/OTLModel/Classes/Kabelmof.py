# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.KlKabelmofType import KlKabelmofType
from OTLMOW.OTLModel.Datatypes.KlKabelmofVerbinding import KlKabelmofVerbinding
from OTLMOW.OTLModel.Datatypes.KlNetwerkType import KlNetwerkType
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kabelmof(AIMNaamObject, PuntGeometrie):
    """Een verbindingsgreep die aansluitingen van kabels rondom afsluit."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelmof'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self._netwerkType = OTLAttribuut(field=KlNetwerkType,
                                         naam='netwerkType',
                                         label='netwerktype',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelmof.netwerkType',
                                         definition='Geeft aan bij welk type nutsvoorzieningennet de kabelmof hoort volgens de types uit IMKL en Inspire.',
                                         owner=self)

        self._type = OTLAttribuut(field=KlKabelmofType,
                                  naam='type',
                                  label='type kabelmof',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelmof.type',
                                  definition='Soort mof volgens een lijst van types.',
                                  owner=self)

        self._verbindingstype = OTLAttribuut(field=KlKabelmofVerbinding,
                                             naam='verbindingstype',
                                             label='verbindingstype',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelmof.verbindingstype',
                                             definition='Geeft het type aansluiting in de mof aan.',
                                             owner=self)

    @property
    def netwerkType(self):
        """Geeft aan bij welk type nutsvoorzieningennet de kabelmof hoort volgens de types uit IMKL en Inspire."""
        return self._netwerkType.waarde

    @netwerkType.setter
    def netwerkType(self, value):
        self._netwerkType.set_waarde(value, owner=self)

    @property
    def type(self):
        """Soort mof volgens een lijst van types."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def verbindingstype(self):
        """Geeft het type aansluiting in de mof aan."""
        return self._verbindingstype.waarde

    @verbindingstype.setter
    def verbindingstype(self, value):
        self._verbindingstype.set_waarde(value, owner=self)
