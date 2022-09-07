# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.Abstracten.BijlageVoertuigkering import BijlageVoertuigkering
from OTLMOW.OTLModel.Classes.Abstracten.LijnvormigElement import LijnvormigElement
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.DtcProductidentificatiecode import DtcProductidentificatiecode
from OTLMOW.OTLModel.Datatypes.KlLEACMateriaal import KlLEACMateriaal
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class AfschermendeConstructie(BijlageVoertuigkering, LijnvormigElement):
    """Abstracte die een lijn- of puntvormige constructie,geïnstalleerd langs de weg om een kerend vermogen te bieden aan een dwalend voertuig,samenvat."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        BijlageVoertuigkering.__init__(self)
        LijnvormigElement.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie', deprecated='2.0.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Referentiepunt')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WegbebakeningAfschermendeConstructies')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie', deprecated='2.0.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoertuigkerendGeluidsschermelement')

        self._certificaathouder = OTLAttribuut(field=StringField,
                                               naam='certificaathouder',
                                               label='certificaathouder',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie.certificaathouder',
                                               definition='De houder van het uitvoeringscertificaat.',
                                               owner=self)

        self._isPermanent = OTLAttribuut(field=BooleanField,
                                         naam='isPermanent',
                                         label='is permanent',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie.isPermanent',
                                         definition='Vermelding of de afschermende constructie al dan niet van permanente aard is.',
                                         owner=self)

        self._materiaal = OTLAttribuut(field=KlLEACMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie.materiaal',
                                       definition='Het gebruikte materiaal voor de afschermende constructie.',
                                       owner=self)

        self._metTandGroef = OTLAttribuut(field=BooleanField,
                                          naam='metTandGroef',
                                          label='met tand-groef',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie.metTandGroef',
                                          definition='Geeft aan of de afschermende constructie bevestigd is aan de onderliggende laag door middel van een tand-groef aansluiting.',
                                          owner=self)

        self._productidentificatiecode = OTLAttribuut(field=DtcProductidentificatiecode,
                                                      naam='productidentificatiecode',
                                                      label='productidentificatiecode',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie.productidentificatiecode',
                                                      definition='De productidentificatiecode voor het bepalen van de code van het gebruikte product (bv. COPRO/BENOR).',
                                                      owner=self)

        self._productnaam = OTLAttribuut(field=StringField,
                                         naam='productnaam',
                                         label='productnaam',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie.productnaam',
                                         definition='Dit is de commerciële naam van de afschermende constructie.',
                                         owner=self)

        self._testrapport = OTLAttribuut(field=DtcDocument,
                                         naam='testrapport',
                                         label='testrapport',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie.testrapport',
                                         usagenote='Attribuut uit gebruik sinds versie 2.0.0 ',
                                         deprecated_version='2.0.0',
                                         kardinaliteit_max='*',
                                         definition='De testresultaten van een afschermende constructie.',
                                         owner=self)

        self._uitvoeringscertificatie = OTLAttribuut(field=DtcDocument,
                                                     naam='uitvoeringscertificatie',
                                                     label='uitvoeringscertificatie',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie.uitvoeringscertificatie',
                                                     usagenote='Bestanden van het type xlsx of pdf.',
                                                     definition='Documentatie van het certificaat.',
                                                     owner=self)

        self._video = OTLAttribuut(field=DtcDocument,
                                   naam='video',
                                   label='video',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie.video',
                                   usagenote='Attribuut uit gebruik sinds versie 2.0.0 ',
                                   deprecated_version='2.0.0',
                                   kardinaliteit_max='*',
                                   definition='Video van de testen op afschermende constructies.',
                                   owner=self)

    @property
    def certificaathouder(self):
        """De houder van het uitvoeringscertificaat."""
        return self._certificaathouder.get_waarde()

    @certificaathouder.setter
    def certificaathouder(self, value):
        self._certificaathouder.set_waarde(value, owner=self)

    @property
    def isPermanent(self):
        """Vermelding of de afschermende constructie al dan niet van permanente aard is."""
        return self._isPermanent.get_waarde()

    @isPermanent.setter
    def isPermanent(self, value):
        self._isPermanent.set_waarde(value, owner=self)

    @property
    def materiaal(self):
        """Het gebruikte materiaal voor de afschermende constructie."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def metTandGroef(self):
        """Geeft aan of de afschermende constructie bevestigd is aan de onderliggende laag door middel van een tand-groef aansluiting."""
        return self._metTandGroef.get_waarde()

    @metTandGroef.setter
    def metTandGroef(self, value):
        self._metTandGroef.set_waarde(value, owner=self)

    @property
    def productidentificatiecode(self):
        """De productidentificatiecode voor het bepalen van de code van het gebruikte product (bv. COPRO/BENOR)."""
        return self._productidentificatiecode.get_waarde()

    @productidentificatiecode.setter
    def productidentificatiecode(self, value):
        self._productidentificatiecode.set_waarde(value, owner=self)

    @property
    def productnaam(self):
        """Dit is de commerciële naam van de afschermende constructie."""
        return self._productnaam.get_waarde()

    @productnaam.setter
    def productnaam(self, value):
        self._productnaam.set_waarde(value, owner=self)

    @property
    def testrapport(self):
        """De testresultaten van een afschermende constructie."""
        return self._testrapport.get_waarde()

    @testrapport.setter
    def testrapport(self, value):
        self._testrapport.set_waarde(value, owner=self)

    @property
    def uitvoeringscertificatie(self):
        """Documentatie van het certificaat."""
        return self._uitvoeringscertificatie.get_waarde()

    @uitvoeringscertificatie.setter
    def uitvoeringscertificatie(self, value):
        self._uitvoeringscertificatie.set_waarde(value, owner=self)

    @property
    def video(self):
        """Video van de testen op afschermende constructies."""
        return self._video.get_waarde()

    @video.setter
    def video(self, value):
        self._video.set_waarde(value, owner=self)
