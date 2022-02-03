# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class SeinbrugDVM(EMObject):
    """Mechanische contructie DVM installatie"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#SeinbrugDVM'
    label = 'Seinbrug DVM'

    def __init__(self):
        super().__init__()

        self._ralKleur = EMAttribuut(field=StringField,
                                     naam='RAL kleur',
                                     label='RAL kleur',
                                     objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.ralKleur',
                                     definitie='Definitie nog toe te voegen voor eigenschap RAL kleur',
                                     owner=self)

        self._beschadigingAanwezig = EMAttribuut(field=BooleanField,
                                                 naam='beschadiging aanwezig',
                                                 label='beschadiging aanwezig',
                                                 objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.beschadigingAanwezig',
                                                 definitie='Definitie nog toe te voegen voor eigenschap beschadiging aanwezig',
                                                 owner=self)

        self._beschadigingAnderePlaats = EMAttribuut(field=StringField,
                                                     naam='beschadiging andere plaats',
                                                     label='beschadiging andere plaats',
                                                     objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.beschadigingAnderePlaats',
                                                     definitie='Definitie nog toe te voegen voor eigenschap beschadiging andere plaats',
                                                     owner=self)

        self._beschadigingBeugelsBord = EMAttribuut(field=StringField,
                                                    naam='beschadiging beugels bord',
                                                    label='beschadiging beugels bord',
                                                    objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.beschadigingBeugelsBord',
                                                    definitie='Definitie nog toe te voegen voor eigenschap beschadiging beugels bord',
                                                    owner=self)

        self._beschadigingKolomLinks = EMAttribuut(field=StringField,
                                                   naam='beschadiging kolom links',
                                                   label='beschadiging kolom links',
                                                   objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.beschadigingKolomLinks',
                                                   definitie='Definitie nog toe te voegen voor eigenschap beschadiging kolom links',
                                                   owner=self)

        self._beschadigingKolomRechts = EMAttribuut(field=StringField,
                                                    naam='beschadiging kolom rechts',
                                                    label='beschadiging kolom rechts',
                                                    objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.beschadigingKolomRechts',
                                                    definitie='Definitie nog toe te voegen voor eigenschap beschadiging kolom rechts',
                                                    owner=self)

        self._beschadigingLadderLinks = EMAttribuut(field=StringField,
                                                    naam='beschadiging ladder links',
                                                    label='beschadiging ladder links',
                                                    objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.beschadigingLadderLinks',
                                                    definitie='Definitie nog toe te voegen voor eigenschap beschadiging ladder links',
                                                    owner=self)

        self._beschadigingLadderRechts = EMAttribuut(field=StringField,
                                                     naam='beschadiging ladder rechts',
                                                     label='beschadiging ladder rechts',
                                                     objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.beschadigingLadderRechts',
                                                     definitie='Definitie nog toe te voegen voor eigenschap beschadiging ladder rechts',
                                                     owner=self)

        self._beschadigingLiggerBoven = EMAttribuut(field=StringField,
                                                    naam='beschadiging ligger boven',
                                                    label='beschadiging ligger boven',
                                                    objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.beschadigingLiggerBoven',
                                                    definitie='Definitie nog toe te voegen voor eigenschap beschadiging ligger boven',
                                                    owner=self)

        self._beschadigingLiggerOnder = EMAttribuut(field=StringField,
                                                    naam='beschadiging ligger onder',
                                                    label='beschadiging ligger onder',
                                                    objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.beschadigingLiggerOnder',
                                                    definitie='Definitie nog toe te voegen voor eigenschap beschadiging ligger onder',
                                                    owner=self)

        self._borgingLeuningenAangebracht = EMAttribuut(field=StringField,
                                                        naam='borging leuningen aangebracht',
                                                        label='borging leuningen aangebracht',
                                                        objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.borgingLeuningenAangebracht',
                                                        definitie='Definitie nog toe te voegen voor eigenschap toestand boutverbinding',
                                                        owner=self)

        self._datumNieuweBescherming = EMAttribuut(field=DateField,
                                                   naam='datum nieuwe bescherming',
                                                   label='datum nieuwe bescherming',
                                                   objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.datumNieuweBescherming',
                                                   definitie='Definitie nog toe te voegen voor eigenschap datum nieuwe bescherming',
                                                   owner=self)

        self._datumNieuweSeinbrugDvm = EMAttribuut(field=DateField,
                                                   naam='datum nieuwe seinbrug DVM',
                                                   label='datum nieuwe seinbrug DVM',
                                                   objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.datumNieuweSeinbrugDvm',
                                                   definitie='Definitie nog toe te voegen voor eigenschap datum nieuwe seinbrug DVM',
                                                   owner=self)

        self._externeRoestAanwezig = EMAttribuut(field=BooleanField,
                                                 naam='externe roest aanwezig',
                                                 label='externe roest aanwezig',
                                                 objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.externeRoestAanwezig',
                                                 definitie='Definitie nog toe te voegen voor eigenschap externe roest aanwezig',
                                                 owner=self)

        self._externeRoestAnderePlaats = EMAttribuut(field=StringField,
                                                     naam='externe roest andere plaats',
                                                     label='externe roest andere plaats',
                                                     objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.externeRoestAnderePlaats',
                                                     definitie='Definitie nog toe te voegen voor eigenschap externe roest andere plaats',
                                                     owner=self)

        self._externeRoestBeugelsBord = EMAttribuut(field=StringField,
                                                    naam='externe roest beugels bord',
                                                    label='externe roest beugels bord',
                                                    objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.externeRoestBeugelsBord',
                                                    definitie='Definitie nog toe te voegen voor eigenschap externe roest beugels bord',
                                                    owner=self)

        self._externeRoestKolomLinks = EMAttribuut(field=StringField,
                                                   naam='externe roest kolom links',
                                                   label='externe roest kolom links',
                                                   objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.externeRoestKolomLinks',
                                                   definitie='Definitie nog toe te voegen voor eigenschap externe roest kolom links',
                                                   owner=self)

        self._externeRoestKolomRechts = EMAttribuut(field=StringField,
                                                    naam='externe roest kolom rechts',
                                                    label='externe roest kolom rechts',
                                                    objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.externeRoestKolomRechts',
                                                    definitie='Definitie nog toe te voegen voor eigenschap externe roest kolom rechts',
                                                    owner=self)

        self._externeRoestLadderLinks = EMAttribuut(field=StringField,
                                                    naam='externe roest ladder links',
                                                    label='externe roest ladder links',
                                                    objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.externeRoestLadderLinks',
                                                    definitie='Definitie nog toe te voegen voor eigenschap externe roest ladder links',
                                                    owner=self)

        self._externeRoestLadderRechts = EMAttribuut(field=StringField,
                                                     naam='externe roest ladder rechts',
                                                     label='externe roest ladder rechts',
                                                     objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.externeRoestLadderRechts',
                                                     definitie='Definitie nog toe te voegen voor eigenschap externe roest ladder rechts',
                                                     owner=self)

        self._externeRoestLiggerBoven = EMAttribuut(field=StringField,
                                                    naam='externe roest ligger boven',
                                                    label='externe roest ligger boven',
                                                    objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.externeRoestLiggerBoven',
                                                    definitie='Definitie nog toe te voegen voor eigenschap externe roest ligger boven',
                                                    owner=self)

        self._externeRoestLiggerOnder = EMAttribuut(field=StringField,
                                                    naam='externe roest ligger onder',
                                                    label='externe roest ligger onder',
                                                    objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.externeRoestLiggerOnder',
                                                    definitie='Definitie nog toe te voegen voor eigenschap externe roest ligger onder',
                                                    owner=self)

        self._interneRoest = EMAttribuut(field=StringField,
                                         naam='interne roest',
                                         label='interne roest',
                                         objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.interneRoest',
                                         definitie='Definitie nog toe te voegen voor eigenschap interne roest',
                                         owner=self)

        self._lengteOverspanning = EMAttribuut(field=FloatOrDecimalField,
                                               naam='lengte overspanning',
                                               label='lengte overspanning',
                                               objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.lengteOverspanning',
                                               definitie='Definitie nog toe te voegen voor eigenschap lengte overspanning',
                                               owner=self)

        self._minimumVrijeHoogte = EMAttribuut(field=FloatOrDecimalField,
                                               naam='minimum vrije hoogte',
                                               label='minimum vrije hoogte',
                                               objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.minimumVrijeHoogte',
                                               definitie='Definitie nog toe te voegen voor eigenschap minimum vrije hoogte',
                                               owner=self)

        self._ontbrekendeDelen = EMAttribuut(field=StringField,
                                             naam='ontbrekende delen',
                                             label='ontbrekende delen',
                                             objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.ontbrekendeDelen',
                                             definitie='Definitie nog toe te voegen voor eigenschap ontbrekende delen',
                                             owner=self)

        self._redenSeinbrugDvmVerwijderd = EMAttribuut(field=StringField,
                                                       naam='reden seinbrug DVM verwijderd',
                                                       label='reden seinbrug DVM verwijderd',
                                                       objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.redenSeinbrugDvmVerwijderd',
                                                       definitie='Definitie nog toe te voegen voor eigenschap reden seinbrug DVM verwijderd',
                                                       owner=self)

        self._seinbrugDvmVerwijderd = EMAttribuut(field=BooleanField,
                                                  naam='seinbrug DVM verwijderd',
                                                  label='seinbrug DVM verwijderd',
                                                  objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.seinbrugDvmVerwijderd',
                                                  definitie='Definitie nog toe te voegen voor eigenschap seinbrug DVM verwijderd',
                                                  owner=self)

        self._toestandFundering = EMAttribuut(field=StringField,
                                              naam='toestand fundering',
                                              label='toestand fundering',
                                              objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.toestandFundering',
                                              definitie='Definitie nog toe te voegen voor eigenschap toestand fundering',
                                              owner=self)

        self._toestandKabels = EMAttribuut(field=StringField,
                                           naam='toestand kabels',
                                           label='toestand kabels',
                                           objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.toestandKabels',
                                           definitie='Definitie nog toe te voegen voor eigenschap toestand kabels',
                                           owner=self)

        self._typeESeinbrug = EMAttribuut(field=StringField,
                                          naam='type E-seinbrug',
                                          label='type E-seinbrug',
                                          objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.typeESeinbrug',
                                          definitie='Definitie nog toe te voegen voor eigenschap type E-seinbrug',
                                          owner=self)

        self._typeBescherming = EMAttribuut(field=StringField,
                                            naam='type bescherming',
                                            label='type bescherming',
                                            objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SeinbrugDVM.typeBescherming',
                                            definitie='Definitie nog toe te voegen voor eigenschap type bescherming',
                                            owner=self)

        self._typeSeinbrug = EMAttribuut(field=StringField,
                                         naam='type seinbrug',
                                         label='type seinbrug',
                                         objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.typeSeinbrug',
                                         definitie='Definitie nog toe te voegen voor eigenschap type seinbrug',
                                         owner=self)

    @property
    def ralKleur(self):
        """Definitie nog toe te voegen voor eigenschap RAL kleur"""
        return self._ralKleur.waarde

    @ralKleur.setter
    def ralKleur(self, value):
        self._ralKleur.set_waarde(value, owner=self)

    @property
    def beschadigingAanwezig(self):
        """Definitie nog toe te voegen voor eigenschap beschadiging aanwezig"""
        return self._beschadigingAanwezig.waarde

    @beschadigingAanwezig.setter
    def beschadigingAanwezig(self, value):
        self._beschadigingAanwezig.set_waarde(value, owner=self)

    @property
    def beschadigingAnderePlaats(self):
        """Definitie nog toe te voegen voor eigenschap beschadiging andere plaats"""
        return self._beschadigingAnderePlaats.waarde

    @beschadigingAnderePlaats.setter
    def beschadigingAnderePlaats(self, value):
        self._beschadigingAnderePlaats.set_waarde(value, owner=self)

    @property
    def beschadigingBeugelsBord(self):
        """Definitie nog toe te voegen voor eigenschap beschadiging beugels bord"""
        return self._beschadigingBeugelsBord.waarde

    @beschadigingBeugelsBord.setter
    def beschadigingBeugelsBord(self, value):
        self._beschadigingBeugelsBord.set_waarde(value, owner=self)

    @property
    def beschadigingKolomLinks(self):
        """Definitie nog toe te voegen voor eigenschap beschadiging kolom links"""
        return self._beschadigingKolomLinks.waarde

    @beschadigingKolomLinks.setter
    def beschadigingKolomLinks(self, value):
        self._beschadigingKolomLinks.set_waarde(value, owner=self)

    @property
    def beschadigingKolomRechts(self):
        """Definitie nog toe te voegen voor eigenschap beschadiging kolom rechts"""
        return self._beschadigingKolomRechts.waarde

    @beschadigingKolomRechts.setter
    def beschadigingKolomRechts(self, value):
        self._beschadigingKolomRechts.set_waarde(value, owner=self)

    @property
    def beschadigingLadderLinks(self):
        """Definitie nog toe te voegen voor eigenschap beschadiging ladder links"""
        return self._beschadigingLadderLinks.waarde

    @beschadigingLadderLinks.setter
    def beschadigingLadderLinks(self, value):
        self._beschadigingLadderLinks.set_waarde(value, owner=self)

    @property
    def beschadigingLadderRechts(self):
        """Definitie nog toe te voegen voor eigenschap beschadiging ladder rechts"""
        return self._beschadigingLadderRechts.waarde

    @beschadigingLadderRechts.setter
    def beschadigingLadderRechts(self, value):
        self._beschadigingLadderRechts.set_waarde(value, owner=self)

    @property
    def beschadigingLiggerBoven(self):
        """Definitie nog toe te voegen voor eigenschap beschadiging ligger boven"""
        return self._beschadigingLiggerBoven.waarde

    @beschadigingLiggerBoven.setter
    def beschadigingLiggerBoven(self, value):
        self._beschadigingLiggerBoven.set_waarde(value, owner=self)

    @property
    def beschadigingLiggerOnder(self):
        """Definitie nog toe te voegen voor eigenschap beschadiging ligger onder"""
        return self._beschadigingLiggerOnder.waarde

    @beschadigingLiggerOnder.setter
    def beschadigingLiggerOnder(self, value):
        self._beschadigingLiggerOnder.set_waarde(value, owner=self)

    @property
    def borgingLeuningenAangebracht(self):
        """Definitie nog toe te voegen voor eigenschap toestand boutverbinding"""
        return self._borgingLeuningenAangebracht.waarde

    @borgingLeuningenAangebracht.setter
    def borgingLeuningenAangebracht(self, value):
        self._borgingLeuningenAangebracht.set_waarde(value, owner=self)

    @property
    def datumNieuweBescherming(self):
        """Definitie nog toe te voegen voor eigenschap datum nieuwe bescherming"""
        return self._datumNieuweBescherming.waarde

    @datumNieuweBescherming.setter
    def datumNieuweBescherming(self, value):
        self._datumNieuweBescherming.set_waarde(value, owner=self)

    @property
    def datumNieuweSeinbrugDvm(self):
        """Definitie nog toe te voegen voor eigenschap datum nieuwe seinbrug DVM"""
        return self._datumNieuweSeinbrugDvm.waarde

    @datumNieuweSeinbrugDvm.setter
    def datumNieuweSeinbrugDvm(self, value):
        self._datumNieuweSeinbrugDvm.set_waarde(value, owner=self)

    @property
    def externeRoestAanwezig(self):
        """Definitie nog toe te voegen voor eigenschap externe roest aanwezig"""
        return self._externeRoestAanwezig.waarde

    @externeRoestAanwezig.setter
    def externeRoestAanwezig(self, value):
        self._externeRoestAanwezig.set_waarde(value, owner=self)

    @property
    def externeRoestAnderePlaats(self):
        """Definitie nog toe te voegen voor eigenschap externe roest andere plaats"""
        return self._externeRoestAnderePlaats.waarde

    @externeRoestAnderePlaats.setter
    def externeRoestAnderePlaats(self, value):
        self._externeRoestAnderePlaats.set_waarde(value, owner=self)

    @property
    def externeRoestBeugelsBord(self):
        """Definitie nog toe te voegen voor eigenschap externe roest beugels bord"""
        return self._externeRoestBeugelsBord.waarde

    @externeRoestBeugelsBord.setter
    def externeRoestBeugelsBord(self, value):
        self._externeRoestBeugelsBord.set_waarde(value, owner=self)

    @property
    def externeRoestKolomLinks(self):
        """Definitie nog toe te voegen voor eigenschap externe roest kolom links"""
        return self._externeRoestKolomLinks.waarde

    @externeRoestKolomLinks.setter
    def externeRoestKolomLinks(self, value):
        self._externeRoestKolomLinks.set_waarde(value, owner=self)

    @property
    def externeRoestKolomRechts(self):
        """Definitie nog toe te voegen voor eigenschap externe roest kolom rechts"""
        return self._externeRoestKolomRechts.waarde

    @externeRoestKolomRechts.setter
    def externeRoestKolomRechts(self, value):
        self._externeRoestKolomRechts.set_waarde(value, owner=self)

    @property
    def externeRoestLadderLinks(self):
        """Definitie nog toe te voegen voor eigenschap externe roest ladder links"""
        return self._externeRoestLadderLinks.waarde

    @externeRoestLadderLinks.setter
    def externeRoestLadderLinks(self, value):
        self._externeRoestLadderLinks.set_waarde(value, owner=self)

    @property
    def externeRoestLadderRechts(self):
        """Definitie nog toe te voegen voor eigenschap externe roest ladder rechts"""
        return self._externeRoestLadderRechts.waarde

    @externeRoestLadderRechts.setter
    def externeRoestLadderRechts(self, value):
        self._externeRoestLadderRechts.set_waarde(value, owner=self)

    @property
    def externeRoestLiggerBoven(self):
        """Definitie nog toe te voegen voor eigenschap externe roest ligger boven"""
        return self._externeRoestLiggerBoven.waarde

    @externeRoestLiggerBoven.setter
    def externeRoestLiggerBoven(self, value):
        self._externeRoestLiggerBoven.set_waarde(value, owner=self)

    @property
    def externeRoestLiggerOnder(self):
        """Definitie nog toe te voegen voor eigenschap externe roest ligger onder"""
        return self._externeRoestLiggerOnder.waarde

    @externeRoestLiggerOnder.setter
    def externeRoestLiggerOnder(self, value):
        self._externeRoestLiggerOnder.set_waarde(value, owner=self)

    @property
    def interneRoest(self):
        """Definitie nog toe te voegen voor eigenschap interne roest"""
        return self._interneRoest.waarde

    @interneRoest.setter
    def interneRoest(self, value):
        self._interneRoest.set_waarde(value, owner=self)

    @property
    def lengteOverspanning(self):
        """Definitie nog toe te voegen voor eigenschap lengte overspanning"""
        return self._lengteOverspanning.waarde

    @lengteOverspanning.setter
    def lengteOverspanning(self, value):
        self._lengteOverspanning.set_waarde(value, owner=self)

    @property
    def minimumVrijeHoogte(self):
        """Definitie nog toe te voegen voor eigenschap minimum vrije hoogte"""
        return self._minimumVrijeHoogte.waarde

    @minimumVrijeHoogte.setter
    def minimumVrijeHoogte(self, value):
        self._minimumVrijeHoogte.set_waarde(value, owner=self)

    @property
    def ontbrekendeDelen(self):
        """Definitie nog toe te voegen voor eigenschap ontbrekende delen"""
        return self._ontbrekendeDelen.waarde

    @ontbrekendeDelen.setter
    def ontbrekendeDelen(self, value):
        self._ontbrekendeDelen.set_waarde(value, owner=self)

    @property
    def redenSeinbrugDvmVerwijderd(self):
        """Definitie nog toe te voegen voor eigenschap reden seinbrug DVM verwijderd"""
        return self._redenSeinbrugDvmVerwijderd.waarde

    @redenSeinbrugDvmVerwijderd.setter
    def redenSeinbrugDvmVerwijderd(self, value):
        self._redenSeinbrugDvmVerwijderd.set_waarde(value, owner=self)

    @property
    def seinbrugDvmVerwijderd(self):
        """Definitie nog toe te voegen voor eigenschap seinbrug DVM verwijderd"""
        return self._seinbrugDvmVerwijderd.waarde

    @seinbrugDvmVerwijderd.setter
    def seinbrugDvmVerwijderd(self, value):
        self._seinbrugDvmVerwijderd.set_waarde(value, owner=self)

    @property
    def toestandFundering(self):
        """Definitie nog toe te voegen voor eigenschap toestand fundering"""
        return self._toestandFundering.waarde

    @toestandFundering.setter
    def toestandFundering(self, value):
        self._toestandFundering.set_waarde(value, owner=self)

    @property
    def toestandKabels(self):
        """Definitie nog toe te voegen voor eigenschap toestand kabels"""
        return self._toestandKabels.waarde

    @toestandKabels.setter
    def toestandKabels(self, value):
        self._toestandKabels.set_waarde(value, owner=self)

    @property
    def typeESeinbrug(self):
        """Definitie nog toe te voegen voor eigenschap type E-seinbrug"""
        return self._typeESeinbrug.waarde

    @typeESeinbrug.setter
    def typeESeinbrug(self, value):
        self._typeESeinbrug.set_waarde(value, owner=self)

    @property
    def typeBescherming(self):
        """Definitie nog toe te voegen voor eigenschap type bescherming"""
        return self._typeBescherming.waarde

    @typeBescherming.setter
    def typeBescherming(self, value):
        self._typeBescherming.set_waarde(value, owner=self)

    @property
    def typeSeinbrug(self):
        """Definitie nog toe te voegen voor eigenschap type seinbrug"""
        return self._typeSeinbrug.waarde

    @typeSeinbrug.setter
    def typeSeinbrug(self, value):
        self._typeSeinbrug.set_waarde(value, owner=self)

