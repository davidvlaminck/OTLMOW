# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefNaderOnderzoekTomograaf(Proef):
    """Een geluids- en/of elektrische weerstandstomografie is een niet-destructieve methode om rot en holtes in bomen op te sporen door gebruik van geluidsgolven en/of elektrische stroom."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefNaderOnderzoekTomograaf'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._inclusiefElektrisch = OTLAttribuut(field=BooleanField,
                                                 naam='inclusiefElektrisch',
                                                 label='inclusief elektrisch',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefNaderOnderzoekTomograaf.inclusiefElektrisch',
                                                 definition='Aanduiding of naast een geluidsweerstandstomografie ook een elektrische weerstandstomografie gebeurd is.')

        self._naderOnderzoekTomograaf = OTLAttribuut(field=DtcDocument,
                                                     naam='naderOnderzoekTomograaf',
                                                     label='nader onderzoek tomograaf',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefNaderOnderzoekTomograaf.naderOnderzoekTomograaf',
                                                     kardinaliteit_max='*',
                                                     definition='Het resultaat van de tomograaf proef.')

    @property
    def inclusiefElektrisch(self):
        """Aanduiding of naast een geluidsweerstandstomografie ook een elektrische weerstandstomografie gebeurd is."""
        return self._inclusiefElektrisch.waarde

    @inclusiefElektrisch.setter
    def inclusiefElektrisch(self, value):
        self._inclusiefElektrisch.set_waarde(value, owner=self)

    @property
    def naderOnderzoekTomograaf(self):
        """Het resultaat van de tomograaf proef."""
        return self._naderOnderzoekTomograaf.waarde

    @naderOnderzoekTomograaf.setter
    def naderOnderzoekTomograaf(self, value):
        self._naderOnderzoekTomograaf.set_waarde(value, owner=self)
