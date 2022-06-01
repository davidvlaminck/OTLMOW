# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.DtcBereikInKg import DtcBereikInKg
from OTLMOW.OTLModel.Datatypes.DtcKwaliteitscertifcaat import DtcKwaliteitscertifcaat
from OTLMOW.OTLModel.Datatypes.KlAfmetingAswegerzone import KlAfmetingAswegerzone
from OTLMOW.OTLModel.Datatypes.KlAswegersiteTypeMarkering import KlAswegersiteTypeMarkering


# Generated with OTLClassCreator. To modify: extend, do not edit
class Aswegersite(AIMNaamObject):
    """Het geheel van infrastructuurelementen en toestellen op één locatie voor de exploitatie van een asweger."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aswegersite'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._afmetingAswegerZone = OTLAttribuut(field=KlAfmetingAswegerzone,
                                                 naam='afmetingAswegerZone',
                                                 label='afmeting aswegerzone',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aswegersite.afmetingAswegerZone',
                                                 definition='De afmeting van de zone voor en na de weegplaat, inclusief de weegplaat zelf, als een waarde uit een vaste lijst van standaard afmetingen.',
                                                 owner=self)

        self._kwaliteitscertificaat = OTLAttribuut(field=DtcKwaliteitscertifcaat,
                                                   naam='kwaliteitscertificaat',
                                                   label='kwaliteitscertificaat',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aswegersite.kwaliteitscertificaat',
                                                   definition='Het certificaat uitgereikt bij de eerste ijk nodig voor de rechtsgeldige uitbating van de aswegersite.',
                                                   owner=self)

        self._typeMarkering = OTLAttribuut(field=KlAswegersiteTypeMarkering,
                                           naam='typeMarkering',
                                           label='type markering',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aswegersite.typeMarkering',
                                           definition='Geeft welke wegmarkering er aanwezig zijn rond de aswegerzone als een waarde uit een vaste lijst van mogelijkheden.',
                                           owner=self)

        self._weegvermogenBereik = OTLAttribuut(field=DtcBereikInKg,
                                                naam='weegvermogenBereik',
                                                label='weegvermogen bereik',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aswegersite.weegvermogenBereik',
                                                definition='Het bereik (gewicht) dat de asweger kan wegen, uitgedrukt in kilo.',
                                                owner=self)

    @property
    def afmetingAswegerZone(self):
        """De afmeting van de zone voor en na de weegplaat, inclusief de weegplaat zelf, als een waarde uit een vaste lijst van standaard afmetingen."""
        return self._afmetingAswegerZone.get_waarde()

    @afmetingAswegerZone.setter
    def afmetingAswegerZone(self, value):
        self._afmetingAswegerZone.set_waarde(value, owner=self)

    @property
    def kwaliteitscertificaat(self):
        """Het certificaat uitgereikt bij de eerste ijk nodig voor de rechtsgeldige uitbating van de aswegersite."""
        return self._kwaliteitscertificaat.get_waarde()

    @kwaliteitscertificaat.setter
    def kwaliteitscertificaat(self, value):
        self._kwaliteitscertificaat.set_waarde(value, owner=self)

    @property
    def typeMarkering(self):
        """Geeft welke wegmarkering er aanwezig zijn rond de aswegerzone als een waarde uit een vaste lijst van mogelijkheden."""
        return self._typeMarkering.get_waarde()

    @typeMarkering.setter
    def typeMarkering(self, value):
        self._typeMarkering.set_waarde(value, owner=self)

    @property
    def weegvermogenBereik(self):
        """Het bereik (gewicht) dat de asweger kan wegen, uitgedrukt in kilo."""
        return self._weegvermogenBereik.get_waarde()

    @weegvermogenBereik.setter
    def weegvermogenBereik(self, value):
        self._weegvermogenBereik.set_waarde(value, owner=self)
