# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class HSDeel(EMObject):
    """subonderdeel van HS-installatie"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#HSDeel'
    label = 'Hoogspanningsgedeelte'

    def __init__(self):
        super().__init__()

        self._ReserveZekeringenHsAanwezig = EMAttribuut(field=StringField,
                                                         naam='3 reserve zekeringen HS aanwezig',
                                                         label='3 reserve zekeringen HS aanwezig',
                                                         objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSDeel.3ReserveZekeringenHsAanwezig',
                                                         definitie='Definitie nog toe te voegen voor eigenschap 3 reserve zekeringen HS aanwezig')

        self._hsSchakelappTrafoStofSpinnenwebVrij = EMAttribuut(field=StringField,
                                                                naam='HS schakelapp/trafo stof&spinnenweb vrij',
                                                                label='HS schakelapp/trafo stof&spinnenweb vrij',
                                                                objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSDeel.hsSchakelappTrafoStofSpinnenwebVrij',
                                                                definitie='Definitie nog toe te voegen voor eigenschap HS schakelapp/trafo stof&spinnenweb vrij')

        self._alleKabelsGelabeldVolgensSchema = EMAttribuut(field=StringField,
                                                            naam='alle kabels gelabeld volgens schema',
                                                            label='alle kabels gelabeld volgens schema',
                                                            objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.alleKabelsGelabeldVolgensSchema',
                                                            definitie='Definitie nog toe te voegen voor eigenschap alle kabels gelabeld volgens schema')

        self._attestGlobaleAardingAanwezig = EMAttribuut(field=StringField,
                                                         naam='attest globale aarding aanwezig',
                                                         label='attest globale aarding aanwezig',
                                                         objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSDeel.attestGlobaleAardingAanwezig',
                                                         definitie='Definitie nog toe te voegen voor eigenschap attest globale aarding aanwezig')

        self._componentenGelabeldVolgensSchema = EMAttribuut(field=StringField,
                                                             naam='componenten gelabeld volgens schema',
                                                             label='componenten gelabeld volgens schema',
                                                             objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.componentenGelabeldVolgensSchema',
                                                             definitie='Definitie nog toe te voegen voor eigenschap componenten gelabeld volgens schema')

        self._eendraadschemaAanwezig = EMAttribuut(field=StringField,
                                                   naam='eendraadschema aanwezig',
                                                   label='eendraadschema aanwezig',
                                                   objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSDeel.eendraadschemaAanwezig',
                                                   definitie='Definitie nog toe te voegen voor eigenschap eendraadschema aanwezig')

        self._geenLekEindsluitingAankomstveldenDnb = EMAttribuut(field=StringField,
                                                                 naam='geen lek eindsluiting aankomstvelden DNB',
                                                                 label='geen lek eindsluiting aankomstvelden DNB',
                                                                 objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSDeel.geenLekEindsluitingAankomstveldenDnb',
                                                                 definitie='Definitie nog toe te voegen voor eigenschap geen lek eindsluiting aankomstvelden DNB')

        self._geenLekEindsluitingTrafobeveilig = EMAttribuut(field=StringField,
                                                             naam='geen lek eindsluiting trafobeveilig',
                                                             label='geen lek eindsluiting trafobeveilig',
                                                             objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSDeel.geenLekEindsluitingTrafobeveilig',
                                                             definitie='Definitie nog toe te voegen voor eigenschap geen lek eindsluiting trafobeveilig')

        self._geenTrafoOlieLekkage = EMAttribuut(field=StringField,
                                                 naam='geen trafo olie lekkage',
                                                 label='geen trafo olie lekkage',
                                                 objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSDeel.geenTrafoOlieLekkage',
                                                 definitie='Definitie nog toe te voegen voor eigenschap geen trafo olie lekkage')

        self._geenZichtbareDefectenOpenSchakelapp = EMAttribuut(field=StringField,
                                                                naam='geen zichtbare defecten open schakelapp',
                                                                label='geen zichtbare defecten open schakelapp',
                                                                objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSDeel.geenZichtbareDefectenOpenSchakelapp',
                                                                definitie='Definitie nog toe te voegen voor eigenschap geen zichtbare defecten open schakelapp')

        self._geisoleerdeHandschInPerfecteStaat = EMAttribuut(field=StringField,
                                                              naam='geisoleerde handsch in perfecte staat',
                                                              label='geisoleerde handsch in perfecte staat',
                                                              objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.geisoleerdeHandschInPerfecteStaat',
                                                              definitie='Definitie nog toe te voegen voor eigenschap geisoleerde handsch in perfecte staat')

        self._geldigKeuringsverslagHsAanwezig = EMAttribuut(field=StringField,
                                                            naam='geldig keuringsverslag HS aanwezig',
                                                            label='geldig keuringsverslag HS aanwezig',
                                                            objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSDeel.geldigKeuringsverslagHsAanwezig',
                                                            definitie='Definitie nog toe te voegen voor eigenschap geldig keuringsverslag HS aanwezig')

        self._isolatiemattenInGoedeStaat = EMAttribuut(field=StringField,
                                                       naam='isolatiematten in goede staat',
                                                       label='isolatiematten in goede staat',
                                                       objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSDeel.isolatiemattenInGoedeStaat',
                                                       definitie='Definitie nog toe te voegen voor eigenschap isolatiematten in goede staat')

        self._liggingsplanAardingenAanwezig = EMAttribuut(field=StringField,
                                                          naam='liggingsplan aardingen aanwezig',
                                                          label='liggingsplan aardingen aanwezig',
                                                          objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSDeel.liggingsplanAardingenAanwezig',
                                                          definitie='Definitie nog toe te voegen voor eigenschap liggingsplan aardingen aanwezig')

        self._neonSpanningsindicatorenFunctioneren = EMAttribuut(field=StringField,
                                                                 naam='neon spanningsindicatoren functioneren',
                                                                 label='neon spanningsindicatoren functioneren',
                                                                 objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSDeel.neonSpanningsindicatorenFunctioneren',
                                                                 definitie='Definitie nog toe te voegen voor eigenschap neon spanningsindicatoren functioneren')

        self._notitieinspectie = EMAttribuut(field=StringField,
                                             naam='notitieInspectie',
                                             label='notitieInspectie',
                                             objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.notitieinspectie',
                                             definitie='Definitie nog toe te voegen voor eigenschap notitie')

        self._oliepeilTrafoNormaalNiveau = EMAttribuut(field=StringField,
                                                       naam='oliepeil trafo normaal niveau',
                                                       label='oliepeil trafo normaal niveau',
                                                       objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSDeel.oliepeilTrafoNormaalNiveau',
                                                       definitie='Definitie nog toe te voegen voor eigenschap oliepeil trafo normaal niveau')

        self._openBarenstelStofSpinnenwebVrij = EMAttribuut(field=StringField,
                                                            naam='open barenstel stof/spinnenweb vrij',
                                                            label='open barenstel stof/spinnenweb vrij',
                                                            objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSDeel.openBarenstelStofSpinnenwebVrij',
                                                            definitie='Definitie nog toe te voegen voor eigenschap open barenstel stof/spinnenweb vrij')

        self._opmerkingenOverHsGedeelte = EMAttribuut(field=StringField,
                                                      naam='opmerkingen over HS gedeelte',
                                                      label='opmerkingen over HS gedeelte',
                                                      objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSDeel.opmerkingenOverHsGedeelte',
                                                      definitie='Definitie nog toe te voegen voor eigenschap opmerkingen over HS gedeelte')

        self._schakelbankInGoedeStaat = EMAttribuut(field=StringField,
                                                    naam='schakelbank in goede staat',
                                                    label='schakelbank in goede staat',
                                                    objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSDeel.schakelbankInGoedeStaat',
                                                    definitie='Definitie nog toe te voegen voor eigenschap schakelbank in goede staat')

        self._schakelhendelStokInGoedeStaat = EMAttribuut(field=StringField,
                                                          naam='schakelhendel / stok in goede staat',
                                                          label='schakelhendel / stok in goede staat',
                                                          objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSDeel.schakelhendelStokInGoedeStaat',
                                                          definitie='Definitie nog toe te voegen voor eigenschap schakelhendel / stok in goede staat')

        self._schakelpompMagnefixFunctioneert = EMAttribuut(field=StringField,
                                                            naam='schakelpomp magnefix functioneert',
                                                            label='schakelpomp magnefix functioneert',
                                                            objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSDeel.schakelpompMagnefixFunctioneert',
                                                            definitie='Definitie nog toe te voegen voor eigenschap schakelpomp magnefix functioneert')

        self._vitale5EhboElektrocutieplaatAanwezig = EMAttribuut(field=StringField,
                                                                 naam='vitale5-EHBO-Elektrocutieplaat aanwezig',
                                                                 label='vitale5-EHBO-Elektrocutieplaat aanwezig',
                                                                 objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#HSDeel.vitale5EhboElektrocutieplaatAanwezig',
                                                                 definitie='Definitie nog toe te voegen voor eigenschap vitale5-EHBO-Elektrocutieplaat aanwezig')

    @property
    def ReserveZekeringenHsAanwezig(self):
        """Definitie nog toe te voegen voor eigenschap 3 reserve zekeringen HS aanwezig"""
        return self._ReserveZekeringenHsAanwezig.waarde

    @ReserveZekeringenHsAanwezig.setter
    def ReserveZekeringenHsAanwezig(self, value):
        self._ReserveZekeringenHsAanwezig.set_waarde(value, owner=self)

    @property
    def hsSchakelappTrafoStofSpinnenwebVrij(self):
        """Definitie nog toe te voegen voor eigenschap HS schakelapp/trafo stof&spinnenweb vrij"""
        return self._hsSchakelappTrafoStofSpinnenwebVrij.waarde

    @hsSchakelappTrafoStofSpinnenwebVrij.setter
    def hsSchakelappTrafoStofSpinnenwebVrij(self, value):
        self._hsSchakelappTrafoStofSpinnenwebVrij.set_waarde(value, owner=self)

    @property
    def alleKabelsGelabeldVolgensSchema(self):
        """Definitie nog toe te voegen voor eigenschap alle kabels gelabeld volgens schema"""
        return self._alleKabelsGelabeldVolgensSchema.waarde

    @alleKabelsGelabeldVolgensSchema.setter
    def alleKabelsGelabeldVolgensSchema(self, value):
        self._alleKabelsGelabeldVolgensSchema.set_waarde(value, owner=self)

    @property
    def attestGlobaleAardingAanwezig(self):
        """Definitie nog toe te voegen voor eigenschap attest globale aarding aanwezig"""
        return self._attestGlobaleAardingAanwezig.waarde

    @attestGlobaleAardingAanwezig.setter
    def attestGlobaleAardingAanwezig(self, value):
        self._attestGlobaleAardingAanwezig.set_waarde(value, owner=self)

    @property
    def componentenGelabeldVolgensSchema(self):
        """Definitie nog toe te voegen voor eigenschap componenten gelabeld volgens schema"""
        return self._componentenGelabeldVolgensSchema.waarde

    @componentenGelabeldVolgensSchema.setter
    def componentenGelabeldVolgensSchema(self, value):
        self._componentenGelabeldVolgensSchema.set_waarde(value, owner=self)

    @property
    def eendraadschemaAanwezig(self):
        """Definitie nog toe te voegen voor eigenschap eendraadschema aanwezig"""
        return self._eendraadschemaAanwezig.waarde

    @eendraadschemaAanwezig.setter
    def eendraadschemaAanwezig(self, value):
        self._eendraadschemaAanwezig.set_waarde(value, owner=self)

    @property
    def geenLekEindsluitingAankomstveldenDnb(self):
        """Definitie nog toe te voegen voor eigenschap geen lek eindsluiting aankomstvelden DNB"""
        return self._geenLekEindsluitingAankomstveldenDnb.waarde

    @geenLekEindsluitingAankomstveldenDnb.setter
    def geenLekEindsluitingAankomstveldenDnb(self, value):
        self._geenLekEindsluitingAankomstveldenDnb.set_waarde(value, owner=self)

    @property
    def geenLekEindsluitingTrafobeveilig(self):
        """Definitie nog toe te voegen voor eigenschap geen lek eindsluiting trafobeveilig"""
        return self._geenLekEindsluitingTrafobeveilig.waarde

    @geenLekEindsluitingTrafobeveilig.setter
    def geenLekEindsluitingTrafobeveilig(self, value):
        self._geenLekEindsluitingTrafobeveilig.set_waarde(value, owner=self)

    @property
    def geenTrafoOlieLekkage(self):
        """Definitie nog toe te voegen voor eigenschap geen trafo olie lekkage"""
        return self._geenTrafoOlieLekkage.waarde

    @geenTrafoOlieLekkage.setter
    def geenTrafoOlieLekkage(self, value):
        self._geenTrafoOlieLekkage.set_waarde(value, owner=self)

    @property
    def geenZichtbareDefectenOpenSchakelapp(self):
        """Definitie nog toe te voegen voor eigenschap geen zichtbare defecten open schakelapp"""
        return self._geenZichtbareDefectenOpenSchakelapp.waarde

    @geenZichtbareDefectenOpenSchakelapp.setter
    def geenZichtbareDefectenOpenSchakelapp(self, value):
        self._geenZichtbareDefectenOpenSchakelapp.set_waarde(value, owner=self)

    @property
    def geisoleerdeHandschInPerfecteStaat(self):
        """Definitie nog toe te voegen voor eigenschap geisoleerde handsch in perfecte staat"""
        return self._geisoleerdeHandschInPerfecteStaat.waarde

    @geisoleerdeHandschInPerfecteStaat.setter
    def geisoleerdeHandschInPerfecteStaat(self, value):
        self._geisoleerdeHandschInPerfecteStaat.set_waarde(value, owner=self)

    @property
    def geldigKeuringsverslagHsAanwezig(self):
        """Definitie nog toe te voegen voor eigenschap geldig keuringsverslag HS aanwezig"""
        return self._geldigKeuringsverslagHsAanwezig.waarde

    @geldigKeuringsverslagHsAanwezig.setter
    def geldigKeuringsverslagHsAanwezig(self, value):
        self._geldigKeuringsverslagHsAanwezig.set_waarde(value, owner=self)

    @property
    def isolatiemattenInGoedeStaat(self):
        """Definitie nog toe te voegen voor eigenschap isolatiematten in goede staat"""
        return self._isolatiemattenInGoedeStaat.waarde

    @isolatiemattenInGoedeStaat.setter
    def isolatiemattenInGoedeStaat(self, value):
        self._isolatiemattenInGoedeStaat.set_waarde(value, owner=self)

    @property
    def liggingsplanAardingenAanwezig(self):
        """Definitie nog toe te voegen voor eigenschap liggingsplan aardingen aanwezig"""
        return self._liggingsplanAardingenAanwezig.waarde

    @liggingsplanAardingenAanwezig.setter
    def liggingsplanAardingenAanwezig(self, value):
        self._liggingsplanAardingenAanwezig.set_waarde(value, owner=self)

    @property
    def neonSpanningsindicatorenFunctioneren(self):
        """Definitie nog toe te voegen voor eigenschap neon spanningsindicatoren functioneren"""
        return self._neonSpanningsindicatorenFunctioneren.waarde

    @neonSpanningsindicatorenFunctioneren.setter
    def neonSpanningsindicatorenFunctioneren(self, value):
        self._neonSpanningsindicatorenFunctioneren.set_waarde(value, owner=self)

    @property
    def notitieinspectie(self):
        """Definitie nog toe te voegen voor eigenschap notitie"""
        return self._notitieinspectie.waarde

    @notitieinspectie.setter
    def notitieinspectie(self, value):
        self._notitieinspectie.set_waarde(value, owner=self)

    @property
    def oliepeilTrafoNormaalNiveau(self):
        """Definitie nog toe te voegen voor eigenschap oliepeil trafo normaal niveau"""
        return self._oliepeilTrafoNormaalNiveau.waarde

    @oliepeilTrafoNormaalNiveau.setter
    def oliepeilTrafoNormaalNiveau(self, value):
        self._oliepeilTrafoNormaalNiveau.set_waarde(value, owner=self)

    @property
    def openBarenstelStofSpinnenwebVrij(self):
        """Definitie nog toe te voegen voor eigenschap open barenstel stof/spinnenweb vrij"""
        return self._openBarenstelStofSpinnenwebVrij.waarde

    @openBarenstelStofSpinnenwebVrij.setter
    def openBarenstelStofSpinnenwebVrij(self, value):
        self._openBarenstelStofSpinnenwebVrij.set_waarde(value, owner=self)

    @property
    def opmerkingenOverHsGedeelte(self):
        """Definitie nog toe te voegen voor eigenschap opmerkingen over HS gedeelte"""
        return self._opmerkingenOverHsGedeelte.waarde

    @opmerkingenOverHsGedeelte.setter
    def opmerkingenOverHsGedeelte(self, value):
        self._opmerkingenOverHsGedeelte.set_waarde(value, owner=self)

    @property
    def schakelbankInGoedeStaat(self):
        """Definitie nog toe te voegen voor eigenschap schakelbank in goede staat"""
        return self._schakelbankInGoedeStaat.waarde

    @schakelbankInGoedeStaat.setter
    def schakelbankInGoedeStaat(self, value):
        self._schakelbankInGoedeStaat.set_waarde(value, owner=self)

    @property
    def schakelhendelStokInGoedeStaat(self):
        """Definitie nog toe te voegen voor eigenschap schakelhendel / stok in goede staat"""
        return self._schakelhendelStokInGoedeStaat.waarde

    @schakelhendelStokInGoedeStaat.setter
    def schakelhendelStokInGoedeStaat(self, value):
        self._schakelhendelStokInGoedeStaat.set_waarde(value, owner=self)

    @property
    def schakelpompMagnefixFunctioneert(self):
        """Definitie nog toe te voegen voor eigenschap schakelpomp magnefix functioneert"""
        return self._schakelpompMagnefixFunctioneert.waarde

    @schakelpompMagnefixFunctioneert.setter
    def schakelpompMagnefixFunctioneert(self, value):
        self._schakelpompMagnefixFunctioneert.set_waarde(value, owner=self)

    @property
    def vitale5EhboElektrocutieplaatAanwezig(self):
        """Definitie nog toe te voegen voor eigenschap vitale5-EHBO-Elektrocutieplaat aanwezig"""
        return self._vitale5EhboElektrocutieplaatAanwezig.waarde

    @vitale5EhboElektrocutieplaatAanwezig.setter
    def vitale5EhboElektrocutieplaatAanwezig(self, value):
        self._vitale5EhboElektrocutieplaatAanwezig.set_waarde(value, owner=self)

