# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Classes.Signalisatie import Signalisatie
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KlVerkeersspiegelVorm import KlVerkeersspiegelVorm
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verkeersspiegel(AIMObject, Signalisatie, PuntGeometrie):
    """Een verkeersspiegel is een spiegel die de zichtbaarheid verbetert van het aankomende verkeer."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersspiegel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        Signalisatie.__init__(self)
        PuntGeometrie.__init__(self)

        self._bijlageDocument = OTLAttribuut(field=DtcDocument,
                                             naam='bijlageDocument',
                                             label='bijlage document',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersspiegel.bijlageDocument',
                                             kardinaliteit_max='*',
                                             definition='Een document met dossiernummer waardoor men kan terugkoppelen naar de vergunning.',
                                             owner=self)

        self._isGoedgekeurd = OTLAttribuut(field=BooleanField,
                                           naam='isGoedgekeurd',
                                           label='is goedgekeurd',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersspiegel.isGoedgekeurd',
                                           definition='Geeft of de verkeersspiegel al dan niet goedgekeurd is.',
                                           owner=self)

        self._vorm = OTLAttribuut(field=KlVerkeersspiegelVorm,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersspiegel.vorm',
                                  definition='Bepaling van de vorm van de gebruikte verkeersspiegel.',
                                  owner=self)

    @property
    def bijlageDocument(self):
        """Een document met dossiernummer waardoor men kan terugkoppelen naar de vergunning."""
        return self._bijlageDocument.get_waarde()

    @bijlageDocument.setter
    def bijlageDocument(self, value):
        self._bijlageDocument.set_waarde(value, owner=self)

    @property
    def isGoedgekeurd(self):
        """Geeft of de verkeersspiegel al dan niet goedgekeurd is."""
        return self._isGoedgekeurd.get_waarde()

    @isGoedgekeurd.setter
    def isGoedgekeurd(self, value):
        self._isGoedgekeurd.set_waarde(value, owner=self)

    @property
    def vorm(self):
        """Bepaling van de vorm van de gebruikte verkeersspiegel."""
        return self._vorm.get_waarde()

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self)
