# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AbstracteAanvullendeGeometrie import AbstracteAanvullendeGeometrie
from OTLMOW.OTLModel.Datatypes.KlOnderwaterkruisingAanlegWijze import KlOnderwaterkruisingAanlegWijze
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Onderwaterkruising(AbstracteAanvullendeGeometrie, LijnGeometrie):
    """Gebruikt voor de registratie van kenmerken en geometrie van een ruimte waar kabels en leidingen onder een waterweg door gaan."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderwaterkruising'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AbstracteAanvullendeGeometrie.__init__(self)
        LijnGeometrie.__init__(self)

        self._aanlegWijze = OTLAttribuut(field=KlOnderwaterkruisingAanlegWijze,
                                         naam='aanlegWijze',
                                         label='aanlge wijze',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderwaterkruising.aanlegWijze',
                                         definition='De manier waarop de onderwaterkruising gerealiseerd is volgens een vaste lijst met mogelijkheden.',
                                         owner=self)

        self._buitendiameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                            naam='buitendiameter',
                                            label='buitendiameter',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderwaterkruising.buitendiameter',
                                            definition='De buitendiameter van de onderwaterkruising. Indien de krusing niet cirkelvormig is, gaat het hier om de diameter van de omgeschreven cirkel.',
                                            owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderwaterkruising.lengte',
                                    definition='De effectieve lengte van de onderwaterkruising, rekening houdend met eventuele curves en dus niet als projectie op een vlak.',
                                    owner=self)

    @property
    def aanlegWijze(self):
        """De manier waarop de onderwaterkruising gerealiseerd is volgens een vaste lijst met mogelijkheden."""
        return self._aanlegWijze.waarde

    @aanlegWijze.setter
    def aanlegWijze(self, value):
        self._aanlegWijze.set_waarde(value, owner=self)

    @property
    def buitendiameter(self):
        """De buitendiameter van de onderwaterkruising. Indien de krusing niet cirkelvormig is, gaat het hier om de diameter van de omgeschreven cirkel."""
        return self._buitendiameter.waarde

    @buitendiameter.setter
    def buitendiameter(self, value):
        self._buitendiameter.set_waarde(value, owner=self)

    @property
    def lengte(self):
        """De effectieve lengte van de onderwaterkruising, rekening houdend met eventuele curves en dus niet als projectie op een vlak."""
        return self._lengte.waarde

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)
