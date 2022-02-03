# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class TGC(EMObject):
    """Toegangscontrole (gedeelte waarvoor de onderhoudsaannemer dient tussen te komen)"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#TGC'
    label = 'Toegangscontrole aannemer'

    def __init__(self):
        super().__init__()

        self._ap1001ReaderAantal = EMAttribuut(field=FloatOrDecimalField,
                                               naam='AP1001 (reader) aantal',
                                               label='AP1001 (reader) aantal',
                                               objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.ap1001ReaderAantal',
                                               definitie='Definitie nog toe te voegen voor eigenschap AP1001 (reader) aantal',
                                               owner=self)

        self._ap1009DualReaderAantal = EMAttribuut(field=FloatOrDecimalField,
                                                   naam='AP1009 (dual reader) aantal',
                                                   label='AP1009 (dual reader) aantal',
                                                   objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.ap1009DualReaderAantal',
                                                   definitie='Definitie nog toe te voegen voor eigenschap AP1009 (dual reader) aantal',
                                                   owner=self)

        self._ap2001VoedingAantal = EMAttribuut(field=FloatOrDecimalField,
                                                naam='AP2001 (voeding) aantal',
                                                label='AP2001 (voeding) aantal',
                                                objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.ap2001VoedingAantal',
                                                definitie='Definitie nog toe te voegen voor eigenschap AP2001 (voeding) aantal',
                                                owner=self)

        self._ap3002InputEenheidAantal = EMAttribuut(field=FloatOrDecimalField,
                                                     naam='AP3002 (input eenheid) aantal',
                                                     label='AP3002 (input eenheid) aantal',
                                                     objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.ap3002InputEenheidAantal',
                                                     definitie='Definitie nog toe te voegen voor eigenschap AP3002 (input eenheid) aantal',
                                                     owner=self)

        self._ap3004OutputEenheidAantal = EMAttribuut(field=FloatOrDecimalField,
                                                      naam='AP3004 (output eenheid) aantal',
                                                      label='AP3004 (output eenheid) aantal',
                                                      objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.ap3004OutputEenheidAantal',
                                                      definitie='Definitie nog toe te voegen voor eigenschap AP3004 (output eenheid) aantal',
                                                      owner=self)

        self._ap7803BlueTechnologieAantal = EMAttribuut(field=FloatOrDecimalField,
                                                        naam='AP7803 (blue technologie) aantal',
                                                        label='AP7803 (blue technologie) aantal',
                                                        objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.ap7803BlueTechnologieAantal',
                                                        definitie='Definitie nog toe te voegen voor eigenschap AP7803 (blue technologie) aantal',
                                                        owner=self)

        self._ap8001ControleEenheidAantal = EMAttribuut(field=FloatOrDecimalField,
                                                        naam='AP8001 (controle eenheid) aantal',
                                                        label='AP8001 (controle eenheid) aantal',
                                                        objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.ap8001ControleEenheidAantal',
                                                        definitie='Definitie nog toe te voegen voor eigenschap AP8001 (controle eenheid) aantal',
                                                        owner=self)

        self._rioRemoteInputOutputAantal = EMAttribuut(field=FloatOrDecimalField,
                                                       naam='RIO (remote input output) aantal',
                                                       label='RIO (remote input output) aantal',
                                                       objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.rioRemoteInputOutputAantal',
                                                       definitie='Definitie nog toe te voegen voor eigenschap RIO (remote input output) aantal',
                                                       owner=self)

        self._andere = EMAttribuut(field=StringField,
                                   naam='andere',
                                   label='andere',
                                   objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.andere',
                                   definitie='Definitie nog toe te voegen voor eigenschap andere',
                                   owner=self)

        self._apparatuurOpslagCameraBeeldenAantal = EMAttribuut(field=FloatOrDecimalField,
                                                                naam='apparatuur opslag camera beelden aantal',
                                                                label='apparatuur opslag camera beelden aantal',
                                                                objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.apparatuurOpslagCameraBeeldenAantal',
                                                                definitie='Definitie nog toe te voegen voor eigenschap apparatuur opslag camera beelden aantal',
                                                                owner=self)

        self._apparatuurOpslagCameraBeeldenType = EMAttribuut(field=StringField,
                                                              naam='apparatuur opslag camera beelden type',
                                                              label='apparatuur opslag camera beelden type',
                                                              objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.apparatuurOpslagCameraBeeldenType',
                                                              definitie='Definitie nog toe te voegen voor eigenschap apparatuur opslag camera beelden type',
                                                              owner=self)

        self._automaatNummer = EMAttribuut(field=StringField,
                                           naam='automaat nummer',
                                           label='automaat nummer',
                                           objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.automaatNummer',
                                           definitie='Definitie nog toe te voegen voor eigenschap automaat nummer',
                                           owner=self)

        self._automatischeDeursluiterAantal = EMAttribuut(field=FloatOrDecimalField,
                                                          naam='automatische deursluiter aantal',
                                                          label='automatische deursluiter aantal',
                                                          objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.automatischeDeursluiterAantal',
                                                          definitie='Definitie nog toe te voegen voor eigenschap automatische deursluiter aantal',
                                                          owner=self)

        self._batterijAantal = EMAttribuut(field=FloatOrDecimalField,
                                           naam='batterij aantal',
                                           label='batterij aantal',
                                           objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.batterijAantal',
                                           definitie='Definitie nog toe te voegen voor eigenschap batterij aantal',
                                           owner=self)

        self._bewakingAircoAantal = EMAttribuut(field=FloatOrDecimalField,
                                                naam='bewaking airco aantal',
                                                label='bewaking airco aantal',
                                                objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.bewakingAircoAantal',
                                                definitie='Definitie nog toe te voegen voor eigenschap bewaking airco aantal',
                                                owner=self)

        self._bewakingVerlichtingAantal = EMAttribuut(field=FloatOrDecimalField,
                                                      naam='bewaking verlichting aantal',
                                                      label='bewaking verlichting aantal',
                                                      objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.bewakingVerlichtingAantal',
                                                      definitie='Definitie nog toe te voegen voor eigenschap bewaking verlichting aantal',
                                                      owner=self)

        self._bewegingsdetectorAantal = EMAttribuut(field=FloatOrDecimalField,
                                                    naam='bewegingsdetector aantal',
                                                    label='bewegingsdetector aantal',
                                                    objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.bewegingsdetectorAantal',
                                                    definitie='Definitie nog toe te voegen voor eigenschap bewegingsdetector aantal',
                                                    owner=self)

        self._buitensireneAantal = EMAttribuut(field=FloatOrDecimalField,
                                               naam='buitensirene aantal',
                                               label='buitensirene aantal',
                                               objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.buitensireneAantal',
                                               definitie='Definitie nog toe te voegen voor eigenschap buitensirene aantal',
                                               owner=self)

        self._cameraAantal = EMAttribuut(field=FloatOrDecimalField,
                                         naam='camera aantal',
                                         label='camera aantal',
                                         objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.cameraAantal',
                                         definitie='Definitie nog toe te voegen voor eigenschap camera aantal',
                                         owner=self)

        self._cameraType = EMAttribuut(field=StringField,
                                       naam='camera type',
                                       label='camera type',
                                       objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.cameraType',
                                       definitie='Definitie nog toe te voegen voor eigenschap camera type',
                                       owner=self)

        self._centrServerToepassingssoftwareVersie = EMAttribuut(field=StringField,
                                                                 naam='centr server toepassingssoftware versie',
                                                                 label='centr server toepassingssoftware versie',
                                                                 objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.centrServerToepassingssoftwareVersie',
                                                                 definitie='Definitie nog toe te voegen voor eigenschap centr server toepassingssoftware versie',
                                                                 owner=self)

        self._centraleServerHardwareAantal = EMAttribuut(field=FloatOrDecimalField,
                                                         naam='centrale server hardware aantal',
                                                         label='centrale server hardware aantal',
                                                         objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.centraleServerHardwareAantal',
                                                         definitie='Definitie nog toe te voegen voor eigenschap centrale server hardware aantal',
                                                         owner=self)

        self._centraleServerHardwareType = EMAttribuut(field=StringField,
                                                       naam='centrale server hardware type',
                                                       label='centrale server hardware type',
                                                       objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.centraleServerHardwareType',
                                                       definitie='Definitie nog toe te voegen voor eigenschap centrale server hardware type',
                                                       owner=self)

        self._centraleServerOperatingsoftwareVersie = EMAttribuut(field=StringField,
                                                                  naam='centrale server operatingsoftware versie',
                                                                  label='centrale server operatingsoftware versie',
                                                                  objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.centraleServerOperatingsoftwareVersie',
                                                                  definitie='Definitie nog toe te voegen voor eigenschap centrale server operatingsoftware versie',
                                                                  owner=self)

        self._centraleServerTypeOperatingSoftware = EMAttribuut(field=BooleanField,
                                                                naam='centrale server type> operating software',
                                                                label='centrale server type> operating software',
                                                                objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.centraleServerTypeOperatingSoftware',
                                                                definitie='Definitie nog toe te voegen voor eigenschap centrale server type> operating software',
                                                                owner=self)

        self._centraleServerTypeToepassingssoftware = EMAttribuut(field=BooleanField,
                                                                  naam='centrale server type>toepassingssoftware',
                                                                  label='centrale server type>toepassingssoftware',
                                                                  objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.centraleServerTypeToepassingssoftware',
                                                                  definitie='Definitie nog toe te voegen voor eigenschap centrale server type>toepassingssoftware',
                                                                  owner=self)

        self._codeklavierAantal = EMAttribuut(field=FloatOrDecimalField,
                                              naam='codeklavier aantal',
                                              label='codeklavier aantal',
                                              objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.codeklavierAantal',
                                              definitie='Definitie nog toe te voegen voor eigenschap codeklavier aantal',
                                              owner=self)

        self._deurslotMeerpuntsIseoCilinderAantal = EMAttribuut(field=FloatOrDecimalField,
                                                                naam='deurslot meerpunts+ISEO cilinder aantal',
                                                                label='deurslot meerpunts+ISEO cilinder aantal',
                                                                objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.deurslotMeerpuntsIseoCilinderAantal',
                                                                definitie='Definitie nog toe te voegen voor eigenschap deurslot meerpunts+ISEO cilinder aantal',
                                                                owner=self)

        self._deurslotMotorischeCilEmvy3ksAantal = EMAttribuut(field=FloatOrDecimalField,
                                                               naam='deurslot motorische cil(EMVY 3KS) aantal',
                                                               label='deurslot motorische cil(EMVY 3KS) aantal',
                                                               objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.deurslotMotorischeCilEmvy3ksAantal',
                                                               definitie='Definitie nog toe te voegen voor eigenschap deurslot motorische cil(EMVY 3KS) aantal',
                                                               owner=self)

        self._inbraakcentraleAantal = EMAttribuut(field=FloatOrDecimalField,
                                                  naam='inbraakcentrale aantal',
                                                  label='inbraakcentrale aantal',
                                                  objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.inbraakcentraleAantal',
                                                  definitie='Definitie nog toe te voegen voor eigenschap inbraakcentrale aantal',
                                                  owner=self)

        self._inbraakcentraleType = EMAttribuut(field=StringField,
                                                naam='inbraakcentrale type',
                                                label='inbraakcentrale type',
                                                objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.inbraakcentraleType',
                                                definitie='Definitie nog toe te voegen voor eigenschap inbraakcentrale type',
                                                owner=self)

        self._kaartlezerAantal = EMAttribuut(field=FloatOrDecimalField,
                                             naam='kaartlezer aantal',
                                             label='kaartlezer aantal',
                                             objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.kaartlezerAantal',
                                             definitie='Definitie nog toe te voegen voor eigenschap kaartlezer aantal',
                                             owner=self)

        self._magneetcontactenAantal = EMAttribuut(field=FloatOrDecimalField,
                                                   naam='magneetcontacten aantal',
                                                   label='magneetcontacten aantal',
                                                   objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.magneetcontactenAantal',
                                                   definitie='Definitie nog toe te voegen voor eigenschap magneetcontacten aantal',
                                                   owner=self)

        self._noodverlichtingAantal = EMAttribuut(field=FloatOrDecimalField,
                                                  naam='noodverlichting aantal',
                                                  label='noodverlichting aantal',
                                                  objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.noodverlichtingAantal',
                                                  definitie='Definitie nog toe te voegen voor eigenschap noodverlichting aantal',
                                                  owner=self)

        self._notitieinspectie = EMAttribuut(field=StringField,
                                             naam='notitieInspectie',
                                             label='notitieInspectie',
                                             objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.notitieinspectie',
                                             definitie='Definitie nog toe te voegen voor eigenschap notitie',
                                             owner=self)

        self._opmerkingenBijOnderhoud = EMAttribuut(field=StringField,
                                                    naam='opmerkingen bij onderhoud',
                                                    label='opmerkingen bij onderhoud',
                                                    objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.opmerkingenBijOnderhoud',
                                                    definitie='Definitie nog toe te voegen voor eigenschap opmerkingen bij onderhoud',
                                                    owner=self)

        self._resultaatOnderhoud = EMAttribuut(field=StringField,
                                               naam='resultaat onderhoud',
                                               label='resultaat onderhoud',
                                               objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.resultaatOnderhoud',
                                               definitie='Definitie nog toe te voegen voor eigenschap resultaat onderhoud',
                                               owner=self)

        self._rookmeldersAantal = EMAttribuut(field=FloatOrDecimalField,
                                              naam='rookmelders aantal',
                                              label='rookmelders aantal',
                                              objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.rookmeldersAantal',
                                              definitie='Definitie nog toe te voegen voor eigenschap rookmelders aantal',
                                              owner=self)

    @property
    def ap1001ReaderAantal(self):
        """Definitie nog toe te voegen voor eigenschap AP1001 (reader) aantal"""
        return self._ap1001ReaderAantal.waarde

    @ap1001ReaderAantal.setter
    def ap1001ReaderAantal(self, value):
        self._ap1001ReaderAantal.set_waarde(value, owner=self)

    @property
    def ap1009DualReaderAantal(self):
        """Definitie nog toe te voegen voor eigenschap AP1009 (dual reader) aantal"""
        return self._ap1009DualReaderAantal.waarde

    @ap1009DualReaderAantal.setter
    def ap1009DualReaderAantal(self, value):
        self._ap1009DualReaderAantal.set_waarde(value, owner=self)

    @property
    def ap2001VoedingAantal(self):
        """Definitie nog toe te voegen voor eigenschap AP2001 (voeding) aantal"""
        return self._ap2001VoedingAantal.waarde

    @ap2001VoedingAantal.setter
    def ap2001VoedingAantal(self, value):
        self._ap2001VoedingAantal.set_waarde(value, owner=self)

    @property
    def ap3002InputEenheidAantal(self):
        """Definitie nog toe te voegen voor eigenschap AP3002 (input eenheid) aantal"""
        return self._ap3002InputEenheidAantal.waarde

    @ap3002InputEenheidAantal.setter
    def ap3002InputEenheidAantal(self, value):
        self._ap3002InputEenheidAantal.set_waarde(value, owner=self)

    @property
    def ap3004OutputEenheidAantal(self):
        """Definitie nog toe te voegen voor eigenschap AP3004 (output eenheid) aantal"""
        return self._ap3004OutputEenheidAantal.waarde

    @ap3004OutputEenheidAantal.setter
    def ap3004OutputEenheidAantal(self, value):
        self._ap3004OutputEenheidAantal.set_waarde(value, owner=self)

    @property
    def ap7803BlueTechnologieAantal(self):
        """Definitie nog toe te voegen voor eigenschap AP7803 (blue technologie) aantal"""
        return self._ap7803BlueTechnologieAantal.waarde

    @ap7803BlueTechnologieAantal.setter
    def ap7803BlueTechnologieAantal(self, value):
        self._ap7803BlueTechnologieAantal.set_waarde(value, owner=self)

    @property
    def ap8001ControleEenheidAantal(self):
        """Definitie nog toe te voegen voor eigenschap AP8001 (controle eenheid) aantal"""
        return self._ap8001ControleEenheidAantal.waarde

    @ap8001ControleEenheidAantal.setter
    def ap8001ControleEenheidAantal(self, value):
        self._ap8001ControleEenheidAantal.set_waarde(value, owner=self)

    @property
    def rioRemoteInputOutputAantal(self):
        """Definitie nog toe te voegen voor eigenschap RIO (remote input output) aantal"""
        return self._rioRemoteInputOutputAantal.waarde

    @rioRemoteInputOutputAantal.setter
    def rioRemoteInputOutputAantal(self, value):
        self._rioRemoteInputOutputAantal.set_waarde(value, owner=self)

    @property
    def andere(self):
        """Definitie nog toe te voegen voor eigenschap andere"""
        return self._andere.waarde

    @andere.setter
    def andere(self, value):
        self._andere.set_waarde(value, owner=self)

    @property
    def apparatuurOpslagCameraBeeldenAantal(self):
        """Definitie nog toe te voegen voor eigenschap apparatuur opslag camera beelden aantal"""
        return self._apparatuurOpslagCameraBeeldenAantal.waarde

    @apparatuurOpslagCameraBeeldenAantal.setter
    def apparatuurOpslagCameraBeeldenAantal(self, value):
        self._apparatuurOpslagCameraBeeldenAantal.set_waarde(value, owner=self)

    @property
    def apparatuurOpslagCameraBeeldenType(self):
        """Definitie nog toe te voegen voor eigenschap apparatuur opslag camera beelden type"""
        return self._apparatuurOpslagCameraBeeldenType.waarde

    @apparatuurOpslagCameraBeeldenType.setter
    def apparatuurOpslagCameraBeeldenType(self, value):
        self._apparatuurOpslagCameraBeeldenType.set_waarde(value, owner=self)

    @property
    def automaatNummer(self):
        """Definitie nog toe te voegen voor eigenschap automaat nummer"""
        return self._automaatNummer.waarde

    @automaatNummer.setter
    def automaatNummer(self, value):
        self._automaatNummer.set_waarde(value, owner=self)

    @property
    def automatischeDeursluiterAantal(self):
        """Definitie nog toe te voegen voor eigenschap automatische deursluiter aantal"""
        return self._automatischeDeursluiterAantal.waarde

    @automatischeDeursluiterAantal.setter
    def automatischeDeursluiterAantal(self, value):
        self._automatischeDeursluiterAantal.set_waarde(value, owner=self)

    @property
    def batterijAantal(self):
        """Definitie nog toe te voegen voor eigenschap batterij aantal"""
        return self._batterijAantal.waarde

    @batterijAantal.setter
    def batterijAantal(self, value):
        self._batterijAantal.set_waarde(value, owner=self)

    @property
    def bewakingAircoAantal(self):
        """Definitie nog toe te voegen voor eigenschap bewaking airco aantal"""
        return self._bewakingAircoAantal.waarde

    @bewakingAircoAantal.setter
    def bewakingAircoAantal(self, value):
        self._bewakingAircoAantal.set_waarde(value, owner=self)

    @property
    def bewakingVerlichtingAantal(self):
        """Definitie nog toe te voegen voor eigenschap bewaking verlichting aantal"""
        return self._bewakingVerlichtingAantal.waarde

    @bewakingVerlichtingAantal.setter
    def bewakingVerlichtingAantal(self, value):
        self._bewakingVerlichtingAantal.set_waarde(value, owner=self)

    @property
    def bewegingsdetectorAantal(self):
        """Definitie nog toe te voegen voor eigenschap bewegingsdetector aantal"""
        return self._bewegingsdetectorAantal.waarde

    @bewegingsdetectorAantal.setter
    def bewegingsdetectorAantal(self, value):
        self._bewegingsdetectorAantal.set_waarde(value, owner=self)

    @property
    def buitensireneAantal(self):
        """Definitie nog toe te voegen voor eigenschap buitensirene aantal"""
        return self._buitensireneAantal.waarde

    @buitensireneAantal.setter
    def buitensireneAantal(self, value):
        self._buitensireneAantal.set_waarde(value, owner=self)

    @property
    def cameraAantal(self):
        """Definitie nog toe te voegen voor eigenschap camera aantal"""
        return self._cameraAantal.waarde

    @cameraAantal.setter
    def cameraAantal(self, value):
        self._cameraAantal.set_waarde(value, owner=self)

    @property
    def cameraType(self):
        """Definitie nog toe te voegen voor eigenschap camera type"""
        return self._cameraType.waarde

    @cameraType.setter
    def cameraType(self, value):
        self._cameraType.set_waarde(value, owner=self)

    @property
    def centrServerToepassingssoftwareVersie(self):
        """Definitie nog toe te voegen voor eigenschap centr server toepassingssoftware versie"""
        return self._centrServerToepassingssoftwareVersie.waarde

    @centrServerToepassingssoftwareVersie.setter
    def centrServerToepassingssoftwareVersie(self, value):
        self._centrServerToepassingssoftwareVersie.set_waarde(value, owner=self)

    @property
    def centraleServerHardwareAantal(self):
        """Definitie nog toe te voegen voor eigenschap centrale server hardware aantal"""
        return self._centraleServerHardwareAantal.waarde

    @centraleServerHardwareAantal.setter
    def centraleServerHardwareAantal(self, value):
        self._centraleServerHardwareAantal.set_waarde(value, owner=self)

    @property
    def centraleServerHardwareType(self):
        """Definitie nog toe te voegen voor eigenschap centrale server hardware type"""
        return self._centraleServerHardwareType.waarde

    @centraleServerHardwareType.setter
    def centraleServerHardwareType(self, value):
        self._centraleServerHardwareType.set_waarde(value, owner=self)

    @property
    def centraleServerOperatingsoftwareVersie(self):
        """Definitie nog toe te voegen voor eigenschap centrale server operatingsoftware versie"""
        return self._centraleServerOperatingsoftwareVersie.waarde

    @centraleServerOperatingsoftwareVersie.setter
    def centraleServerOperatingsoftwareVersie(self, value):
        self._centraleServerOperatingsoftwareVersie.set_waarde(value, owner=self)

    @property
    def centraleServerTypeOperatingSoftware(self):
        """Definitie nog toe te voegen voor eigenschap centrale server type> operating software"""
        return self._centraleServerTypeOperatingSoftware.waarde

    @centraleServerTypeOperatingSoftware.setter
    def centraleServerTypeOperatingSoftware(self, value):
        self._centraleServerTypeOperatingSoftware.set_waarde(value, owner=self)

    @property
    def centraleServerTypeToepassingssoftware(self):
        """Definitie nog toe te voegen voor eigenschap centrale server type>toepassingssoftware"""
        return self._centraleServerTypeToepassingssoftware.waarde

    @centraleServerTypeToepassingssoftware.setter
    def centraleServerTypeToepassingssoftware(self, value):
        self._centraleServerTypeToepassingssoftware.set_waarde(value, owner=self)

    @property
    def codeklavierAantal(self):
        """Definitie nog toe te voegen voor eigenschap codeklavier aantal"""
        return self._codeklavierAantal.waarde

    @codeklavierAantal.setter
    def codeklavierAantal(self, value):
        self._codeklavierAantal.set_waarde(value, owner=self)

    @property
    def deurslotMeerpuntsIseoCilinderAantal(self):
        """Definitie nog toe te voegen voor eigenschap deurslot meerpunts+ISEO cilinder aantal"""
        return self._deurslotMeerpuntsIseoCilinderAantal.waarde

    @deurslotMeerpuntsIseoCilinderAantal.setter
    def deurslotMeerpuntsIseoCilinderAantal(self, value):
        self._deurslotMeerpuntsIseoCilinderAantal.set_waarde(value, owner=self)

    @property
    def deurslotMotorischeCilEmvy3ksAantal(self):
        """Definitie nog toe te voegen voor eigenschap deurslot motorische cil(EMVY 3KS) aantal"""
        return self._deurslotMotorischeCilEmvy3ksAantal.waarde

    @deurslotMotorischeCilEmvy3ksAantal.setter
    def deurslotMotorischeCilEmvy3ksAantal(self, value):
        self._deurslotMotorischeCilEmvy3ksAantal.set_waarde(value, owner=self)

    @property
    def inbraakcentraleAantal(self):
        """Definitie nog toe te voegen voor eigenschap inbraakcentrale aantal"""
        return self._inbraakcentraleAantal.waarde

    @inbraakcentraleAantal.setter
    def inbraakcentraleAantal(self, value):
        self._inbraakcentraleAantal.set_waarde(value, owner=self)

    @property
    def inbraakcentraleType(self):
        """Definitie nog toe te voegen voor eigenschap inbraakcentrale type"""
        return self._inbraakcentraleType.waarde

    @inbraakcentraleType.setter
    def inbraakcentraleType(self, value):
        self._inbraakcentraleType.set_waarde(value, owner=self)

    @property
    def kaartlezerAantal(self):
        """Definitie nog toe te voegen voor eigenschap kaartlezer aantal"""
        return self._kaartlezerAantal.waarde

    @kaartlezerAantal.setter
    def kaartlezerAantal(self, value):
        self._kaartlezerAantal.set_waarde(value, owner=self)

    @property
    def magneetcontactenAantal(self):
        """Definitie nog toe te voegen voor eigenschap magneetcontacten aantal"""
        return self._magneetcontactenAantal.waarde

    @magneetcontactenAantal.setter
    def magneetcontactenAantal(self, value):
        self._magneetcontactenAantal.set_waarde(value, owner=self)

    @property
    def noodverlichtingAantal(self):
        """Definitie nog toe te voegen voor eigenschap noodverlichting aantal"""
        return self._noodverlichtingAantal.waarde

    @noodverlichtingAantal.setter
    def noodverlichtingAantal(self, value):
        self._noodverlichtingAantal.set_waarde(value, owner=self)

    @property
    def notitieinspectie(self):
        """Definitie nog toe te voegen voor eigenschap notitie"""
        return self._notitieinspectie.waarde

    @notitieinspectie.setter
    def notitieinspectie(self, value):
        self._notitieinspectie.set_waarde(value, owner=self)

    @property
    def opmerkingenBijOnderhoud(self):
        """Definitie nog toe te voegen voor eigenschap opmerkingen bij onderhoud"""
        return self._opmerkingenBijOnderhoud.waarde

    @opmerkingenBijOnderhoud.setter
    def opmerkingenBijOnderhoud(self, value):
        self._opmerkingenBijOnderhoud.set_waarde(value, owner=self)

    @property
    def resultaatOnderhoud(self):
        """Definitie nog toe te voegen voor eigenschap resultaat onderhoud"""
        return self._resultaatOnderhoud.waarde

    @resultaatOnderhoud.setter
    def resultaatOnderhoud(self, value):
        self._resultaatOnderhoud.set_waarde(value, owner=self)

    @property
    def rookmeldersAantal(self):
        """Definitie nog toe te voegen voor eigenschap rookmelders aantal"""
        return self._rookmeldersAantal.waarde

    @rookmeldersAantal.setter
    def rookmeldersAantal(self, value):
        self._rookmeldersAantal.set_waarde(value, owner=self)

