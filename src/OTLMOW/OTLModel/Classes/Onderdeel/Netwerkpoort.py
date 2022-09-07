# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.IntegerField import IntegerField
from OTLMOW.OTLModel.Datatypes.KlNetwerkMerk import KlNetwerkMerk
from OTLMOW.OTLModel.Datatypes.KlNetwerkTechnologie import KlNetwerkTechnologie
from OTLMOW.OTLModel.Datatypes.KlNetwerkpoortConfig import KlNetwerkpoortConfig
from OTLMOW.OTLModel.Datatypes.KlNetwerkpoortGolflengte import KlNetwerkpoortGolflengte
from OTLMOW.OTLModel.Datatypes.KlNetwerkpoortType import KlNetwerkpoortType
from OTLMOW.OTLModel.Datatypes.StringField import StringField
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Netwerkpoort(AIMNaamObject, PuntGeometrie):
    """De ingang van het toestel samen met component die erop zit,bv. SFP of XFP."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkkaart')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Link')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pad')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VLAN')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Zpad')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Controller')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HardwareToegang')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SoftwareToegang')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Flitspaal')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AIDModule')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afmetingsensor')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordExternePU')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVLuskaart')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVProcessorkaart')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Neerslagsensor')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omvormer')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WIMDatalogger')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IpPowerSwitch')

        self._beschrijvingFabrikant = OTLAttribuut(field=StringField,
                                                   naam='beschrijvingFabrikant',
                                                   label='beschrijving fabrikant',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort.beschrijvingFabrikant',
                                                   definition='Bijkomende specificaties over het apparaat of onderdeel type van de fabrikant.',
                                                   owner=self)

        self._code = OTLAttribuut(field=StringField,
                                  naam='code',
                                  label='code',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort.code',
                                  definition='Bestelcode van dit toestel of onderdeel bij de fabrikant.',
                                  owner=self)

        self._config = OTLAttribuut(field=KlNetwerkpoortConfig,
                                    naam='config',
                                    label='config',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort.config',
                                    definition='Soort verbinding aangeboden aan de klant.',
                                    owner=self)

        self._golflengte = OTLAttribuut(field=KlNetwerkpoortGolflengte,
                                        naam='golflengte',
                                        label='golflengte',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort.golflengte',
                                        definition='De golflengte waarop deze poort communiceert.',
                                        owner=self)

        self._merk = OTLAttribuut(field=KlNetwerkMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort.merk',
                                  definition='Merk waarmee de fabrikant de netwerkpoort identificeert.',
                                  owner=self)

        self._nNILANCapaciteit = OTLAttribuut(field=IntegerField,
                                              naam='nNILANCapaciteit',
                                              label='NNI LAN-capaciteit',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort.nNILANCapaciteit',
                                              definition='Bandbreedte via deze poort, uitgedrukt in Mb/s, enkel van toepassing indien NNI poort.',
                                              owner=self)

        self._serienummer = OTLAttribuut(field=StringField,
                                         naam='serienummer',
                                         label='serienummer',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort.serienummer',
                                         definition='Unieke identificatiecode van het toestel, toegekend door de fabrikant.',
                                         owner=self)

        self._technologie = OTLAttribuut(field=KlNetwerkTechnologie,
                                         naam='technologie',
                                         label='technologie',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort.technologie',
                                         definition='Intern gebruikt netwerk protocol.',
                                         owner=self)

        self._type = OTLAttribuut(field=KlNetwerkpoortType,
                                  naam='type',
                                  label='model',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort.type',
                                  definition='Geeft het soort netwerk interface weer.',
                                  owner=self)

    @property
    def beschrijvingFabrikant(self):
        """Bijkomende specificaties over het apparaat of onderdeel type van de fabrikant."""
        return self._beschrijvingFabrikant.get_waarde()

    @beschrijvingFabrikant.setter
    def beschrijvingFabrikant(self, value):
        self._beschrijvingFabrikant.set_waarde(value, owner=self)

    @property
    def code(self):
        """Bestelcode van dit toestel of onderdeel bij de fabrikant."""
        return self._code.get_waarde()

    @code.setter
    def code(self, value):
        self._code.set_waarde(value, owner=self)

    @property
    def config(self):
        """Soort verbinding aangeboden aan de klant."""
        return self._config.get_waarde()

    @config.setter
    def config(self, value):
        self._config.set_waarde(value, owner=self)

    @property
    def golflengte(self):
        """De golflengte waarop deze poort communiceert."""
        return self._golflengte.get_waarde()

    @golflengte.setter
    def golflengte(self, value):
        self._golflengte.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Merk waarmee de fabrikant de netwerkpoort identificeert."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def nNILANCapaciteit(self):
        """Bandbreedte via deze poort, uitgedrukt in Mb/s, enkel van toepassing indien NNI poort."""
        return self._nNILANCapaciteit.get_waarde()

    @nNILANCapaciteit.setter
    def nNILANCapaciteit(self, value):
        self._nNILANCapaciteit.set_waarde(value, owner=self)

    @property
    def serienummer(self):
        """Unieke identificatiecode van het toestel, toegekend door de fabrikant."""
        return self._serienummer.get_waarde()

    @serienummer.setter
    def serienummer(self, value):
        self._serienummer.set_waarde(value, owner=self)

    @property
    def technologie(self):
        """Intern gebruikt netwerk protocol."""
        return self._technologie.get_waarde()

    @technologie.setter
    def technologie(self, value):
        self._technologie.set_waarde(value, owner=self)

    @property
    def type(self):
        """Geeft het soort netwerk interface weer."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
