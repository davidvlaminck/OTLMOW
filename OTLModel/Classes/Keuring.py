# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DateField import DateField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KwantWrdInJaar import KwantWrdInJaar


# Generated with OTLClassCreator. To modify: extend, do not edit
class Keuring(Proef, AttributeInfo):
    """Technische keuring uitgevoerd door een officiële keuringsinstantie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#Keuring'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        Proef.__init__(self)

        self._datum = OTLAttribuut(field=DateField,
                                   naam='datum',
                                   label='keuringsdatum',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#Keuring.datum',
                                   definition='De datum waarop de keuring werd uitgevoerd.')

        self._geldigheidsDuur = OTLAttribuut(field=KwantWrdInJaar,
                                             naam='geldigheidsDuur',
                                             label='geldigheidsduur',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#Keuring.geldigheidsDuur',
                                             definition='de periode (in jaar) waarbinnen de keuring geldig blijft. ')

        self._verslag = OTLAttribuut(field=DtcDocument,
                                     naam='verslag',
                                     label='keuringsverslag',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#Keuring.verslag',
                                     definition='document met het verslag van de keuring.')

    @property
    def datum(self):
        """De datum waarop de keuring werd uitgevoerd."""
        return self._datum.waarde

    @datum.setter
    def datum(self, value):
        self._datum.set_waarde(value, owner=self)

    @property
    def geldigheidsDuur(self):
        """de periode (in jaar) waarbinnen de keuring geldig blijft. """
        return self._geldigheidsDuur.waarde

    @geldigheidsDuur.setter
    def geldigheidsDuur(self, value):
        self._geldigheidsDuur.set_waarde(value, owner=self)

    @property
    def verslag(self):
        """document met het verslag van de keuring."""
        return self._verslag.waarde

    @verslag.setter
    def verslag(self, value):
        self._verslag.set_waarde(value, owner=self)
