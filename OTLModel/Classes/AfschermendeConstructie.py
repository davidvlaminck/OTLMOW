# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLModel.Classes.BijlageVoertuigkering import BijlageVoertuigkering
from OTLModel.Classes.LijnvormigElement import LijnvormigElement
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.DtcProductidentificatiecode import DtcProductidentificatiecode
from OTLModel.Datatypes.KlLEACMateriaal import KlLEACMateriaal
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class AfschermendeConstructie(BijlageVoertuigkering, LijnvormigElement, AttributeInfo):
    """Abstracte die een lijn- of puntvormige constructie,geïnstalleerd langs de weg om een kerend vermogen te bieden aan een dwalend voertuig,samenvat."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AttributeInfo.__init__(self)
        BijlageVoertuigkering.__init__(self)
        LijnvormigElement.__init__(self)

        self._certificaathouder = OTLAttribuut(field=StringField,
                                               naam='certificaathouder',
                                               label='certificaathouder',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie.certificaathouder',
                                               definition='De houder van het uitvoeringscertificaat.')

        self._isPermanent = OTLAttribuut(field=BooleanField,
                                         naam='isPermanent',
                                         label='is permanent',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie.isPermanent',
                                         definition='Vermelding of de afschermende constructie al dan niet van permanente aard is.')

        self._materiaal = OTLAttribuut(field=KlLEACMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie.materiaal',
                                       definition='Het gebruikte materiaal voor de afschermende constructie.')

        self._metTandGroef = OTLAttribuut(field=BooleanField,
                                          naam='metTandGroef',
                                          label='met tand-groef',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie.metTandGroef',
                                          definition='Geeft aan of de afschermende constructie bevestigd is aan de onderliggende laag door middel van een tand-groef aansluiting.')

        self._productidentificatiecode = OTLAttribuut(field=DtcProductidentificatiecode,
                                                      naam='productidentificatiecode',
                                                      label='productidentificatiecode',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie.productidentificatiecode',
                                                      definition='De productidentificatiecode voor het bepalen van de code van het gebruikte product (bv. COPRO/BENOR).')

        self._productnaam = OTLAttribuut(field=StringField,
                                         naam='productnaam',
                                         label='productnaam',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie.productnaam',
                                         definition='Dit is de commerciële naam van de afschermende constructie.')

        self._testrapport = OTLAttribuut(field=DtcDocument,
                                         naam='testrapport',
                                         label='testrapport',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie.testrapport',
                                         usagenote='Attribuut uit gebruik sinds versie 2.0.0',
                                         deprecated_version='2.0.0',
                                         kardinaliteit_max='*',
                                         definition='De testresultaten van een afschermende constructie.')

        self._uitvoeringscertificatie = OTLAttribuut(field=DtcDocument,
                                                     naam='uitvoeringscertificatie',
                                                     label='uitvoeringscertificatie',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie.uitvoeringscertificatie',
                                                     usagenote='Bestanden van het type xlsx of pdf.',
                                                     definition='Documentatie van het certificaat.')

        self._video = OTLAttribuut(field=DtcDocument,
                                   naam='video',
                                   label='video',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie.video',
                                   usagenote='Attribuut uit gebruik sinds versie 2.0.0 .Enkel videobestanden zijn toegelaten.',
                                   deprecated_version='2.0.0',
                                   kardinaliteit_max='*',
                                   definition='Video van de testen op afschermende constructies.')

    @property
    def certificaathouder(self):
        """De houder van het uitvoeringscertificaat."""
        return self._certificaathouder.waarde

    @certificaathouder.setter
    def certificaathouder(self, value):
        self._certificaathouder.set_waarde(value, owner=self)

    @property
    def isPermanent(self):
        """Vermelding of de afschermende constructie al dan niet van permanente aard is."""
        return self._isPermanent.waarde

    @isPermanent.setter
    def isPermanent(self, value):
        self._isPermanent.set_waarde(value, owner=self)

    @property
    def materiaal(self):
        """Het gebruikte materiaal voor de afschermende constructie."""
        return self._materiaal.waarde

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def metTandGroef(self):
        """Geeft aan of de afschermende constructie bevestigd is aan de onderliggende laag door middel van een tand-groef aansluiting."""
        return self._metTandGroef.waarde

    @metTandGroef.setter
    def metTandGroef(self, value):
        self._metTandGroef.set_waarde(value, owner=self)

    @property
    def productidentificatiecode(self):
        """De productidentificatiecode voor het bepalen van de code van het gebruikte product (bv. COPRO/BENOR)."""
        return self._productidentificatiecode.waarde

    @productidentificatiecode.setter
    def productidentificatiecode(self, value):
        self._productidentificatiecode.set_waarde(value, owner=self)

    @property
    def productnaam(self):
        """Dit is de commerciële naam van de afschermende constructie."""
        return self._productnaam.waarde

    @productnaam.setter
    def productnaam(self, value):
        self._productnaam.set_waarde(value, owner=self)

    @property
    def testrapport(self):
        """De testresultaten van een afschermende constructie."""
        return self._testrapport.waarde

    @testrapport.setter
    def testrapport(self, value):
        self._testrapport.set_waarde(value, owner=self)

    @property
    def uitvoeringscertificatie(self):
        """Documentatie van het certificaat."""
        return self._uitvoeringscertificatie.waarde

    @uitvoeringscertificatie.setter
    def uitvoeringscertificatie(self, value):
        self._uitvoeringscertificatie.set_waarde(value, owner=self)

    @property
    def video(self):
        """Video van de testen op afschermende constructies."""
        return self._video.waarde

    @video.setter
    def video(self, value):
        self._video.set_waarde(value, owner=self)
