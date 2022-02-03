# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from OTLMOW.OTLModel.Datatypes.DateTimeField import DateTimeField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class CCTV(EMObject):
    """GESLOTEN TV-CIRCUIT"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#CCTV'
    label = 'CCTV camera'

    def __init__(self):
        super().__init__()

        self._wifiAntenneAanwezig = EMAttribuut(field=BooleanField,
                                                naam='WIFI antenne aanwezig',
                                                label='WIFI antenne aanwezig',
                                                objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.wifiAntenneAanwezig',
                                                definitie='Definitie nog toe te voegen voor eigenschap WIFI antenne aanwezig',
                                                owner=self)

        self._beschadigingRoestvormingWaterdichtheid = EMAttribuut(field=StringField,
                                                                   naam='beschadiging roestvorming waterdichtheid',
                                                                   label='beschadiging roestvorming waterdichtheid',
                                                                   objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.beschadigingRoestvormingWaterdichtheid',
                                                                   definitie='Definitie nog toe te voegen voor eigenschap beschadiging roestvorming waterdichtheid',
                                                                   owner=self)

        self._cameraRedenDatumIngevenInventaris = EMAttribuut(field=StringField,
                                                              naam='camera > reden? datum ingeven inventaris',
                                                              label='camera > reden? datum ingeven inventaris',
                                                              objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.cameraRedenDatumIngevenInventaris',
                                                              definitie='Definitie nog toe te voegen voor eigenschap camera > reden? datum ingeven inventaris',
                                                              owner=self)

        self._cameraVervangen = EMAttribuut(field=BooleanField,
                                            naam='camera vervangen?',
                                            label='camera vervangen?',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.cameraVervangen',
                                            definitie='Definitie nog toe te voegen voor eigenschap camera vervangen?',
                                            owner=self)

        self._controleMet = EMAttribuut(field=StringField,
                                        naam='controle met',
                                        label='controle met',
                                        objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.controleMet',
                                        definitie='Definitie nog toe te voegen voor eigenschap controle met',
                                        owner=self)

        self._controleWerkingKwaliteitBijKlant = EMAttribuut(field=StringField,
                                                             naam='controle werking kwaliteit bij klant',
                                                             label='controle werking kwaliteit bij klant',
                                                             objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.controleWerkingKwaliteitBijKlant',
                                                             definitie='bij klant wordt het VVC -VTC - Politie bedoeld',
                                                             owner=self)

        self._datumNieuwVertrekGeplaatst = EMAttribuut(field=DateField,
                                                       naam='datum nieuw vertrek geplaatst',
                                                       label='datum nieuw vertrek geplaatst',
                                                       objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.datumNieuwVertrekGeplaatst',
                                                       definitie='Definitie nog toe te voegen voor eigenschap datum nieuw vertrek geplaatst',
                                                       owner=self)

        self._datumNieuweCamera = EMAttribuut(field=DateField,
                                              naam='datum nieuwe camera',
                                              label='datum nieuwe camera',
                                              objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.datumNieuweCamera',
                                              definitie='Definitie nog toe te voegen voor eigenschap datum nieuwe camera',
                                              owner=self)

        self._datumNieuweEncoder = EMAttribuut(field=DateField,
                                               naam='datum nieuwe encoder',
                                               label='datum nieuwe encoder',
                                               objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.datumNieuweEncoder',
                                               definitie='Definitie nog toe te voegen voor eigenschap datum nieuwe encoder',
                                               owner=self)

        self._datumNieuweMediaomvormer = EMAttribuut(field=DateField,
                                                     naam='datum nieuwe mediaomvormer',
                                                     label='datum nieuwe mediaomvormer',
                                                     objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.datumNieuweMediaomvormer',
                                                     definitie='Definitie nog toe te voegen voor eigenschap datum nieuwe mediaomvormer',
                                                     owner=self)

        self._einde = EMAttribuut(field=DateTimeField,
                                  naam='einde',
                                  label='einde',
                                  objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.einde',
                                  definitie='Definitie nog toe te voegen voor eigenschap einde',
                                  owner=self)

        self._encoderRedenDatumIngevenInv = EMAttribuut(field=StringField,
                                                        naam='encoder > reden? datum ingeven inv.',
                                                        label='encoder > reden? datum ingeven inv.',
                                                        objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.encoderRedenDatumIngevenInv',
                                                        definitie='Definitie nog toe te voegen voor eigenschap encoder > reden? datum ingeven inv.',
                                                        owner=self)

        self._encoderAanwezig = EMAttribuut(field=BooleanField,
                                            naam='encoder aanwezig?',
                                            label='encoder aanwezig?',
                                            objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.encoderAanwezig',
                                            definitie='Definitie nog toe te voegen voor eigenschap encoder aanwezig?',
                                            owner=self)

        self._encoderInExterneKast = EMAttribuut(field=BooleanField,
                                                 naam='encoder in externe kast',
                                                 label='encoder in externe kast',
                                                 objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.encoderInExterneKast',
                                                 definitie='Definitie nog toe te voegen voor eigenschap encoder in externe kast',
                                                 owner=self)

        self._encoderVervangen = EMAttribuut(field=BooleanField,
                                             naam='encoder vervangen?',
                                             label='encoder vervangen?',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.encoderVervangen',
                                             definitie='Definitie nog toe te voegen voor eigenschap encoder vervangen?',
                                             owner=self)

        self._fotoCamera = EMAttribuut(field=BooleanField,
                                       naam='foto camera',
                                       label='foto camera',
                                       objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.fotoCamera',
                                       definitie='Definitie nog toe te voegen voor eigenschap foto camera',
                                       owner=self)

        self._fotoCameraNaOnderhoud = EMAttribuut(field=BooleanField,
                                                  naam='foto camera na onderhoud',
                                                  label='foto camera na onderhoud',
                                                  objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.fotoCameraNaOnderhoud',
                                                  definitie='Definitie nog toe te voegen voor eigenschap foto camera na onderhoud',
                                                  owner=self)

        self._fotoInhoudPaalkast = EMAttribuut(field=BooleanField,
                                               naam='foto inhoud paalkast',
                                               label='foto inhoud paalkast',
                                               objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.fotoInhoudPaalkast',
                                               definitie='Definitie nog toe te voegen voor eigenschap foto inhoud paalkast',
                                               owner=self)

        self._mediaomvRedenDatumIngevenInv = EMAttribuut(field=StringField,
                                                         naam='mediaomv > reden ? datum ingeven inv.',
                                                         label='mediaomv > reden ? datum ingeven inv.',
                                                         objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#CCTV.mediaomvRedenDatumIngevenInv',
                                                         definitie='Definitie nog toe te voegen voor eigenschap mediaomv > reden ? datum ingeven inv.',
                                                         owner=self)

        self._mediaomvormerAanwezig = EMAttribuut(field=BooleanField,
                                                  naam='mediaomvormer aanwezig?',
                                                  label='mediaomvormer aanwezig?',
                                                  objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.mediaomvormerAanwezig',
                                                  definitie='Definitie nog toe te voegen voor eigenschap mediaomvormer aanwezig?',
                                                  owner=self)

        self._mediaomvormerVervangen = EMAttribuut(field=BooleanField,
                                                   naam='mediaomvormer vervangen?',
                                                   label='mediaomvormer vervangen?',
                                                   objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.mediaomvormerVervangen',
                                                   definitie='Definitie nog toe te voegen voor eigenschap mediaomvormer vervangen?',
                                                   owner=self)

        self._merkEnTypeCamera = EMAttribuut(field=StringField,
                                             naam='merk en type camera',
                                             label='merk en type camera',
                                             objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.merkEnTypeCamera',
                                             definitie='Definitie nog toe te voegen voor eigenschap merk en type camera',
                                             owner=self)

        self._notitieinspectie = EMAttribuut(field=StringField,
                                             naam='notitieInspectie',
                                             label='notitieInspectie',
                                             objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.notitieinspectie',
                                             definitie='Definitie nog toe te voegen voor eigenschap notitie',
                                             owner=self)

        self._opmerkingBeeld = EMAttribuut(field=StringField,
                                           naam='opmerking beeld',
                                           label='opmerking beeld',
                                           objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.opmerkingBeeld',
                                           definitie='Definitie nog toe te voegen voor eigenschap opmerking beeld',
                                           owner=self)

        self._opmerkingBekabelingWartels = EMAttribuut(field=StringField,
                                                       naam='opmerking bekabeling wartels',
                                                       label='opmerking bekabeling wartels',
                                                       objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.opmerkingBekabelingWartels',
                                                       definitie='Definitie nog toe te voegen voor eigenschap opmerking bekabeling wartels',
                                                       owner=self)

        self._opmerkingBeschRoestWaterdichtheid = EMAttribuut(field=StringField,
                                                              naam='opmerking besch/roest/waterdichtheid',
                                                              label='opmerking besch/roest/waterdichtheid',
                                                              objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.opmerkingBeschRoestWaterdichtheid',
                                                              definitie='Definitie nog toe te voegen voor eigenschap opmerking besch/roest/waterdichtheid',
                                                              owner=self)

        self._opmerkingControleKlant = EMAttribuut(field=StringField,
                                                   naam='opmerking controle klant',
                                                   label='opmerking controle klant',
                                                   objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.opmerkingControleKlant',
                                                   definitie='Definitie nog toe te voegen voor eigenschap opmerking controle klant',
                                                   owner=self)

        self._opmerkingInspectieOnderhoud = EMAttribuut(field=StringField,
                                                        naam='opmerking inspectie / onderhoud',
                                                        label='opmerking inspectie / onderhoud',
                                                        objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.opmerkingInspectieOnderhoud',
                                                        definitie='Definitie nog toe te voegen voor eigenschap opmerking inspectie / onderhoud',
                                                        owner=self)

        self._opmerkingStaatBekabelingElementen = EMAttribuut(field=StringField,
                                                              naam='opmerking staat bekabeling elementen',
                                                              label='opmerking staat bekabeling elementen',
                                                              objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.opmerkingStaatBekabelingElementen',
                                                              definitie='Definitie nog toe te voegen voor eigenschap opmerking staat bekabeling elementen',
                                                              owner=self)

        self._opmerkingStaatBekabelingGrondCa = EMAttribuut(field=StringField,
                                                            naam='opmerking staat bekabeling grond - ca',
                                                            label='opmerking staat bekabeling grond - ca',
                                                            objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.opmerkingStaatBekabelingGrondCa',
                                                            definitie='Definitie nog toe te voegen voor eigenschap opmerking staat bekabeling grond - ca',
                                                            owner=self)

        self._opmerkingStaatBeugelsBevestiging = EMAttribuut(field=StringField,
                                                             naam='opmerking staat beugels/ bevestiging',
                                                             label='opmerking staat beugels/ bevestiging',
                                                             objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.opmerkingStaatBeugelsBevestiging',
                                                             definitie='Definitie nog toe te voegen voor eigenschap opmerking staat beugels/ bevestiging',
                                                             owner=self)

        self._opmerkingStaatKabelbegeleiding = EMAttribuut(field=StringField,
                                                           naam='opmerking staat kabelbegeleiding',
                                                           label='opmerking staat kabelbegeleiding',
                                                           objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.opmerkingStaatKabelbegeleiding',
                                                           definitie='Definitie nog toe te voegen voor eigenschap opmerking staat kabelbegeleiding',
                                                           owner=self)

        self._opmerkingStaatSiliconen = EMAttribuut(field=StringField,
                                                    naam='opmerking staat siliconen',
                                                    label='opmerking staat siliconen',
                                                    objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.opmerkingStaatSiliconen',
                                                    definitie='Definitie nog toe te voegen voor eigenschap opmerking staat siliconen',
                                                    owner=self)

        self._opmerkingStaatWifiAntenne = EMAttribuut(field=StringField,
                                                      naam='opmerking staat wifi antenne',
                                                      label='opmerking staat wifi antenne',
                                                      objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.opmerkingStaatWifiAntenne',
                                                      definitie='Definitie nog toe te voegen voor eigenschap opmerking staat wifi antenne',
                                                      owner=self)

        self._opmerkingWartels = EMAttribuut(field=StringField,
                                             naam='opmerking wartels',
                                             label='opmerking wartels',
                                             objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.opmerkingWartels',
                                             definitie='Definitie nog toe te voegen voor eigenschap opmerking wartels',
                                             owner=self)

        self._opmerkingWaterdichtheid = EMAttribuut(field=StringField,
                                                    naam='opmerking waterdichtheid',
                                                    label='opmerking waterdichtheid',
                                                    objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.opmerkingWaterdichtheid',
                                                    definitie='Definitie nog toe te voegen voor eigenschap opmerking waterdichtheid',
                                                    owner=self)

        self._overigeVervangenElementen = EMAttribuut(field=StringField,
                                                      naam='overige vervangen elementen',
                                                      label='overige vervangen elementen',
                                                      objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.overigeVervangenElementen',
                                                      definitie='Definitie nog toe te voegen voor eigenschap overige vervangen elementen',
                                                      owner=self)

        self._paalkastAanwezig = EMAttribuut(field=BooleanField,
                                             naam='paalkast aanwezig',
                                             label='paalkast aanwezig',
                                             objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.paalkastAanwezig',
                                             definitie='Definitie nog toe te voegen voor eigenschap paalkast aanwezig',
                                             owner=self)

        self._paalkastStaatBekabelingElementen = EMAttribuut(field=StringField,
                                                             naam='paalkast staat bekabeling elementen',
                                                             label='paalkast staat bekabeling elementen',
                                                             objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.paalkastStaatBekabelingElementen',
                                                             definitie='Definitie nog toe te voegen voor eigenschap paalkast staat bekabeling elementen',
                                                             owner=self)

        self._paalkastStaatConnectieGrondCamera = EMAttribuut(field=StringField,
                                                              naam='paalkast staat connectie grond - camera',
                                                              label='paalkast staat connectie grond - camera',
                                                              objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.paalkastStaatConnectieGrondCamera',
                                                              definitie='Definitie nog toe te voegen voor eigenschap paalkast staat connectie grond - camera',
                                                              owner=self)

        self._paalkastStaatSiliconen = EMAttribuut(field=StringField,
                                                   naam='paalkast staat siliconen',
                                                   label='paalkast staat siliconen',
                                                   objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.paalkastStaatSiliconen',
                                                   definitie='Definitie nog toe te voegen voor eigenschap paalkast staat siliconen',
                                                   owner=self)

        self._paalkastStaatWartels = EMAttribuut(field=StringField,
                                                 naam='paalkast staat wartels',
                                                 label='paalkast staat wartels',
                                                 objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.paalkastStaatWartels',
                                                 definitie='Definitie nog toe te voegen voor eigenschap paalkast staat wartels',
                                                 owner=self)

        self._paalkastWaterdichtheid = EMAttribuut(field=StringField,
                                                   naam='paalkast waterdichtheid',
                                                   label='paalkast waterdichtheid',
                                                   objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.paalkastWaterdichtheid',
                                                   definitie='Definitie nog toe te voegen voor eigenschap paalkast waterdichtheid',
                                                   owner=self)

        self._reinigingBeugelsBevestigingsmiddelen = EMAttribuut(field=BooleanField,
                                                                 naam='reiniging beugels, bevestigingsmiddelen',
                                                                 label='reiniging beugels, bevestigingsmiddelen',
                                                                 objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.reinigingBeugelsBevestigingsmiddelen',
                                                                 definitie='Definitie nog toe te voegen voor eigenschap reiniging beugels, bevestigingsmiddelen',
                                                                 owner=self)

        self._reinigingKabelbegeleidingBevestiging = EMAttribuut(field=BooleanField,
                                                                 naam='reiniging kabelbegeleiding bevestiging',
                                                                 label='reiniging kabelbegeleiding bevestiging',
                                                                 objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.reinigingKabelbegeleidingBevestiging',
                                                                 definitie='Definitie nog toe te voegen voor eigenschap reiniging kabelbegeleiding bevestiging',
                                                                 owner=self)

        self._reinigingKabelsEnGeleidersAanPaal = EMAttribuut(field=BooleanField,
                                                              naam='reiniging kabels en geleiders aan paal',
                                                              label='reiniging kabels en geleiders aan paal',
                                                              objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.reinigingKabelsEnGeleidersAanPaal',
                                                              definitie='Definitie nog toe te voegen voor eigenschap reiniging kabels en geleiders aan paal',
                                                              owner=self)

        self._reinigingLensEnBehuizing = EMAttribuut(field=BooleanField,
                                                     naam='reiniging lens en behuizing',
                                                     label='reiniging lens en behuizing',
                                                     objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.reinigingLensEnBehuizing',
                                                     definitie='Definitie nog toe te voegen voor eigenschap reiniging lens en behuizing',
                                                     owner=self)

        self._staatStevigheidKabelbegeleidingPaal = EMAttribuut(field=StringField,
                                                                naam='staat /stevigheid kabelbegeleiding paal',
                                                                label='staat /stevigheid kabelbegeleiding paal',
                                                                objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.staatStevigheidKabelbegeleidingPaal',
                                                                definitie='Definitie nog toe te voegen voor eigenschap staat /stevigheid kabelbegeleiding paal',
                                                                owner=self)

        self._staatBekabelingEnWartels = EMAttribuut(field=StringField,
                                                     naam='staat bekabeling en wartels',
                                                     label='staat bekabeling en wartels',
                                                     objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.staatBekabelingEnWartels',
                                                     definitie='Definitie nog toe te voegen voor eigenschap staat bekabeling en wartels',
                                                     owner=self)

        self._staatBeugelBevestigingCamera = EMAttribuut(field=StringField,
                                                         naam='staat beugel / bevestiging camera',
                                                         label='staat beugel / bevestiging camera',
                                                         objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.staatBeugelBevestigingCamera',
                                                         definitie='Definitie nog toe te voegen voor eigenschap staat beugel / bevestiging camera',
                                                         owner=self)

        self._staatWifiAntenne = EMAttribuut(field=StringField,
                                             naam='staat wifi antenne',
                                             label='staat wifi antenne',
                                             objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.staatWifiAntenne',
                                             definitie='Definitie nog toe te voegen voor eigenschap staat wifi antenne',
                                             owner=self)

        self._start = EMAttribuut(field=DateTimeField,
                                  naam='start',
                                  label='start',
                                  objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.start',
                                  definitie='Definitie nog toe te voegen voor eigenschap start',
                                  owner=self)

        self._vertrekRedenDatumIngevenInv = EMAttribuut(field=StringField,
                                                        naam='vertrek > reden? datum ingeven inv.',
                                                        label='vertrek > reden? datum ingeven inv.',
                                                        objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.vertrekRedenDatumIngevenInv',
                                                        definitie='Definitie nog toe te voegen voor eigenschap vertrek > reden? datum ingeven inv.',
                                                        owner=self)

        self._vertrekAanwezig = EMAttribuut(field=BooleanField,
                                            naam='vertrek aanwezig?',
                                            label='vertrek aanwezig?',
                                            objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.vertrekAanwezig',
                                            definitie='Definitie nog toe te voegen voor eigenschap vertrek aanwezig?',
                                            owner=self)

        self._vertrekVervangen = EMAttribuut(field=BooleanField,
                                             naam='vertrek vervangen?',
                                             label='vertrek vervangen?',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.vertrekVervangen',
                                             definitie='Definitie nog toe te voegen voor eigenschap vertrek vervangen?',
                                             owner=self)

        self._werkingEnKwaliteitBeeld = EMAttribuut(field=StringField,
                                                    naam='werking en kwaliteit beeld',
                                                    label='werking en kwaliteit beeld',
                                                    objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.werkingEnKwaliteitBeeld',
                                                    definitie='Definitie nog toe te voegen voor eigenschap werking en kwaliteit beeld',
                                                    owner=self)

    @property
    def wifiAntenneAanwezig(self):
        """Definitie nog toe te voegen voor eigenschap WIFI antenne aanwezig"""
        return self._wifiAntenneAanwezig.waarde

    @wifiAntenneAanwezig.setter
    def wifiAntenneAanwezig(self, value):
        self._wifiAntenneAanwezig.set_waarde(value, owner=self)

    @property
    def beschadigingRoestvormingWaterdichtheid(self):
        """Definitie nog toe te voegen voor eigenschap beschadiging roestvorming waterdichtheid"""
        return self._beschadigingRoestvormingWaterdichtheid.waarde

    @beschadigingRoestvormingWaterdichtheid.setter
    def beschadigingRoestvormingWaterdichtheid(self, value):
        self._beschadigingRoestvormingWaterdichtheid.set_waarde(value, owner=self)

    @property
    def cameraRedenDatumIngevenInventaris(self):
        """Definitie nog toe te voegen voor eigenschap camera > reden? datum ingeven inventaris"""
        return self._cameraRedenDatumIngevenInventaris.waarde

    @cameraRedenDatumIngevenInventaris.setter
    def cameraRedenDatumIngevenInventaris(self, value):
        self._cameraRedenDatumIngevenInventaris.set_waarde(value, owner=self)

    @property
    def cameraVervangen(self):
        """Definitie nog toe te voegen voor eigenschap camera vervangen?"""
        return self._cameraVervangen.waarde

    @cameraVervangen.setter
    def cameraVervangen(self, value):
        self._cameraVervangen.set_waarde(value, owner=self)

    @property
    def controleMet(self):
        """Definitie nog toe te voegen voor eigenschap controle met"""
        return self._controleMet.waarde

    @controleMet.setter
    def controleMet(self, value):
        self._controleMet.set_waarde(value, owner=self)

    @property
    def controleWerkingKwaliteitBijKlant(self):
        """bij klant wordt het VVC -VTC - Politie bedoeld"""
        return self._controleWerkingKwaliteitBijKlant.waarde

    @controleWerkingKwaliteitBijKlant.setter
    def controleWerkingKwaliteitBijKlant(self, value):
        self._controleWerkingKwaliteitBijKlant.set_waarde(value, owner=self)

    @property
    def datumNieuwVertrekGeplaatst(self):
        """Definitie nog toe te voegen voor eigenschap datum nieuw vertrek geplaatst"""
        return self._datumNieuwVertrekGeplaatst.waarde

    @datumNieuwVertrekGeplaatst.setter
    def datumNieuwVertrekGeplaatst(self, value):
        self._datumNieuwVertrekGeplaatst.set_waarde(value, owner=self)

    @property
    def datumNieuweCamera(self):
        """Definitie nog toe te voegen voor eigenschap datum nieuwe camera"""
        return self._datumNieuweCamera.waarde

    @datumNieuweCamera.setter
    def datumNieuweCamera(self, value):
        self._datumNieuweCamera.set_waarde(value, owner=self)

    @property
    def datumNieuweEncoder(self):
        """Definitie nog toe te voegen voor eigenschap datum nieuwe encoder"""
        return self._datumNieuweEncoder.waarde

    @datumNieuweEncoder.setter
    def datumNieuweEncoder(self, value):
        self._datumNieuweEncoder.set_waarde(value, owner=self)

    @property
    def datumNieuweMediaomvormer(self):
        """Definitie nog toe te voegen voor eigenschap datum nieuwe mediaomvormer"""
        return self._datumNieuweMediaomvormer.waarde

    @datumNieuweMediaomvormer.setter
    def datumNieuweMediaomvormer(self, value):
        self._datumNieuweMediaomvormer.set_waarde(value, owner=self)

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
    def encoderAanwezig(self):
        """Definitie nog toe te voegen voor eigenschap encoder aanwezig?"""
        return self._encoderAanwezig.waarde

    @encoderAanwezig.setter
    def encoderAanwezig(self, value):
        self._encoderAanwezig.set_waarde(value, owner=self)

    @property
    def encoderInExterneKast(self):
        """Definitie nog toe te voegen voor eigenschap encoder in externe kast"""
        return self._encoderInExterneKast.waarde

    @encoderInExterneKast.setter
    def encoderInExterneKast(self, value):
        self._encoderInExterneKast.set_waarde(value, owner=self)

    @property
    def encoderVervangen(self):
        """Definitie nog toe te voegen voor eigenschap encoder vervangen?"""
        return self._encoderVervangen.waarde

    @encoderVervangen.setter
    def encoderVervangen(self, value):
        self._encoderVervangen.set_waarde(value, owner=self)

    @property
    def fotoCamera(self):
        """Definitie nog toe te voegen voor eigenschap foto camera"""
        return self._fotoCamera.waarde

    @fotoCamera.setter
    def fotoCamera(self, value):
        self._fotoCamera.set_waarde(value, owner=self)

    @property
    def fotoCameraNaOnderhoud(self):
        """Definitie nog toe te voegen voor eigenschap foto camera na onderhoud"""
        return self._fotoCameraNaOnderhoud.waarde

    @fotoCameraNaOnderhoud.setter
    def fotoCameraNaOnderhoud(self, value):
        self._fotoCameraNaOnderhoud.set_waarde(value, owner=self)

    @property
    def fotoInhoudPaalkast(self):
        """Definitie nog toe te voegen voor eigenschap foto inhoud paalkast"""
        return self._fotoInhoudPaalkast.waarde

    @fotoInhoudPaalkast.setter
    def fotoInhoudPaalkast(self, value):
        self._fotoInhoudPaalkast.set_waarde(value, owner=self)

    @property
    def mediaomvRedenDatumIngevenInv(self):
        """Definitie nog toe te voegen voor eigenschap mediaomv > reden ? datum ingeven inv."""
        return self._mediaomvRedenDatumIngevenInv.waarde

    @mediaomvRedenDatumIngevenInv.setter
    def mediaomvRedenDatumIngevenInv(self, value):
        self._mediaomvRedenDatumIngevenInv.set_waarde(value, owner=self)

    @property
    def mediaomvormerAanwezig(self):
        """Definitie nog toe te voegen voor eigenschap mediaomvormer aanwezig?"""
        return self._mediaomvormerAanwezig.waarde

    @mediaomvormerAanwezig.setter
    def mediaomvormerAanwezig(self, value):
        self._mediaomvormerAanwezig.set_waarde(value, owner=self)

    @property
    def mediaomvormerVervangen(self):
        """Definitie nog toe te voegen voor eigenschap mediaomvormer vervangen?"""
        return self._mediaomvormerVervangen.waarde

    @mediaomvormerVervangen.setter
    def mediaomvormerVervangen(self, value):
        self._mediaomvormerVervangen.set_waarde(value, owner=self)

    @property
    def merkEnTypeCamera(self):
        """Definitie nog toe te voegen voor eigenschap merk en type camera"""
        return self._merkEnTypeCamera.waarde

    @merkEnTypeCamera.setter
    def merkEnTypeCamera(self, value):
        self._merkEnTypeCamera.set_waarde(value, owner=self)

    @property
    def notitieinspectie(self):
        """Definitie nog toe te voegen voor eigenschap notitie"""
        return self._notitieinspectie.waarde

    @notitieinspectie.setter
    def notitieinspectie(self, value):
        self._notitieinspectie.set_waarde(value, owner=self)

    @property
    def opmerkingBeeld(self):
        """Definitie nog toe te voegen voor eigenschap opmerking beeld"""
        return self._opmerkingBeeld.waarde

    @opmerkingBeeld.setter
    def opmerkingBeeld(self, value):
        self._opmerkingBeeld.set_waarde(value, owner=self)

    @property
    def opmerkingBekabelingWartels(self):
        """Definitie nog toe te voegen voor eigenschap opmerking bekabeling wartels"""
        return self._opmerkingBekabelingWartels.waarde

    @opmerkingBekabelingWartels.setter
    def opmerkingBekabelingWartels(self, value):
        self._opmerkingBekabelingWartels.set_waarde(value, owner=self)

    @property
    def opmerkingBeschRoestWaterdichtheid(self):
        """Definitie nog toe te voegen voor eigenschap opmerking besch/roest/waterdichtheid"""
        return self._opmerkingBeschRoestWaterdichtheid.waarde

    @opmerkingBeschRoestWaterdichtheid.setter
    def opmerkingBeschRoestWaterdichtheid(self, value):
        self._opmerkingBeschRoestWaterdichtheid.set_waarde(value, owner=self)

    @property
    def opmerkingControleKlant(self):
        """Definitie nog toe te voegen voor eigenschap opmerking controle klant"""
        return self._opmerkingControleKlant.waarde

    @opmerkingControleKlant.setter
    def opmerkingControleKlant(self, value):
        self._opmerkingControleKlant.set_waarde(value, owner=self)

    @property
    def opmerkingInspectieOnderhoud(self):
        """Definitie nog toe te voegen voor eigenschap opmerking inspectie / onderhoud"""
        return self._opmerkingInspectieOnderhoud.waarde

    @opmerkingInspectieOnderhoud.setter
    def opmerkingInspectieOnderhoud(self, value):
        self._opmerkingInspectieOnderhoud.set_waarde(value, owner=self)

    @property
    def opmerkingStaatBekabelingElementen(self):
        """Definitie nog toe te voegen voor eigenschap opmerking staat bekabeling elementen"""
        return self._opmerkingStaatBekabelingElementen.waarde

    @opmerkingStaatBekabelingElementen.setter
    def opmerkingStaatBekabelingElementen(self, value):
        self._opmerkingStaatBekabelingElementen.set_waarde(value, owner=self)

    @property
    def opmerkingStaatBekabelingGrondCa(self):
        """Definitie nog toe te voegen voor eigenschap opmerking staat bekabeling grond - ca"""
        return self._opmerkingStaatBekabelingGrondCa.waarde

    @opmerkingStaatBekabelingGrondCa.setter
    def opmerkingStaatBekabelingGrondCa(self, value):
        self._opmerkingStaatBekabelingGrondCa.set_waarde(value, owner=self)

    @property
    def opmerkingStaatBeugelsBevestiging(self):
        """Definitie nog toe te voegen voor eigenschap opmerking staat beugels/ bevestiging"""
        return self._opmerkingStaatBeugelsBevestiging.waarde

    @opmerkingStaatBeugelsBevestiging.setter
    def opmerkingStaatBeugelsBevestiging(self, value):
        self._opmerkingStaatBeugelsBevestiging.set_waarde(value, owner=self)

    @property
    def opmerkingStaatKabelbegeleiding(self):
        """Definitie nog toe te voegen voor eigenschap opmerking staat kabelbegeleiding"""
        return self._opmerkingStaatKabelbegeleiding.waarde

    @opmerkingStaatKabelbegeleiding.setter
    def opmerkingStaatKabelbegeleiding(self, value):
        self._opmerkingStaatKabelbegeleiding.set_waarde(value, owner=self)

    @property
    def opmerkingStaatSiliconen(self):
        """Definitie nog toe te voegen voor eigenschap opmerking staat siliconen"""
        return self._opmerkingStaatSiliconen.waarde

    @opmerkingStaatSiliconen.setter
    def opmerkingStaatSiliconen(self, value):
        self._opmerkingStaatSiliconen.set_waarde(value, owner=self)

    @property
    def opmerkingStaatWifiAntenne(self):
        """Definitie nog toe te voegen voor eigenschap opmerking staat wifi antenne"""
        return self._opmerkingStaatWifiAntenne.waarde

    @opmerkingStaatWifiAntenne.setter
    def opmerkingStaatWifiAntenne(self, value):
        self._opmerkingStaatWifiAntenne.set_waarde(value, owner=self)

    @property
    def opmerkingWartels(self):
        """Definitie nog toe te voegen voor eigenschap opmerking wartels"""
        return self._opmerkingWartels.waarde

    @opmerkingWartels.setter
    def opmerkingWartels(self, value):
        self._opmerkingWartels.set_waarde(value, owner=self)

    @property
    def opmerkingWaterdichtheid(self):
        """Definitie nog toe te voegen voor eigenschap opmerking waterdichtheid"""
        return self._opmerkingWaterdichtheid.waarde

    @opmerkingWaterdichtheid.setter
    def opmerkingWaterdichtheid(self, value):
        self._opmerkingWaterdichtheid.set_waarde(value, owner=self)

    @property
    def overigeVervangenElementen(self):
        """Definitie nog toe te voegen voor eigenschap overige vervangen elementen"""
        return self._overigeVervangenElementen.waarde

    @overigeVervangenElementen.setter
    def overigeVervangenElementen(self, value):
        self._overigeVervangenElementen.set_waarde(value, owner=self)

    @property
    def paalkastAanwezig(self):
        """Definitie nog toe te voegen voor eigenschap paalkast aanwezig"""
        return self._paalkastAanwezig.waarde

    @paalkastAanwezig.setter
    def paalkastAanwezig(self, value):
        self._paalkastAanwezig.set_waarde(value, owner=self)

    @property
    def paalkastStaatBekabelingElementen(self):
        """Definitie nog toe te voegen voor eigenschap paalkast staat bekabeling elementen"""
        return self._paalkastStaatBekabelingElementen.waarde

    @paalkastStaatBekabelingElementen.setter
    def paalkastStaatBekabelingElementen(self, value):
        self._paalkastStaatBekabelingElementen.set_waarde(value, owner=self)

    @property
    def paalkastStaatConnectieGrondCamera(self):
        """Definitie nog toe te voegen voor eigenschap paalkast staat connectie grond - camera"""
        return self._paalkastStaatConnectieGrondCamera.waarde

    @paalkastStaatConnectieGrondCamera.setter
    def paalkastStaatConnectieGrondCamera(self, value):
        self._paalkastStaatConnectieGrondCamera.set_waarde(value, owner=self)

    @property
    def paalkastStaatSiliconen(self):
        """Definitie nog toe te voegen voor eigenschap paalkast staat siliconen"""
        return self._paalkastStaatSiliconen.waarde

    @paalkastStaatSiliconen.setter
    def paalkastStaatSiliconen(self, value):
        self._paalkastStaatSiliconen.set_waarde(value, owner=self)

    @property
    def paalkastStaatWartels(self):
        """Definitie nog toe te voegen voor eigenschap paalkast staat wartels"""
        return self._paalkastStaatWartels.waarde

    @paalkastStaatWartels.setter
    def paalkastStaatWartels(self, value):
        self._paalkastStaatWartels.set_waarde(value, owner=self)

    @property
    def paalkastWaterdichtheid(self):
        """Definitie nog toe te voegen voor eigenschap paalkast waterdichtheid"""
        return self._paalkastWaterdichtheid.waarde

    @paalkastWaterdichtheid.setter
    def paalkastWaterdichtheid(self, value):
        self._paalkastWaterdichtheid.set_waarde(value, owner=self)

    @property
    def reinigingBeugelsBevestigingsmiddelen(self):
        """Definitie nog toe te voegen voor eigenschap reiniging beugels, bevestigingsmiddelen"""
        return self._reinigingBeugelsBevestigingsmiddelen.waarde

    @reinigingBeugelsBevestigingsmiddelen.setter
    def reinigingBeugelsBevestigingsmiddelen(self, value):
        self._reinigingBeugelsBevestigingsmiddelen.set_waarde(value, owner=self)

    @property
    def reinigingKabelbegeleidingBevestiging(self):
        """Definitie nog toe te voegen voor eigenschap reiniging kabelbegeleiding bevestiging"""
        return self._reinigingKabelbegeleidingBevestiging.waarde

    @reinigingKabelbegeleidingBevestiging.setter
    def reinigingKabelbegeleidingBevestiging(self, value):
        self._reinigingKabelbegeleidingBevestiging.set_waarde(value, owner=self)

    @property
    def reinigingKabelsEnGeleidersAanPaal(self):
        """Definitie nog toe te voegen voor eigenschap reiniging kabels en geleiders aan paal"""
        return self._reinigingKabelsEnGeleidersAanPaal.waarde

    @reinigingKabelsEnGeleidersAanPaal.setter
    def reinigingKabelsEnGeleidersAanPaal(self, value):
        self._reinigingKabelsEnGeleidersAanPaal.set_waarde(value, owner=self)

    @property
    def reinigingLensEnBehuizing(self):
        """Definitie nog toe te voegen voor eigenschap reiniging lens en behuizing"""
        return self._reinigingLensEnBehuizing.waarde

    @reinigingLensEnBehuizing.setter
    def reinigingLensEnBehuizing(self, value):
        self._reinigingLensEnBehuizing.set_waarde(value, owner=self)

    @property
    def staatStevigheidKabelbegeleidingPaal(self):
        """Definitie nog toe te voegen voor eigenschap staat /stevigheid kabelbegeleiding paal"""
        return self._staatStevigheidKabelbegeleidingPaal.waarde

    @staatStevigheidKabelbegeleidingPaal.setter
    def staatStevigheidKabelbegeleidingPaal(self, value):
        self._staatStevigheidKabelbegeleidingPaal.set_waarde(value, owner=self)

    @property
    def staatBekabelingEnWartels(self):
        """Definitie nog toe te voegen voor eigenschap staat bekabeling en wartels"""
        return self._staatBekabelingEnWartels.waarde

    @staatBekabelingEnWartels.setter
    def staatBekabelingEnWartels(self, value):
        self._staatBekabelingEnWartels.set_waarde(value, owner=self)

    @property
    def staatBeugelBevestigingCamera(self):
        """Definitie nog toe te voegen voor eigenschap staat beugel / bevestiging camera"""
        return self._staatBeugelBevestigingCamera.waarde

    @staatBeugelBevestigingCamera.setter
    def staatBeugelBevestigingCamera(self, value):
        self._staatBeugelBevestigingCamera.set_waarde(value, owner=self)

    @property
    def staatWifiAntenne(self):
        """Definitie nog toe te voegen voor eigenschap staat wifi antenne"""
        return self._staatWifiAntenne.waarde

    @staatWifiAntenne.setter
    def staatWifiAntenne(self, value):
        self._staatWifiAntenne.set_waarde(value, owner=self)

    @property
    def start(self):
        """Definitie nog toe te voegen voor eigenschap start"""
        return self._start.waarde

    @start.setter
    def start(self, value):
        self._start.set_waarde(value, owner=self)

    @property
    def vertrekRedenDatumIngevenInv(self):
        """Definitie nog toe te voegen voor eigenschap vertrek > reden? datum ingeven inv."""
        return self._vertrekRedenDatumIngevenInv.waarde

    @vertrekRedenDatumIngevenInv.setter
    def vertrekRedenDatumIngevenInv(self, value):
        self._vertrekRedenDatumIngevenInv.set_waarde(value, owner=self)

    @property
    def vertrekAanwezig(self):
        """Definitie nog toe te voegen voor eigenschap vertrek aanwezig?"""
        return self._vertrekAanwezig.waarde

    @vertrekAanwezig.setter
    def vertrekAanwezig(self, value):
        self._vertrekAanwezig.set_waarde(value, owner=self)

    @property
    def vertrekVervangen(self):
        """Definitie nog toe te voegen voor eigenschap vertrek vervangen?"""
        return self._vertrekVervangen.waarde

    @vertrekVervangen.setter
    def vertrekVervangen(self, value):
        self._vertrekVervangen.set_waarde(value, owner=self)

    @property
    def werkingEnKwaliteitBeeld(self):
        """Definitie nog toe te voegen voor eigenschap werking en kwaliteit beeld"""
        return self._werkingEnKwaliteitBeeld.waarde

    @werkingEnKwaliteitBeeld.setter
    def werkingEnKwaliteitBeeld(self, value):
        self._werkingEnKwaliteitBeeld.set_waarde(value, owner=self)

