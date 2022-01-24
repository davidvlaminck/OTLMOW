# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.DteTekstblok import DteTekstblok
from OTLModel.Datatypes.KlRioleringVorm import KlRioleringVorm
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter
from OTLModel.Datatypes.KwantWrdInPromille import KwantWrdInPromille


# Generated with OTLClassCreator. To modify: extend, do not edit
class Buis(AIMObject):
    """Abstracte om de gemeenschappelijke eigenschappen en relaties van de verschillende soorten buizen onder één noemer te houden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._bokAfwaarts = OTLAttribuut(field=KwantWrdInMeterTAW,
                                         naam='bokAfwaarts',
                                         label='bok afwaarts',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.bokAfwaarts',
                                         definition='Peil in meter-TAW van de vloei aan de afwaartse kant van de buis.')

        self._bokOpwaarts = OTLAttribuut(field=KwantWrdInMeterTAW,
                                         naam='bokOpwaarts',
                                         label='bok opwaarts',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.bokOpwaarts',
                                         definition='Peil in meter-TAW van de vloei aan de opwaartse kant van de buis.')

        self._breedte = OTLAttribuut(field=KwantWrdInMillimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.breedte',
                                     usagenote='Attribuut uit gebruik sinds versie 2.1.0 ',
                                     deprecated_version='2.1.0',
                                     definition='De breedte van de buis in millimeter.')

        self._breedteBinnenzijde = OTLAttribuut(field=KwantWrdInMillimeter,
                                                naam='breedteBinnenzijde',
                                                label='breedte binnenzijde',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.breedteBinnenzijde',
                                                definition='De breedte van de binnenzijde van de buis in millimeter. Bij cirkelvormige buizen is dit de binnendiameter.')

        self._breedteBuitenzijde = OTLAttribuut(field=KwantWrdInMillimeter,
                                                naam='breedteBuitenzijde',
                                                label='breedte buitenzijde',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.breedteBuitenzijde',
                                                definition='De breedte van de buitenzijde van de buis in millimeter. Bij cirkelvormige buizen is dit de buitendiameter.')

        self._diepteAfwaarts = OTLAttribuut(field=KwantWrdInMeter,
                                            naam='diepteAfwaarts',
                                            label='diepte afwaarts',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.diepteAfwaarts',
                                            definition='Diepte van de vloei aan de afwaartse kant van de buis t.o.v. de bovenkant van het deksel.')

        self._diepteOpwaarts = OTLAttribuut(field=KwantWrdInMeter,
                                            naam='diepteOpwaarts',
                                            label='diepte opwaarts',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.diepteOpwaarts',
                                            definition='De diepte van de vloei aan de opwaartse kant van de buis t.o.v. de bovenkant van het deksel.')

        self._helling = OTLAttribuut(field=KwantWrdInPromille,
                                     naam='helling',
                                     label='helling',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.helling',
                                     definition='De helling van de buis in de lengterichting, uitgedrukt in promille.')

        self._hoogteBinnenzijde = OTLAttribuut(field=KwantWrdInMillimeter,
                                               naam='hoogteBinnenzijde',
                                               label='hoogte binnenzijde',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.hoogteBinnenzijde',
                                               definition='De hoogte van de binnenzijde van de buis in millimeter. Bij cirkelvormige buizen is dit de binnendiameter.')

        self._hoogteBuitenzijde = OTLAttribuut(field=KwantWrdInMillimeter,
                                               naam='hoogteBuitenzijde',
                                               label='hoogte buitenzijde',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.hoogteBuitenzijde',
                                               definition='De hoogte van de buitenzijde van een buis in millimeter. Bij cirkelvormige buizen is dit de buitendiameter.')

        self._isManToegankelijk = OTLAttribuut(field=BooleanField,
                                               naam='isManToegankelijk',
                                               label='is man toegankelijk',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.isManToegankelijk',
                                               definition='Bepaalt of de buis toegankelijk is voor een persoon.')

        self._isOpgevuld = OTLAttribuut(field=BooleanField,
                                        naam='isOpgevuld',
                                        label='is opgevuld',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.isOpgevuld',
                                        definition='Geeft aan of de buis gestabiliseerd/opgevuld is of niet.')

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.lengte',
                                    definition='De totale lengte in meter van de buis tussen opwaartse en afwaartse put.')

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.technischeFiche',
                                             usagenote='Bestanden van het type xlsx of pdf.',
                                             kardinaliteit_max='*',
                                             definition='De technische fiche van de buis.')

        self._toestandBuis = OTLAttribuut(field=DteTekstblok,
                                          naam='toestandBuis',
                                          label='toestand buis',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.toestandBuis',
                                          definition='Opmerkingen van de toestand en staat van de buis.')

        self._vorm = OTLAttribuut(field=KlRioleringVorm,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.vorm',
                                  definition='Bepaalt de vorm van de buis.')

    @property
    def bokAfwaarts(self):
        """Peil in meter-TAW van de vloei aan de afwaartse kant van de buis."""
        return self._bokAfwaarts.waarde

    @bokAfwaarts.setter
    def bokAfwaarts(self, value):
        self._bokAfwaarts.set_waarde(value, owner=self)

    @property
    def bokOpwaarts(self):
        """Peil in meter-TAW van de vloei aan de opwaartse kant van de buis."""
        return self._bokOpwaarts.waarde

    @bokOpwaarts.setter
    def bokOpwaarts(self, value):
        self._bokOpwaarts.set_waarde(value, owner=self)

    @property
    def breedte(self):
        """De breedte van de buis in millimeter."""
        return self._breedte.waarde

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def breedteBinnenzijde(self):
        """De breedte van de binnenzijde van de buis in millimeter. Bij cirkelvormige buizen is dit de binnendiameter."""
        return self._breedteBinnenzijde.waarde

    @breedteBinnenzijde.setter
    def breedteBinnenzijde(self, value):
        self._breedteBinnenzijde.set_waarde(value, owner=self)

    @property
    def breedteBuitenzijde(self):
        """De breedte van de buitenzijde van de buis in millimeter. Bij cirkelvormige buizen is dit de buitendiameter."""
        return self._breedteBuitenzijde.waarde

    @breedteBuitenzijde.setter
    def breedteBuitenzijde(self, value):
        self._breedteBuitenzijde.set_waarde(value, owner=self)

    @property
    def diepteAfwaarts(self):
        """Diepte van de vloei aan de afwaartse kant van de buis t.o.v. de bovenkant van het deksel."""
        return self._diepteAfwaarts.waarde

    @diepteAfwaarts.setter
    def diepteAfwaarts(self, value):
        self._diepteAfwaarts.set_waarde(value, owner=self)

    @property
    def diepteOpwaarts(self):
        """De diepte van de vloei aan de opwaartse kant van de buis t.o.v. de bovenkant van het deksel."""
        return self._diepteOpwaarts.waarde

    @diepteOpwaarts.setter
    def diepteOpwaarts(self, value):
        self._diepteOpwaarts.set_waarde(value, owner=self)

    @property
    def helling(self):
        """De helling van de buis in de lengterichting, uitgedrukt in promille."""
        return self._helling.waarde

    @helling.setter
    def helling(self, value):
        self._helling.set_waarde(value, owner=self)

    @property
    def hoogteBinnenzijde(self):
        """De hoogte van de binnenzijde van de buis in millimeter. Bij cirkelvormige buizen is dit de binnendiameter."""
        return self._hoogteBinnenzijde.waarde

    @hoogteBinnenzijde.setter
    def hoogteBinnenzijde(self, value):
        self._hoogteBinnenzijde.set_waarde(value, owner=self)

    @property
    def hoogteBuitenzijde(self):
        """De hoogte van de buitenzijde van een buis in millimeter. Bij cirkelvormige buizen is dit de buitendiameter."""
        return self._hoogteBuitenzijde.waarde

    @hoogteBuitenzijde.setter
    def hoogteBuitenzijde(self, value):
        self._hoogteBuitenzijde.set_waarde(value, owner=self)

    @property
    def isManToegankelijk(self):
        """Bepaalt of de buis toegankelijk is voor een persoon."""
        return self._isManToegankelijk.waarde

    @isManToegankelijk.setter
    def isManToegankelijk(self, value):
        self._isManToegankelijk.set_waarde(value, owner=self)

    @property
    def isOpgevuld(self):
        """Geeft aan of de buis gestabiliseerd/opgevuld is of niet."""
        return self._isOpgevuld.waarde

    @isOpgevuld.setter
    def isOpgevuld(self, value):
        self._isOpgevuld.set_waarde(value, owner=self)

    @property
    def lengte(self):
        """De totale lengte in meter van de buis tussen opwaartse en afwaartse put."""
        return self._lengte.waarde

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """De technische fiche van de buis."""
        return self._technischeFiche.waarde

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def toestandBuis(self):
        """Opmerkingen van de toestand en staat van de buis."""
        return self._toestandBuis.waarde

    @toestandBuis.setter
    def toestandBuis(self, value):
        self._toestandBuis.set_waarde(value, owner=self)

    @property
    def vorm(self):
        """Bepaalt de vorm van de buis."""
        return self._vorm.waarde

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self)
