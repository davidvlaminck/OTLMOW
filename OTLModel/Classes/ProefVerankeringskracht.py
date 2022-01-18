# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefVerankeringskracht(Proef, AttributeInfo):
    """Een trekproef in situ om de verankering van de ankerstaven in een betonverharding te testen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVerankeringskracht'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        Proef.__init__(self)

        self._verankeringskracht = OTLAttribuut(field=DtcDocument,
                                                naam='verankeringskracht',
                                                label='verankeringskracht',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVerankeringskracht.verankeringskracht',
                                                definition='Het resultaat van de test om de verankeringskracht in de BV laag.')

    @property
    def verankeringskracht(self):
        """Het resultaat van de test om de verankeringskracht in de BV laag."""
        return self._verankeringskracht.waarde

    @verankeringskracht.setter
    def verankeringskracht(self, value):
        self._verankeringskracht.set_waarde(value, owner=self)
