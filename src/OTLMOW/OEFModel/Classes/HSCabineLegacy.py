# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class HSCabineLegacy(EMObject):
    """subonderdeel van HS-installatie"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#HSCabineLegacy'
    label = 'Hoogspanningscabine (Legacy)'

    def __init__(self):
        super().__init__()

        self._alleMetalenOnderdelenGeaardVerbonden = EMAttribuut(field=StringField,
                                                                 naam='alle metalen onderdelen geaard&verbonden',
                                                                 label='alle metalen onderdelen geaard&verbonden',
                                                                 objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSCabineLegacy.alleMetalenOnderdelenGeaardVerbonden',
                                                                 definitie='Definitie nog toe te voegen voor eigenschap alle metalen onderdelen geaard&verbonden')

        self._alleToegangsdeurenSluitenPerfect = EMAttribuut(field=StringField,
                                                             naam='alle toegangsdeuren sluiten perfect',
                                                             label='alle toegangsdeuren sluiten perfect',
                                                             objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSCabineLegacy.alleToegangsdeurenSluitenPerfect',
                                                             definitie='Definitie nog toe te voegen voor eigenschap alle toegangsdeuren sluiten perfect')

        self._alleVerlichtingsarmaturenFunctioneren = EMAttribuut(field=StringField,
                                                                  naam='alle verlichtingsarmaturen functioneren',
                                                                  label='alle verlichtingsarmaturen functioneren',
                                                                  objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSCabineLegacy.alleVerlichtingsarmaturenFunctioneren',
                                                                  definitie='Definitie nog toe te voegen voor eigenschap alle verlichtingsarmaturen functioneren')

        self._bezoekkaartAanwezigEnIngevuld = EMAttribuut(field=StringField,
                                                          naam='bezoekkaart aanwezig en ingevuld',
                                                          label='bezoekkaart aanwezig en ingevuld',
                                                          objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSCabineLegacy.bezoekkaartAanwezigEnIngevuld',
                                                          definitie='Definitie nog toe te voegen voor eigenschap bezoekkaart aanwezig en ingevuld')

        self._binnenGeenSpinnenwebOngedierteZand = EMAttribuut(field=StringField,
                                                               naam='binnen geen spinnenweb/ongedierte/zand',
                                                               label='binnen geen spinnenweb/ongedierte/zand',
                                                               objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSCabineLegacy.binnenGeenSpinnenwebOngedierteZand',
                                                               definitie='Definitie nog toe te voegen voor eigenschap binnen geen spinnenweb/ongedierte/zand')

        self._geenScheurenOpeningenInBehuizing = EMAttribuut(field=StringField,
                                                             naam='geen scheuren/openingen in behuizing',
                                                             label='geen scheuren/openingen in behuizing',
                                                             objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSCabineLegacy.geenScheurenOpeningenInBehuizing',
                                                             definitie='Definitie nog toe te voegen voor eigenschap geen scheuren/openingen in behuizing')

        self._geenStootStruikelgevaar = EMAttribuut(field=StringField,
                                                    naam='geen stoot / struikelgevaar',
                                                    label='geen stoot / struikelgevaar',
                                                    objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSCabineLegacy.geenStootStruikelgevaar',
                                                    definitie='Definitie nog toe te voegen voor eigenschap geen stoot / struikelgevaar')

        self._geenVreemdeMaterialenAanwezig = EMAttribuut(field=StringField,
                                                          naam='geen vreemde materialen aanwezig',
                                                          label='geen vreemde materialen aanwezig',
                                                          objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSCabineLegacy.geenVreemdeMaterialenAanwezig',
                                                          definitie='Definitie nog toe te voegen voor eigenschap geen vreemde materialen aanwezig')

        self._geisoleerdeHandschInPerfecteStaat = EMAttribuut(field=StringField,
                                                              naam='geisoleerde handsch in perfecte staat',
                                                              label='geisoleerde handsch in perfecte staat',
                                                              objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.geisoleerdeHandschInPerfecteStaat',
                                                              definitie='Definitie nog toe te voegen voor eigenschap geisoleerde handsch in perfecte staat')

        self._indicatieplatenAanwezigOpToegangsdeur = EMAttribuut(field=StringField,
                                                                  naam='indicatieplaten aanwezig op toegangsdeur',
                                                                  label='indicatieplaten aanwezig op toegangsdeur',
                                                                  objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSCabineLegacy.indicatieplatenAanwezigOpToegangsdeur',
                                                                  definitie='Definitie nog toe te voegen voor eigenschap indicatieplaten aanwezig op toegangsdeur')

        self._isolerendSasInGoedeStaat = EMAttribuut(field=StringField,
                                                     naam='isolerend sas in goede staat',
                                                     label='isolerend sas in goede staat',
                                                     objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSCabineLegacy.isolerendSasInGoedeStaat',
                                                     definitie='Definitie nog toe te voegen voor eigenschap isolerend sas in goede staat')

        self._kabelkelderVrijVanWater = EMAttribuut(field=StringField,
                                                    naam='kabelkelder vrij van water',
                                                    label='kabelkelder vrij van water',
                                                    objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.kabelkelderVrijVanWater',
                                                    definitie='Definitie nog toe te voegen voor eigenschap kabelkelder vrij van water')

        self._noodverlichtingsarmaturenFunctioneren = EMAttribuut(field=StringField,
                                                                  naam='noodverlichtingsarmaturen functioneren',
                                                                  label='noodverlichtingsarmaturen functioneren',
                                                                  objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSCabineLegacy.noodverlichtingsarmaturenFunctioneren',
                                                                  definitie='Definitie nog toe te voegen voor eigenschap noodverlichtingsarmaturen functioneren')

        self._opmerkingenOverHsCabine = EMAttribuut(field=StringField,
                                                    naam='opmerkingen over HS cabine',
                                                    label='opmerkingen over HS cabine',
                                                    objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSCabineLegacy.opmerkingenOverHsCabine',
                                                    definitie='Definitie nog toe te voegen voor eigenschap opmerkingen over HS cabine')

        self._slotenEnScharnierenInGoedeStaat = EMAttribuut(field=StringField,
                                                            naam='sloten en scharnieren in goede staat',
                                                            label='sloten en scharnieren in goede staat',
                                                            objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSCabineLegacy.slotenEnScharnierenInGoedeStaat',
                                                            definitie='Definitie nog toe te voegen voor eigenschap sloten en scharnieren in goede staat')

        self._thermostaatHygrostaatFunctioneert = EMAttribuut(field=StringField,
                                                              naam='thermostaat / hygrostaat functioneert',
                                                              label='thermostaat / hygrostaat functioneert',
                                                              objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSCabineLegacy.thermostaatHygrostaatFunctioneert',
                                                              definitie='Definitie nog toe te voegen voor eigenschap thermostaat / hygrostaat functioneert')

        self._toegangVrijVanOnkruidStruikenTakken = EMAttribuut(field=StringField,
                                                                naam='toegang vrij van onkruid/struiken/takken',
                                                                label='toegang vrij van onkruid/struiken/takken',
                                                                objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSCabineLegacy.toegangVrijVanOnkruidStruikenTakken',
                                                                definitie='Definitie nog toe te voegen voor eigenschap toegang vrij van onkruid/struiken/takken')

        self._toegangspadInGoedeStaat = EMAttribuut(field=StringField,
                                                    naam='toegangspad in goede staat',
                                                    label='toegangspad in goede staat',
                                                    objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSCabineLegacy.toegangspadInGoedeStaat',
                                                    definitie='Definitie nog toe te voegen voor eigenschap toegangspad in goede staat')

        self._verluchtingsroostersInGoedeStaat = EMAttribuut(field=StringField,
                                                             naam='verluchtingsroosters in goede staat',
                                                             label='verluchtingsroosters in goede staat',
                                                             objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSCabineLegacy.verluchtingsroostersInGoedeStaat',
                                                             definitie='Definitie nog toe te voegen voor eigenschap verluchtingsroosters in goede staat')

        self._verwarmingstoestelNietAfgedekt = EMAttribuut(field=StringField,
                                                           naam='verwarmingstoestel niet afgedekt',
                                                           label='verwarmingstoestel niet afgedekt',
                                                           objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSCabineLegacy.verwarmingstoestelNietAfgedekt',
                                                           definitie='Definitie nog toe te voegen voor eigenschap verwarmingstoestel niet afgedekt')

    @property
    def alleMetalenOnderdelenGeaardVerbonden(self):
        """Definitie nog toe te voegen voor eigenschap alle metalen onderdelen geaard&verbonden"""
        return self._alleMetalenOnderdelenGeaardVerbonden.waarde

    @alleMetalenOnderdelenGeaardVerbonden.setter
    def alleMetalenOnderdelenGeaardVerbonden(self, value):
        self._alleMetalenOnderdelenGeaardVerbonden.set_waarde(value, owner=self)

    @property
    def alleToegangsdeurenSluitenPerfect(self):
        """Definitie nog toe te voegen voor eigenschap alle toegangsdeuren sluiten perfect"""
        return self._alleToegangsdeurenSluitenPerfect.waarde

    @alleToegangsdeurenSluitenPerfect.setter
    def alleToegangsdeurenSluitenPerfect(self, value):
        self._alleToegangsdeurenSluitenPerfect.set_waarde(value, owner=self)

    @property
    def alleVerlichtingsarmaturenFunctioneren(self):
        """Definitie nog toe te voegen voor eigenschap alle verlichtingsarmaturen functioneren"""
        return self._alleVerlichtingsarmaturenFunctioneren.waarde

    @alleVerlichtingsarmaturenFunctioneren.setter
    def alleVerlichtingsarmaturenFunctioneren(self, value):
        self._alleVerlichtingsarmaturenFunctioneren.set_waarde(value, owner=self)

    @property
    def bezoekkaartAanwezigEnIngevuld(self):
        """Definitie nog toe te voegen voor eigenschap bezoekkaart aanwezig en ingevuld"""
        return self._bezoekkaartAanwezigEnIngevuld.waarde

    @bezoekkaartAanwezigEnIngevuld.setter
    def bezoekkaartAanwezigEnIngevuld(self, value):
        self._bezoekkaartAanwezigEnIngevuld.set_waarde(value, owner=self)

    @property
    def binnenGeenSpinnenwebOngedierteZand(self):
        """Definitie nog toe te voegen voor eigenschap binnen geen spinnenweb/ongedierte/zand"""
        return self._binnenGeenSpinnenwebOngedierteZand.waarde

    @binnenGeenSpinnenwebOngedierteZand.setter
    def binnenGeenSpinnenwebOngedierteZand(self, value):
        self._binnenGeenSpinnenwebOngedierteZand.set_waarde(value, owner=self)

    @property
    def geenScheurenOpeningenInBehuizing(self):
        """Definitie nog toe te voegen voor eigenschap geen scheuren/openingen in behuizing"""
        return self._geenScheurenOpeningenInBehuizing.waarde

    @geenScheurenOpeningenInBehuizing.setter
    def geenScheurenOpeningenInBehuizing(self, value):
        self._geenScheurenOpeningenInBehuizing.set_waarde(value, owner=self)

    @property
    def geenStootStruikelgevaar(self):
        """Definitie nog toe te voegen voor eigenschap geen stoot / struikelgevaar"""
        return self._geenStootStruikelgevaar.waarde

    @geenStootStruikelgevaar.setter
    def geenStootStruikelgevaar(self, value):
        self._geenStootStruikelgevaar.set_waarde(value, owner=self)

    @property
    def geenVreemdeMaterialenAanwezig(self):
        """Definitie nog toe te voegen voor eigenschap geen vreemde materialen aanwezig"""
        return self._geenVreemdeMaterialenAanwezig.waarde

    @geenVreemdeMaterialenAanwezig.setter
    def geenVreemdeMaterialenAanwezig(self, value):
        self._geenVreemdeMaterialenAanwezig.set_waarde(value, owner=self)

    @property
    def geisoleerdeHandschInPerfecteStaat(self):
        """Definitie nog toe te voegen voor eigenschap geisoleerde handsch in perfecte staat"""
        return self._geisoleerdeHandschInPerfecteStaat.waarde

    @geisoleerdeHandschInPerfecteStaat.setter
    def geisoleerdeHandschInPerfecteStaat(self, value):
        self._geisoleerdeHandschInPerfecteStaat.set_waarde(value, owner=self)

    @property
    def indicatieplatenAanwezigOpToegangsdeur(self):
        """Definitie nog toe te voegen voor eigenschap indicatieplaten aanwezig op toegangsdeur"""
        return self._indicatieplatenAanwezigOpToegangsdeur.waarde

    @indicatieplatenAanwezigOpToegangsdeur.setter
    def indicatieplatenAanwezigOpToegangsdeur(self, value):
        self._indicatieplatenAanwezigOpToegangsdeur.set_waarde(value, owner=self)

    @property
    def isolerendSasInGoedeStaat(self):
        """Definitie nog toe te voegen voor eigenschap isolerend sas in goede staat"""
        return self._isolerendSasInGoedeStaat.waarde

    @isolerendSasInGoedeStaat.setter
    def isolerendSasInGoedeStaat(self, value):
        self._isolerendSasInGoedeStaat.set_waarde(value, owner=self)

    @property
    def kabelkelderVrijVanWater(self):
        """Definitie nog toe te voegen voor eigenschap kabelkelder vrij van water"""
        return self._kabelkelderVrijVanWater.waarde

    @kabelkelderVrijVanWater.setter
    def kabelkelderVrijVanWater(self, value):
        self._kabelkelderVrijVanWater.set_waarde(value, owner=self)

    @property
    def noodverlichtingsarmaturenFunctioneren(self):
        """Definitie nog toe te voegen voor eigenschap noodverlichtingsarmaturen functioneren"""
        return self._noodverlichtingsarmaturenFunctioneren.waarde

    @noodverlichtingsarmaturenFunctioneren.setter
    def noodverlichtingsarmaturenFunctioneren(self, value):
        self._noodverlichtingsarmaturenFunctioneren.set_waarde(value, owner=self)

    @property
    def opmerkingenOverHsCabine(self):
        """Definitie nog toe te voegen voor eigenschap opmerkingen over HS cabine"""
        return self._opmerkingenOverHsCabine.waarde

    @opmerkingenOverHsCabine.setter
    def opmerkingenOverHsCabine(self, value):
        self._opmerkingenOverHsCabine.set_waarde(value, owner=self)

    @property
    def slotenEnScharnierenInGoedeStaat(self):
        """Definitie nog toe te voegen voor eigenschap sloten en scharnieren in goede staat"""
        return self._slotenEnScharnierenInGoedeStaat.waarde

    @slotenEnScharnierenInGoedeStaat.setter
    def slotenEnScharnierenInGoedeStaat(self, value):
        self._slotenEnScharnierenInGoedeStaat.set_waarde(value, owner=self)

    @property
    def thermostaatHygrostaatFunctioneert(self):
        """Definitie nog toe te voegen voor eigenschap thermostaat / hygrostaat functioneert"""
        return self._thermostaatHygrostaatFunctioneert.waarde

    @thermostaatHygrostaatFunctioneert.setter
    def thermostaatHygrostaatFunctioneert(self, value):
        self._thermostaatHygrostaatFunctioneert.set_waarde(value, owner=self)

    @property
    def toegangVrijVanOnkruidStruikenTakken(self):
        """Definitie nog toe te voegen voor eigenschap toegang vrij van onkruid/struiken/takken"""
        return self._toegangVrijVanOnkruidStruikenTakken.waarde

    @toegangVrijVanOnkruidStruikenTakken.setter
    def toegangVrijVanOnkruidStruikenTakken(self, value):
        self._toegangVrijVanOnkruidStruikenTakken.set_waarde(value, owner=self)

    @property
    def toegangspadInGoedeStaat(self):
        """Definitie nog toe te voegen voor eigenschap toegangspad in goede staat"""
        return self._toegangspadInGoedeStaat.waarde

    @toegangspadInGoedeStaat.setter
    def toegangspadInGoedeStaat(self, value):
        self._toegangspadInGoedeStaat.set_waarde(value, owner=self)

    @property
    def verluchtingsroostersInGoedeStaat(self):
        """Definitie nog toe te voegen voor eigenschap verluchtingsroosters in goede staat"""
        return self._verluchtingsroostersInGoedeStaat.waarde

    @verluchtingsroostersInGoedeStaat.setter
    def verluchtingsroostersInGoedeStaat(self, value):
        self._verluchtingsroostersInGoedeStaat.set_waarde(value, owner=self)

    @property
    def verwarmingstoestelNietAfgedekt(self):
        """Definitie nog toe te voegen voor eigenschap verwarmingstoestel niet afgedekt"""
        return self._verwarmingstoestelNietAfgedekt.waarde

    @verwarmingstoestelNietAfgedekt.setter
    def verwarmingstoestelNietAfgedekt(self, value):
        self._verwarmingstoestelNietAfgedekt.set_waarde(value, owner=self)

