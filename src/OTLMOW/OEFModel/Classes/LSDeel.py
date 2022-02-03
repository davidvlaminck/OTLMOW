# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class LSDeel(EMObject):
    """Alle laagspanningscomponenten van Ã©Ã©n behuizing, uitgezonderd de aansluiting"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#LSDeel'
    label = 'Laagspanningsgedeelte'

    def __init__(self):
        super().__init__()

        self._alsBordStofSpinnenwebVrij = EMAttribuut(field=StringField,
                                                      naam='ALS bord stof & spinnenweb vrij',
                                                      label='ALS bord stof & spinnenweb vrij',
                                                      objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#LSDeel.alsBordStofSpinnenwebVrij',
                                                      definitie='Definitie nog toe te voegen voor eigenschap ALS bord stof & spinnenweb vrij',
                                                      owner=self)

        self._opmerkingenOverAlsGedeelte = EMAttribuut(field=StringField,
                                                       naam='Opmerkingen over ALS gedeelte',
                                                       label='Opmerkingen over ALS gedeelte',
                                                       objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#LSDeel.opmerkingenOverAlsGedeelte',
                                                       definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen over ALS gedeelte',
                                                       owner=self)

        self._afstandsbewakingOnline = EMAttribuut(field=StringField,
                                                   naam='afstandsbewaking online',
                                                   label='afstandsbewaking online',
                                                   objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#LSDeel.afstandsbewakingOnline',
                                                   definitie='Definitie nog toe te voegen voor eigenschap afstandsbewaking online',
                                                   owner=self)

        self._alleKabelsGelabeldVolgensSchema = EMAttribuut(field=StringField,
                                                            naam='alle kabels gelabeld volgens schema',
                                                            label='alle kabels gelabeld volgens schema',
                                                            objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.alleKabelsGelabeldVolgensSchema',
                                                            definitie='Definitie nog toe te voegen voor eigenschap alle kabels gelabeld volgens schema',
                                                            owner=self)

        self._bedradingsschemaAlsUpToDate = EMAttribuut(field=StringField,
                                                        naam='bedradingsschema ALS up to date',
                                                        label='bedradingsschema ALS up to date',
                                                        objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#LSDeel.bedradingsschemaAlsUpToDate',
                                                        definitie='Definitie nog toe te voegen voor eigenschap bedradingsschema ALS up to date',
                                                        owner=self)

        self._bordverlichtingAlsBordFunctioneert = EMAttribuut(field=StringField,
                                                               naam='bordverlichting ALS bord functioneert',
                                                               label='bordverlichting ALS bord functioneert',
                                                               objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#LSDeel.bordverlichtingAlsBordFunctioneert',
                                                               definitie='Definitie nog toe te voegen voor eigenschap bordverlichting ALS bord functioneert',
                                                               owner=self)

        self._componentenGelabeldVolgensSchema = EMAttribuut(field=StringField,
                                                             naam='componenten gelabeld volgens schema',
                                                             label='componenten gelabeld volgens schema',
                                                             objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.componentenGelabeldVolgensSchema',
                                                             definitie='Definitie nog toe te voegen voor eigenschap componenten gelabeld volgens schema',
                                                             owner=self)

        self._geldigKeuringsverslagAlsBordAanwezig = EMAttribuut(field=StringField,
                                                                 naam='geldig keuringsverslag ALS bord aanwezig',
                                                                 label='geldig keuringsverslag ALS bord aanwezig',
                                                                 objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#LSDeel.geldigKeuringsverslagAlsBordAanwezig',
                                                                 definitie='Definitie nog toe te voegen voor eigenschap geldig keuringsverslag ALS bord aanwezig',
                                                                 owner=self)

    @property
    def alsBordStofSpinnenwebVrij(self):
        """Definitie nog toe te voegen voor eigenschap ALS bord stof & spinnenweb vrij"""
        return self._alsBordStofSpinnenwebVrij.waarde

    @alsBordStofSpinnenwebVrij.setter
    def alsBordStofSpinnenwebVrij(self, value):
        self._alsBordStofSpinnenwebVrij.set_waarde(value, owner=self)

    @property
    def opmerkingenOverAlsGedeelte(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen over ALS gedeelte"""
        return self._opmerkingenOverAlsGedeelte.waarde

    @opmerkingenOverAlsGedeelte.setter
    def opmerkingenOverAlsGedeelte(self, value):
        self._opmerkingenOverAlsGedeelte.set_waarde(value, owner=self)

    @property
    def afstandsbewakingOnline(self):
        """Definitie nog toe te voegen voor eigenschap afstandsbewaking online"""
        return self._afstandsbewakingOnline.waarde

    @afstandsbewakingOnline.setter
    def afstandsbewakingOnline(self, value):
        self._afstandsbewakingOnline.set_waarde(value, owner=self)

    @property
    def alleKabelsGelabeldVolgensSchema(self):
        """Definitie nog toe te voegen voor eigenschap alle kabels gelabeld volgens schema"""
        return self._alleKabelsGelabeldVolgensSchema.waarde

    @alleKabelsGelabeldVolgensSchema.setter
    def alleKabelsGelabeldVolgensSchema(self, value):
        self._alleKabelsGelabeldVolgensSchema.set_waarde(value, owner=self)

    @property
    def bedradingsschemaAlsUpToDate(self):
        """Definitie nog toe te voegen voor eigenschap bedradingsschema ALS up to date"""
        return self._bedradingsschemaAlsUpToDate.waarde

    @bedradingsschemaAlsUpToDate.setter
    def bedradingsschemaAlsUpToDate(self, value):
        self._bedradingsschemaAlsUpToDate.set_waarde(value, owner=self)

    @property
    def bordverlichtingAlsBordFunctioneert(self):
        """Definitie nog toe te voegen voor eigenschap bordverlichting ALS bord functioneert"""
        return self._bordverlichtingAlsBordFunctioneert.waarde

    @bordverlichtingAlsBordFunctioneert.setter
    def bordverlichtingAlsBordFunctioneert(self, value):
        self._bordverlichtingAlsBordFunctioneert.set_waarde(value, owner=self)

    @property
    def componentenGelabeldVolgensSchema(self):
        """Definitie nog toe te voegen voor eigenschap componenten gelabeld volgens schema"""
        return self._componentenGelabeldVolgensSchema.waarde

    @componentenGelabeldVolgensSchema.setter
    def componentenGelabeldVolgensSchema(self, value):
        self._componentenGelabeldVolgensSchema.set_waarde(value, owner=self)

    @property
    def geldigKeuringsverslagAlsBordAanwezig(self):
        """Definitie nog toe te voegen voor eigenschap geldig keuringsverslag ALS bord aanwezig"""
        return self._geldigKeuringsverslagAlsBordAanwezig.waarde

    @geldigKeuringsverslagAlsBordAanwezig.setter
    def geldigKeuringsverslagAlsBordAanwezig(self, value):
        self._geldigKeuringsverslagAlsBordAanwezig.set_waarde(value, owner=self)

