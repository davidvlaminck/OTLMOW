# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefGrondkarakteristieken(Proef):
    """Bepaling van de grondeigenschappen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGrondkarakteristieken'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._bepalingGrondkarakteristieken = OTLAttribuut(field=DtcDocument,
                                                           naam='bepalingGrondkarakteristieken',
                                                           label='bepaling grondkarakteristieken',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGrondkarakteristieken.bepalingGrondkarakteristieken',
                                                           definition='Proef met de resultaten van de grondkarakteristieken.')

    @property
    def bepalingGrondkarakteristieken(self):
        """Proef met de resultaten van de grondkarakteristieken."""
        return self._bepalingGrondkarakteristieken.waarde

    @bepalingGrondkarakteristieken.setter
    def bepalingGrondkarakteristieken(self, value):
        self._bepalingGrondkarakteristieken.set_waarde(value, owner=self)
