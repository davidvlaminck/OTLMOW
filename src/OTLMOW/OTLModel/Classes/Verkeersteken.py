# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.DtcAdres import DtcAdres
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.DtcExterneReferentie import DtcExterneReferentie
from OTLMOW.OTLModel.Datatypes.KlVerkeerstekenWettelijkeStatus import KlVerkeerstekenWettelijkeStatus
from OTLMOW.OTLModel.Datatypes.StringField import StringField
from OTLMOW.GeometrieArtefact.GeenGeometrie import GeenGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verkeersteken(AIMObject, GeenGeometrie):
    """Abstracte klasse voor aanwijzingen ten behoeve van de weggebruikers die verbonden wordt aan het aankondigen of opleggen van een bepaalde verkeersmaatregel zoals bepaald in de wegcode."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersteken'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMObject.__init__(self)
        GeenGeometrie.__init__(self)

        self._adres = OTLAttribuut(field=DtcAdres,
                                   naam='adres',
                                   label='adres',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersteken.adres',
                                   definition='Adres van het verkeersteken.',
                                   owner=self)

        self._afbeelding = OTLAttribuut(field=DtcDocument,
                                        naam='afbeelding',
                                        label='afbeelding',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersteken.afbeelding',
                                        kardinaliteit_min='0',
                                        kardinaliteit_max='*',
                                        definition='Foto van het verkeersteken.',
                                        owner=self)

        self._mobiliteitsMaatregel = OTLAttribuut(field=DtcExterneReferentie,
                                                  naam='mobiliteitsMaatregel',
                                                  label='mobiliteitsmaatregel',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersteken.mobiliteitsMaatregel',
                                                  kardinaliteit_min='0',
                                                  kardinaliteit_max='*',
                                                  definition='Externe referentie naar een maatregel om de beweging en verplaatsing van de weggebruiker op het openbaar domein of privé domein met openbaar karakter te organiseren.',
                                                  owner=self)

        self._plaatsbeschrijving = OTLAttribuut(field=StringField,
                                                naam='plaatsbeschrijving',
                                                label='plaatsbeschrijving',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersteken.plaatsbeschrijving',
                                                definition='Tekstuele beschrijving waar het verkeersteken zal komen.',
                                                owner=self)

        self._signalisatieVergunning = OTLAttribuut(field=DtcExterneReferentie,
                                                    naam='signalisatieVergunning',
                                                    label='signalisatievergunning',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersteken.signalisatieVergunning',
                                                    kardinaliteit_min='0',
                                                    kardinaliteit_max='*',
                                                    definition='Externe referentie naar een vergunning voor het tijdelijk aanbrengen of wijzigen van signalisatie op het openbaar domein of privaat domein met openbaar karakter.',
                                                    owner=self)

        self._variabelOpschrift = OTLAttribuut(field=StringField,
                                               naam='variabelOpschrift',
                                               label='variabel opschrift',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersteken.variabelOpschrift',
                                               definition='Variabele tekst die op het verkeersbordconcept komt te staan.',
                                               owner=self)

        self._wettelijkeStatus = OTLAttribuut(field=KlVerkeerstekenWettelijkeStatus,
                                              naam='wettelijkeStatus',
                                              label='wettelijke status',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersteken.wettelijkeStatus',
                                              usagenote='Bijvoorbeeld: vergund, niet-vergund, in ontwerp',
                                              definition='Duidt de wettelijke status aan van het verkeersteken.',
                                              owner=self)

    @property
    def adres(self):
        """Adres van het verkeersteken."""
        return self._adres.waarde

    @adres.setter
    def adres(self, value):
        self._adres.set_waarde(value, owner=self)

    @property
    def afbeelding(self):
        """Foto van het verkeersteken."""
        return self._afbeelding.waarde

    @afbeelding.setter
    def afbeelding(self, value):
        self._afbeelding.set_waarde(value, owner=self)

    @property
    def mobiliteitsMaatregel(self):
        """Externe referentie naar een maatregel om de beweging en verplaatsing van de weggebruiker op het openbaar domein of privé domein met openbaar karakter te organiseren."""
        return self._mobiliteitsMaatregel.waarde

    @mobiliteitsMaatregel.setter
    def mobiliteitsMaatregel(self, value):
        self._mobiliteitsMaatregel.set_waarde(value, owner=self)

    @property
    def plaatsbeschrijving(self):
        """Tekstuele beschrijving waar het verkeersteken zal komen."""
        return self._plaatsbeschrijving.waarde

    @plaatsbeschrijving.setter
    def plaatsbeschrijving(self, value):
        self._plaatsbeschrijving.set_waarde(value, owner=self)

    @property
    def signalisatieVergunning(self):
        """Externe referentie naar een vergunning voor het tijdelijk aanbrengen of wijzigen van signalisatie op het openbaar domein of privaat domein met openbaar karakter."""
        return self._signalisatieVergunning.waarde

    @signalisatieVergunning.setter
    def signalisatieVergunning(self, value):
        self._signalisatieVergunning.set_waarde(value, owner=self)

    @property
    def variabelOpschrift(self):
        """Variabele tekst die op het verkeersbordconcept komt te staan."""
        return self._variabelOpschrift.waarde

    @variabelOpschrift.setter
    def variabelOpschrift(self, value):
        self._variabelOpschrift.set_waarde(value, owner=self)

    @property
    def wettelijkeStatus(self):
        """Duidt de wettelijke status aan van het verkeersteken."""
        return self._wettelijkeStatus.waarde

    @wettelijkeStatus.setter
    def wettelijkeStatus(self, value):
        self._wettelijkeStatus.set_waarde(value, owner=self)
