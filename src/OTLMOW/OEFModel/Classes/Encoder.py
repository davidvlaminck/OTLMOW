# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from OTLMOW.OTLModel.Datatypes.DateTimeField import DateTimeField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class Encoder(EMObject):
    """Camera-uitrusting : Het betreft hier een video-encoder. Deze vormt een analoog videosignaal om tot een digitale datastroom"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#Encoder'
    label = 'Encoder'

    def __init__(self):
        super().__init__()

        self._algemeneReinheidKast = EMAttribuut(field=StringField,
                                                 naam='algemene reinheid kast',
                                                 label='algemene reinheid kast',
                                                 objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#Encoder.algemeneReinheidKast',
                                                 definitie='Definitie nog toe te voegen voor eigenschap algemene reinheid kast')

        self._bezoekficheKastIngevuld = EMAttribuut(field=BooleanField,
                                                    naam='bezoekfiche kast ingevuld',
                                                    label='bezoekfiche kast ingevuld',
                                                    objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Encoder.bezoekficheKastIngevuld',
                                                    definitie='Definitie nog toe te voegen voor eigenschap bezoekfiche kast ingevuld')

        self._bodemKastDroog = EMAttribuut(field=StringField,
                                           naam='bodem kast droog',
                                           label='bodem kast droog',
                                           objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#Encoder.bodemKastDroog',
                                           definitie='Definitie nog toe te voegen voor eigenschap bodem kast droog')

        self._datumNieuweEncoder = EMAttribuut(field=DateField,
                                               naam='datum nieuwe encoder',
                                               label='datum nieuwe encoder',
                                               objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.datumNieuweEncoder',
                                               definitie='Definitie nog toe te voegen voor eigenschap datum nieuwe encoder')

        self._einde = EMAttribuut(field=DateTimeField,
                                  naam='einde',
                                  label='einde',
                                  objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.einde',
                                  definitie='Definitie nog toe te voegen voor eigenschap einde')

        self._encoderRedenDatumIngevenInv = EMAttribuut(field=StringField,
                                                        naam='encoder > reden? datum ingeven inv.',
                                                        label='encoder > reden? datum ingeven inv.',
                                                        objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.encoderRedenDatumIngevenInv',
                                                        definitie='Definitie nog toe te voegen voor eigenschap encoder > reden? datum ingeven inv.')

        self._encoderVervangen = EMAttribuut(field=BooleanField,
                                             naam='encoder vervangen?',
                                             label='encoder vervangen?',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.encoderVervangen',
                                             definitie='Definitie nog toe te voegen voor eigenschap encoder vervangen?')

        self._merkEnTypeEncoder = EMAttribuut(field=StringField,
                                              naam='merk en type encoder',
                                              label='merk en type encoder',
                                              objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#Encoder.merkEnTypeEncoder',
                                              definitie='Definitie nog toe te voegen voor eigenschap merk en type encoder')

        self._opmerkingAlgemeneReinheidKast = EMAttribuut(field=StringField,
                                                          naam='opmerking algemene reinheid kast',
                                                          label='opmerking algemene reinheid kast',
                                                          objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#Encoder.opmerkingAlgemeneReinheidKast',
                                                          definitie='Definitie nog toe te voegen voor eigenschap opmerking algemene reinheid kast')

        self._opmerkingBodemKast = EMAttribuut(field=StringField,
                                               naam='opmerking bodem kast',
                                               label='opmerking bodem kast',
                                               objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#Encoder.opmerkingBodemKast',
                                               definitie='Definitie nog toe te voegen voor eigenschap opmerking bodem kast')

        self._opmerkingInspectieOnderhoud = EMAttribuut(field=StringField,
                                                        naam='opmerking inspectie / onderhoud',
                                                        label='opmerking inspectie / onderhoud',
                                                        objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.opmerkingInspectieOnderhoud',
                                                        definitie='Definitie nog toe te voegen voor eigenschap opmerking inspectie / onderhoud')

        self._start = EMAttribuut(field=DateTimeField,
                                  naam='start',
                                  label='start',
                                  objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.start',
                                  definitie='Definitie nog toe te voegen voor eigenschap start')

        self._stofVerwijderen = EMAttribuut(field=BooleanField,
                                            naam='stof verwijderen',
                                            label='stof verwijderen',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Encoder.stofVerwijderen',
                                            definitie='Definitie nog toe te voegen voor eigenschap stof verwijderen')

    @property
    def algemeneReinheidKast(self):
        """Definitie nog toe te voegen voor eigenschap algemene reinheid kast"""
        return self._algemeneReinheidKast.waarde

    @algemeneReinheidKast.setter
    def algemeneReinheidKast(self, value):
        self._algemeneReinheidKast.set_waarde(value, owner=self)

    @property
    def bezoekficheKastIngevuld(self):
        """Definitie nog toe te voegen voor eigenschap bezoekfiche kast ingevuld"""
        return self._bezoekficheKastIngevuld.waarde

    @bezoekficheKastIngevuld.setter
    def bezoekficheKastIngevuld(self, value):
        self._bezoekficheKastIngevuld.set_waarde(value, owner=self)

    @property
    def bodemKastDroog(self):
        """Definitie nog toe te voegen voor eigenschap bodem kast droog"""
        return self._bodemKastDroog.waarde

    @bodemKastDroog.setter
    def bodemKastDroog(self, value):
        self._bodemKastDroog.set_waarde(value, owner=self)

    @property
    def datumNieuweEncoder(self):
        """Definitie nog toe te voegen voor eigenschap datum nieuwe encoder"""
        return self._datumNieuweEncoder.waarde

    @datumNieuweEncoder.setter
    def datumNieuweEncoder(self, value):
        self._datumNieuweEncoder.set_waarde(value, owner=self)

    @property
    def einde(self):
        """Definitie nog toe te voegen voor eigenschap einde"""
        return self._einde.waarde

    @einde.setter
    def einde(self, value):
        self._einde.set_waarde(value, owner=self)

    @property
    def encoderRedenDatumIngevenInv(self):
        """Definitie nog toe te voegen voor eigenschap encoder > reden? datum ingeven inv."""
        return self._encoderRedenDatumIngevenInv.waarde

    @encoderRedenDatumIngevenInv.setter
    def encoderRedenDatumIngevenInv(self, value):
        self._encoderRedenDatumIngevenInv.set_waarde(value, owner=self)

    @property
    def encoderVervangen(self):
        """Definitie nog toe te voegen voor eigenschap encoder vervangen?"""
        return self._encoderVervangen.waarde

    @encoderVervangen.setter
    def encoderVervangen(self, value):
        self._encoderVervangen.set_waarde(value, owner=self)

    @property
    def merkEnTypeEncoder(self):
        """Definitie nog toe te voegen voor eigenschap merk en type encoder"""
        return self._merkEnTypeEncoder.waarde

    @merkEnTypeEncoder.setter
    def merkEnTypeEncoder(self, value):
        self._merkEnTypeEncoder.set_waarde(value, owner=self)

    @property
    def opmerkingAlgemeneReinheidKast(self):
        """Definitie nog toe te voegen voor eigenschap opmerking algemene reinheid kast"""
        return self._opmerkingAlgemeneReinheidKast.waarde

    @opmerkingAlgemeneReinheidKast.setter
    def opmerkingAlgemeneReinheidKast(self, value):
        self._opmerkingAlgemeneReinheidKast.set_waarde(value, owner=self)

    @property
    def opmerkingBodemKast(self):
        """Definitie nog toe te voegen voor eigenschap opmerking bodem kast"""
        return self._opmerkingBodemKast.waarde

    @opmerkingBodemKast.setter
    def opmerkingBodemKast(self, value):
        self._opmerkingBodemKast.set_waarde(value, owner=self)

    @property
    def opmerkingInspectieOnderhoud(self):
        """Definitie nog toe te voegen voor eigenschap opmerking inspectie / onderhoud"""
        return self._opmerkingInspectieOnderhoud.waarde

    @opmerkingInspectieOnderhoud.setter
    def opmerkingInspectieOnderhoud(self, value):
        self._opmerkingInspectieOnderhoud.set_waarde(value, owner=self)

    @property
    def start(self):
        """Definitie nog toe te voegen voor eigenschap start"""
        return self._start.waarde

    @start.setter
    def start(self, value):
        self._start.set_waarde(value, owner=self)

    @property
    def stofVerwijderen(self):
        """Definitie nog toe te voegen voor eigenschap stof verwijderen"""
        return self._stofVerwijderen.waarde

    @stofVerwijderen.setter
    def stofVerwijderen(self, value):
        self._stofVerwijderen.set_waarde(value, owner=self)

