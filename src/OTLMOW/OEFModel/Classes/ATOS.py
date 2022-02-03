# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from OTLMOW.OTLModel.Datatypes.DateTimeField import DateTimeField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class ATOS(EMObject):
    """ATOS-KNOOP"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#ATOS'
    label = 'ATOS-knoop'

    def __init__(self):
        super().__init__()

        self._DubbeleVoedingOk = EMAttribuut(field=StringField,
                                             naam='(Dubbele) voeding OK',
                                             label='(Dubbele) voeding OK',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.DubbeleVoedingOk',
                                             definitie='Definitie nog toe te voegen voor eigenschap (Dubbele) voeding OK',
                                             owner=self)

        self._abbameldaInstallatieOk = EMAttribuut(field=BooleanField,
                                                   naam='ABBAMelda installatie OK',
                                                   label='ABBAMelda installatie OK',
                                                   objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.abbameldaInstallatieOk',
                                                   definitie='Definitie nog toe te voegen voor eigenschap ABBAMelda installatie OK',
                                                   owner=self)

        self._abbameldaOperoepGemaakt = EMAttribuut(field=BooleanField,
                                                    naam='ABBAMelda operoep gemaakt',
                                                    label='ABBAMelda operoep gemaakt',
                                                    objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.abbameldaOperoepGemaakt',
                                                    definitie='Definitie nog toe te voegen voor eigenschap ABBAMelda operoep gemaakt',
                                                    owner=self)

        self._aanpassingenNodig = EMAttribuut(field=StringField,
                                              naam='Aanpassingen nodig',
                                              label='Aanpassingen nodig',
                                              objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.aanpassingenNodig',
                                              definitie='Definitie nog toe te voegen voor eigenschap Aanpassingen nodig',
                                              owner=self)

        self._algemeneToestandLocatieOk = EMAttribuut(field=BooleanField,
                                                      naam='Algemene toestand locatie OK',
                                                      label='Algemene toestand locatie OK',
                                                      objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.algemeneToestandLocatieOk',
                                                      definitie='Definitie nog toe te voegen voor eigenschap Algemene toestand locatie OK',
                                                      owner=self)

        self._apparatuurFiltersVervangen = EMAttribuut(field=BooleanField,
                                                       naam='Apparatuur filters vervangen',
                                                       label='Apparatuur filters vervangen',
                                                       objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.apparatuurFiltersVervangen',
                                                       definitie='Definitie nog toe te voegen voor eigenschap Apparatuur filters vervangen',
                                                       owner=self)

        self._apparatuurGereinigd = EMAttribuut(field=BooleanField,
                                                naam='Apparatuur gereinigd',
                                                label='Apparatuur gereinigd',
                                                objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.apparatuurGereinigd',
                                                definitie='Definitie nog toe te voegen voor eigenschap Apparatuur gereinigd',
                                                owner=self)

        self._apparatuurVentilatieOk = EMAttribuut(field=BooleanField,
                                                   naam='Apparatuur ventilatie OK',
                                                   label='Apparatuur ventilatie OK',
                                                   objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.apparatuurVentilatieOk',
                                                   definitie='Definitie nog toe te voegen voor eigenschap Apparatuur ventilatie OK',
                                                   owner=self)

        self._apparatuurVrijVanAlarmen = EMAttribuut(field=BooleanField,
                                                     naam='Apparatuur vrij van alarmen',
                                                     label='Apparatuur vrij van alarmen',
                                                     objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.apparatuurVrijVanAlarmen',
                                                     definitie='Definitie nog toe te voegen voor eigenschap Apparatuur vrij van alarmen',
                                                     owner=self)

        self._batterijVervangen = EMAttribuut(field=BooleanField,
                                              naam='Batterij vervangen',
                                              label='Batterij vervangen',
                                              objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.batterijVervangen',
                                              definitie='Definitie nog toe te voegen voor eigenschap Batterij vervangen',
                                              owner=self)

        self._batterijVervangenOp = EMAttribuut(field=DateField,
                                                naam='Batterij vervangen op',
                                                label='Batterij vervangen op',
                                                objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.batterijVervangenOp',
                                                definitie='Definitie nog toe te voegen voor eigenschap Batterij vervangen op',
                                                owner=self)

        self._beschrijvingInterventie = EMAttribuut(field=StringField,
                                                    naam='Beschrijving interventie',
                                                    label='Beschrijving interventie',
                                                    objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.beschrijvingInterventie',
                                                    definitie='Definitie nog toe te voegen voor eigenschap Beschrijving interventie',
                                                    owner=self)

        self._eindeAtos1 = EMAttribuut(field=DateTimeField,
                                       naam='Einde (ATOS 1)',
                                       label='Einde (ATOS 1)',
                                       objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#ATOS.eindeAtos1',
                                       definitie='Definitie nog toe te voegen voor eigenschap Einde (ATOS 1)',
                                       owner=self)

        self._eindeAtos = EMAttribuut(field=DateTimeField,
                                      naam='Einde (ATOS)',
                                      label='Einde (ATOS)',
                                      objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#ATOS.eindeAtos',
                                      definitie='Definitie nog toe te voegen voor eigenschap Einde (ATOS)',
                                      owner=self)

        self._elektrischPlanInstallatieOk = EMAttribuut(field=BooleanField,
                                                        naam='Elektrisch plan / installatie OK',
                                                        label='Elektrisch plan / installatie OK',
                                                        objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.elektrischPlanInstallatieOk',
                                                        definitie='Definitie nog toe te voegen voor eigenschap Elektrisch plan / installatie OK',
                                                        owner=self)

        self._elektrischPlanInstallatieOkOud = EMAttribuut(field=StringField,
                                                           naam='Elektrisch plan/installatie OK oud',
                                                           label='Elektrisch plan/installatie OK oud',
                                                           objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.elektrischPlanInstallatieOkOud',
                                                           definitie='Definitie nog toe te voegen voor eigenschap Elektrisch plan/installatie OK oud',
                                                           owner=self)

        self._fotoSApparatuurGemaakt = EMAttribuut(field=BooleanField,
                                                   naam="Foto's apparatuur gemaakt",
                                                   label="Foto's apparatuur gemaakt",
                                                   objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.fotoSApparatuurGemaakt',
                                                   definitie="Definitie nog toe te voegen voor eigenschap Foto\'s apparatuur gemaakt",
                                                   owner=self)

        self._glasvezelOkBevestigingLabels = EMAttribuut(field=BooleanField,
                                                         naam='Glasvezel OK (bevestiging, labels)',
                                                         label='Glasvezel OK (bevestiging, labels)',
                                                         objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.glasvezelOkBevestigingLabels',
                                                         definitie='Definitie nog toe te voegen voor eigenschap Glasvezel OK (bevestiging, labels)',
                                                         owner=self)

        self._glasvezelOkSelectielijst = EMAttribuut(field=StringField,
                                                     naam='Glasvezel OK selectielijst',
                                                     label='Glasvezel OK selectielijst',
                                                     objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.glasvezelOkSelectielijst',
                                                     definitie='Definitie nog toe te voegen voor eigenschap Glasvezel OK selectielijst',
                                                     owner=self)

        self._glasvezelConnectorsOk = EMAttribuut(field=BooleanField,
                                                  naam='Glasvezel connectors OK',
                                                  label='Glasvezel connectors OK',
                                                  objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.glasvezelConnectorsOk',
                                                  definitie='Definitie nog toe te voegen voor eigenschap Glasvezel connectors OK',
                                                  owner=self)

        self._glasvezelConnectorsSelectielijst = EMAttribuut(field=StringField,
                                                             naam='Glasvezel connectors selectielijst',
                                                             label='Glasvezel connectors selectielijst',
                                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#ATOS.glasvezelConnectorsSelectielijst',
                                                             definitie='Definitie nog toe te voegen voor eigenschap Glasvezel connectors selectielijst',
                                                             owner=self)

        self._klimatiseringLocatieOk = EMAttribuut(field=BooleanField,
                                                   naam='Klimatisering locatie OK',
                                                   label='Klimatisering locatie OK',
                                                   objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.klimatiseringLocatieOk',
                                                   definitie='Definitie nog toe te voegen voor eigenschap Klimatisering locatie OK',
                                                   owner=self)

        self._koperkabelOkBevestigingLabels = EMAttribuut(field=BooleanField,
                                                          naam='Koperkabel OK (bevestiging,labels)',
                                                          label='Koperkabel OK (bevestiging,labels)',
                                                          objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.koperkabelOkBevestigingLabels',
                                                          definitie='Definitie nog toe te voegen voor eigenschap Koperkabel OK (bevestiging,labels)',
                                                          owner=self)

        self._koperkabelOkSelectielijst = EMAttribuut(field=StringField,
                                                      naam='Koperkabel OK selectielijst',
                                                      label='Koperkabel OK selectielijst',
                                                      objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.koperkabelOkSelectielijst',
                                                      definitie='Definitie nog toe te voegen voor eigenschap Koperkabel OK selectielijst',
                                                      owner=self)

        self._locatieBereikbaar = EMAttribuut(field=BooleanField,
                                              naam='Locatie bereikbaar',
                                              label='Locatie bereikbaar',
                                              objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.locatieBereikbaar',
                                              definitie='Definitie nog toe te voegen voor eigenschap Locatie bereikbaar',
                                              owner=self)

        self._naarWie = EMAttribuut(field=StringField,
                                    naam='Naar wie',
                                    label='Naar wie',
                                    objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.naarWie',
                                    definitie='Definitie nog toe te voegen voor eigenschap Naar wie',
                                    owner=self)

        self._opmerkingenAtos1 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (ATOS 1)',
                                             label='Opmerkingen (ATOS 1)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#ATOS.opmerkingenAtos1',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 1)',
                                             owner=self)

        self._opmerkingenAtos10 = EMAttribuut(field=StringField,
                                              naam='Opmerkingen (ATOS 10)',
                                              label='Opmerkingen (ATOS 10)',
                                              objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#ATOS.opmerkingenAtos10',
                                              definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 10)',
                                              owner=self)

        self._opmerkingenAtos11 = EMAttribuut(field=StringField,
                                              naam='Opmerkingen (ATOS 11)',
                                              label='Opmerkingen (ATOS 11)',
                                              objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#ATOS.opmerkingenAtos11',
                                              definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 11)',
                                              owner=self)

        self._opmerkingenAtos12 = EMAttribuut(field=StringField,
                                              naam='Opmerkingen (ATOS 12)',
                                              label='Opmerkingen (ATOS 12)',
                                              objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#ATOS.opmerkingenAtos12',
                                              definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 12)',
                                              owner=self)

        self._opmerkingenAtos13 = EMAttribuut(field=StringField,
                                              naam='Opmerkingen (ATOS 13)',
                                              label='Opmerkingen (ATOS 13)',
                                              objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#ATOS.opmerkingenAtos13',
                                              definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 13)',
                                              owner=self)

        self._opmerkingenAtos15 = EMAttribuut(field=StringField,
                                              naam='Opmerkingen (ATOS 15)',
                                              label='Opmerkingen (ATOS 15)',
                                              objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#ATOS.opmerkingenAtos15',
                                              definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 15)',
                                              owner=self)

        self._opmerkingenAtos16 = EMAttribuut(field=StringField,
                                              naam='Opmerkingen (ATOS 16)',
                                              label='Opmerkingen (ATOS 16)',
                                              objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#ATOS.opmerkingenAtos16',
                                              definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 16)',
                                              owner=self)

        self._opmerkingenAtos17 = EMAttribuut(field=StringField,
                                              naam='Opmerkingen (ATOS 17)',
                                              label='Opmerkingen (ATOS 17)',
                                              objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#ATOS.opmerkingenAtos17',
                                              definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 17)',
                                              owner=self)

        self._opmerkingenAtos18 = EMAttribuut(field=StringField,
                                              naam='Opmerkingen (ATOS 18)',
                                              label='Opmerkingen (ATOS 18)',
                                              objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#ATOS.opmerkingenAtos18',
                                              definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 18)',
                                              owner=self)

        self._opmerkingenAtos19 = EMAttribuut(field=StringField,
                                              naam='Opmerkingen (ATOS 19)',
                                              label='Opmerkingen (ATOS 19)',
                                              objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#ATOS.opmerkingenAtos19',
                                              definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 19)',
                                              owner=self)

        self._opmerkingenAtos2 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (ATOS 2)',
                                             label='Opmerkingen (ATOS 2)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#ATOS.opmerkingenAtos2',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 2)',
                                             owner=self)

        self._opmerkingenAtos20 = EMAttribuut(field=StringField,
                                              naam='Opmerkingen (ATOS 20)',
                                              label='Opmerkingen (ATOS 20)',
                                              objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#ATOS.opmerkingenAtos20',
                                              definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 20)',
                                              owner=self)

        self._opmerkingenAtos21 = EMAttribuut(field=StringField,
                                              naam='Opmerkingen (ATOS 21)',
                                              label='Opmerkingen (ATOS 21)',
                                              objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#ATOS.opmerkingenAtos21',
                                              definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 21)',
                                              owner=self)

        self._opmerkingenAtos3 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (ATOS 3)',
                                             label='Opmerkingen (ATOS 3)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#ATOS.opmerkingenAtos3',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 3)',
                                             owner=self)

        self._opmerkingenAtos4 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (ATOS 4)',
                                             label='Opmerkingen (ATOS 4)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#ATOS.opmerkingenAtos4',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 4)',
                                             owner=self)

        self._opmerkingenAtos5 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (ATOS 5)',
                                             label='Opmerkingen (ATOS 5)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#ATOS.opmerkingenAtos5',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 5)',
                                             owner=self)

        self._opmerkingenAtos6 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (ATOS 6)',
                                             label='Opmerkingen (ATOS 6)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#ATOS.opmerkingenAtos6',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 6)',
                                             owner=self)

        self._opmerkingenAtos7 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (ATOS 7)',
                                             label='Opmerkingen (ATOS 7)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#ATOS.opmerkingenAtos7',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 7)',
                                             owner=self)

        self._opmerkingenAtos8 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (ATOS 8)',
                                             label='Opmerkingen (ATOS 8)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#ATOS.opmerkingenAtos8',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 8)',
                                             owner=self)

        self._opmerkingenAtos9 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (ATOS 9)',
                                             label='Opmerkingen (ATOS 9)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#ATOS.opmerkingenAtos9',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 9)',
                                             owner=self)

        self._opmerkingenAtos = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (ATOS)',
                                            label='Opmerkingen (ATOS)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#ATOS.opmerkingenAtos',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS)',
                                            owner=self)

        self._opmerkingenInspectie = EMAttribuut(field=StringField,
                                                 naam='Opmerkingen inspectie',
                                                 label='Opmerkingen inspectie',
                                                 objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.opmerkingenInspectie',
                                                 definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen inspectie',
                                                 owner=self)

        self._startAtos1 = EMAttribuut(field=DateTimeField,
                                       naam='Start (ATOS 1)',
                                       label='Start (ATOS 1)',
                                       objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#ATOS.startAtos1',
                                       definitie='Definitie nog toe te voegen voor eigenschap Start (ATOS 1)',
                                       owner=self)

        self._startAtos = EMAttribuut(field=DateTimeField,
                                      naam='Start (ATOS)',
                                      label='Start (ATOS)',
                                      objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#ATOS.startAtos',
                                      definitie='Definitie nog toe te voegen voor eigenschap Start (ATOS)',
                                      owner=self)

        self._upsOk = EMAttribuut(field=StringField,
                                  naam='UPS OK',
                                  label='UPS OK',
                                  objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.upsOk',
                                  definitie='Definitie nog toe te voegen voor eigenschap UPS OK',
                                  owner=self)

        self._upsOkOud = EMAttribuut(field=StringField,
                                     naam='UPS OK oud',
                                     label='UPS OK oud',
                                     objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.upsOkOud',
                                     definitie='Definitie nog toe te voegen voor eigenschap UPS OK oud',
                                     owner=self)

        self._ventilatieLocatieOk = EMAttribuut(field=BooleanField,
                                                naam='Ventilatie locatie OK',
                                                label='Ventilatie locatie OK',
                                                objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.ventilatieLocatieOk',
                                                definitie='Definitie nog toe te voegen voor eigenschap Ventilatie locatie OK',
                                                owner=self)

        self._verlichtingLocatieOk = EMAttribuut(field=BooleanField,
                                                 naam='Verlichting locatie OK',
                                                 label='Verlichting locatie OK',
                                                 objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.verlichtingLocatieOk',
                                                 definitie='Definitie nog toe te voegen voor eigenschap Verlichting locatie OK',
                                                 owner=self)

        self._voedingskabelsOk = EMAttribuut(field=BooleanField,
                                             naam='Voedingskabels OK',
                                             label='Voedingskabels OK',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.voedingskabelsOk',
                                             definitie='Definitie nog toe te voegen voor eigenschap Voedingskabels OK',
                                             owner=self)

        self._voedingsstekkersOk = EMAttribuut(field=BooleanField,
                                               naam='Voedingsstekkers OK',
                                               label='Voedingsstekkers OK',
                                               objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.voedingsstekkersOk',
                                               definitie='Definitie nog toe te voegen voor eigenschap Voedingsstekkers OK',
                                               owner=self)

        self._einde = EMAttribuut(field=DateTimeField,
                                  naam='einde',
                                  label='einde',
                                  objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.einde',
                                  definitie='Definitie nog toe te voegen voor eigenschap einde',
                                  owner=self)

        self._labelContactInfoApparatuurOk = EMAttribuut(field=BooleanField,
                                                         naam='label contact info apparatuur OK',
                                                         label='label contact info apparatuur OK',
                                                         objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.labelContactInfoApparatuurOk',
                                                         definitie='Definitie nog toe te voegen voor eigenschap label contact info apparatuur OK',
                                                         owner=self)

        self._labelInstallatieNrApparatuurOk = EMAttribuut(field=BooleanField,
                                                           naam='label installatie nr apparatuur OK',
                                                           label='label installatie nr apparatuur OK',
                                                           objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.labelInstallatieNrApparatuurOk',
                                                           definitie='Definitie nog toe te voegen voor eigenschap label installatie nr apparatuur OK',
                                                           owner=self)

        self._opmerkingenAtos14 = EMAttribuut(field=StringField,
                                              naam='opmerkingen (ATOS 14)',
                                              label='opmerkingen (ATOS 14)',
                                              objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#ATOS.opmerkingenAtos14',
                                              definitie='Definitie nog toe te voegen voor eigenschap opmerkingen (ATOS 14)',
                                              owner=self)

        self._start = EMAttribuut(field=DateTimeField,
                                  naam='start',
                                  label='start',
                                  objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.start',
                                  definitie='Definitie nog toe te voegen voor eigenschap start',
                                  owner=self)

    @property
    def DubbeleVoedingOk(self):
        """Definitie nog toe te voegen voor eigenschap (Dubbele) voeding OK"""
        return self._DubbeleVoedingOk.waarde

    @DubbeleVoedingOk.setter
    def DubbeleVoedingOk(self, value):
        self._DubbeleVoedingOk.set_waarde(value, owner=self)

    @property
    def abbameldaInstallatieOk(self):
        """Definitie nog toe te voegen voor eigenschap ABBAMelda installatie OK"""
        return self._abbameldaInstallatieOk.waarde

    @abbameldaInstallatieOk.setter
    def abbameldaInstallatieOk(self, value):
        self._abbameldaInstallatieOk.set_waarde(value, owner=self)

    @property
    def abbameldaOperoepGemaakt(self):
        """Definitie nog toe te voegen voor eigenschap ABBAMelda operoep gemaakt"""
        return self._abbameldaOperoepGemaakt.waarde

    @abbameldaOperoepGemaakt.setter
    def abbameldaOperoepGemaakt(self, value):
        self._abbameldaOperoepGemaakt.set_waarde(value, owner=self)

    @property
    def aanpassingenNodig(self):
        """Definitie nog toe te voegen voor eigenschap Aanpassingen nodig"""
        return self._aanpassingenNodig.waarde

    @aanpassingenNodig.setter
    def aanpassingenNodig(self, value):
        self._aanpassingenNodig.set_waarde(value, owner=self)

    @property
    def algemeneToestandLocatieOk(self):
        """Definitie nog toe te voegen voor eigenschap Algemene toestand locatie OK"""
        return self._algemeneToestandLocatieOk.waarde

    @algemeneToestandLocatieOk.setter
    def algemeneToestandLocatieOk(self, value):
        self._algemeneToestandLocatieOk.set_waarde(value, owner=self)

    @property
    def apparatuurFiltersVervangen(self):
        """Definitie nog toe te voegen voor eigenschap Apparatuur filters vervangen"""
        return self._apparatuurFiltersVervangen.waarde

    @apparatuurFiltersVervangen.setter
    def apparatuurFiltersVervangen(self, value):
        self._apparatuurFiltersVervangen.set_waarde(value, owner=self)

    @property
    def apparatuurGereinigd(self):
        """Definitie nog toe te voegen voor eigenschap Apparatuur gereinigd"""
        return self._apparatuurGereinigd.waarde

    @apparatuurGereinigd.setter
    def apparatuurGereinigd(self, value):
        self._apparatuurGereinigd.set_waarde(value, owner=self)

    @property
    def apparatuurVentilatieOk(self):
        """Definitie nog toe te voegen voor eigenschap Apparatuur ventilatie OK"""
        return self._apparatuurVentilatieOk.waarde

    @apparatuurVentilatieOk.setter
    def apparatuurVentilatieOk(self, value):
        self._apparatuurVentilatieOk.set_waarde(value, owner=self)

    @property
    def apparatuurVrijVanAlarmen(self):
        """Definitie nog toe te voegen voor eigenschap Apparatuur vrij van alarmen"""
        return self._apparatuurVrijVanAlarmen.waarde

    @apparatuurVrijVanAlarmen.setter
    def apparatuurVrijVanAlarmen(self, value):
        self._apparatuurVrijVanAlarmen.set_waarde(value, owner=self)

    @property
    def batterijVervangen(self):
        """Definitie nog toe te voegen voor eigenschap Batterij vervangen"""
        return self._batterijVervangen.waarde

    @batterijVervangen.setter
    def batterijVervangen(self, value):
        self._batterijVervangen.set_waarde(value, owner=self)

    @property
    def batterijVervangenOp(self):
        """Definitie nog toe te voegen voor eigenschap Batterij vervangen op"""
        return self._batterijVervangenOp.waarde

    @batterijVervangenOp.setter
    def batterijVervangenOp(self, value):
        self._batterijVervangenOp.set_waarde(value, owner=self)

    @property
    def beschrijvingInterventie(self):
        """Definitie nog toe te voegen voor eigenschap Beschrijving interventie"""
        return self._beschrijvingInterventie.waarde

    @beschrijvingInterventie.setter
    def beschrijvingInterventie(self, value):
        self._beschrijvingInterventie.set_waarde(value, owner=self)

    @property
    def eindeAtos1(self):
        """Definitie nog toe te voegen voor eigenschap Einde (ATOS 1)"""
        return self._eindeAtos1.waarde

    @eindeAtos1.setter
    def eindeAtos1(self, value):
        self._eindeAtos1.set_waarde(value, owner=self)

    @property
    def eindeAtos(self):
        """Definitie nog toe te voegen voor eigenschap Einde (ATOS)"""
        return self._eindeAtos.waarde

    @eindeAtos.setter
    def eindeAtos(self, value):
        self._eindeAtos.set_waarde(value, owner=self)

    @property
    def elektrischPlanInstallatieOk(self):
        """Definitie nog toe te voegen voor eigenschap Elektrisch plan / installatie OK"""
        return self._elektrischPlanInstallatieOk.waarde

    @elektrischPlanInstallatieOk.setter
    def elektrischPlanInstallatieOk(self, value):
        self._elektrischPlanInstallatieOk.set_waarde(value, owner=self)

    @property
    def elektrischPlanInstallatieOkOud(self):
        """Definitie nog toe te voegen voor eigenschap Elektrisch plan/installatie OK oud"""
        return self._elektrischPlanInstallatieOkOud.waarde

    @elektrischPlanInstallatieOkOud.setter
    def elektrischPlanInstallatieOkOud(self, value):
        self._elektrischPlanInstallatieOkOud.set_waarde(value, owner=self)

    @property
    def fotoSApparatuurGemaakt(self):
        """Definitie nog toe te voegen voor eigenschap Foto\'s apparatuur gemaakt"""
        return self._fotoSApparatuurGemaakt.waarde

    @fotoSApparatuurGemaakt.setter
    def fotoSApparatuurGemaakt(self, value):
        self._fotoSApparatuurGemaakt.set_waarde(value, owner=self)

    @property
    def glasvezelOkBevestigingLabels(self):
        """Definitie nog toe te voegen voor eigenschap Glasvezel OK (bevestiging, labels)"""
        return self._glasvezelOkBevestigingLabels.waarde

    @glasvezelOkBevestigingLabels.setter
    def glasvezelOkBevestigingLabels(self, value):
        self._glasvezelOkBevestigingLabels.set_waarde(value, owner=self)

    @property
    def glasvezelOkSelectielijst(self):
        """Definitie nog toe te voegen voor eigenschap Glasvezel OK selectielijst"""
        return self._glasvezelOkSelectielijst.waarde

    @glasvezelOkSelectielijst.setter
    def glasvezelOkSelectielijst(self, value):
        self._glasvezelOkSelectielijst.set_waarde(value, owner=self)

    @property
    def glasvezelConnectorsOk(self):
        """Definitie nog toe te voegen voor eigenschap Glasvezel connectors OK"""
        return self._glasvezelConnectorsOk.waarde

    @glasvezelConnectorsOk.setter
    def glasvezelConnectorsOk(self, value):
        self._glasvezelConnectorsOk.set_waarde(value, owner=self)

    @property
    def glasvezelConnectorsSelectielijst(self):
        """Definitie nog toe te voegen voor eigenschap Glasvezel connectors selectielijst"""
        return self._glasvezelConnectorsSelectielijst.waarde

    @glasvezelConnectorsSelectielijst.setter
    def glasvezelConnectorsSelectielijst(self, value):
        self._glasvezelConnectorsSelectielijst.set_waarde(value, owner=self)

    @property
    def klimatiseringLocatieOk(self):
        """Definitie nog toe te voegen voor eigenschap Klimatisering locatie OK"""
        return self._klimatiseringLocatieOk.waarde

    @klimatiseringLocatieOk.setter
    def klimatiseringLocatieOk(self, value):
        self._klimatiseringLocatieOk.set_waarde(value, owner=self)

    @property
    def koperkabelOkBevestigingLabels(self):
        """Definitie nog toe te voegen voor eigenschap Koperkabel OK (bevestiging,labels)"""
        return self._koperkabelOkBevestigingLabels.waarde

    @koperkabelOkBevestigingLabels.setter
    def koperkabelOkBevestigingLabels(self, value):
        self._koperkabelOkBevestigingLabels.set_waarde(value, owner=self)

    @property
    def koperkabelOkSelectielijst(self):
        """Definitie nog toe te voegen voor eigenschap Koperkabel OK selectielijst"""
        return self._koperkabelOkSelectielijst.waarde

    @koperkabelOkSelectielijst.setter
    def koperkabelOkSelectielijst(self, value):
        self._koperkabelOkSelectielijst.set_waarde(value, owner=self)

    @property
    def locatieBereikbaar(self):
        """Definitie nog toe te voegen voor eigenschap Locatie bereikbaar"""
        return self._locatieBereikbaar.waarde

    @locatieBereikbaar.setter
    def locatieBereikbaar(self, value):
        self._locatieBereikbaar.set_waarde(value, owner=self)

    @property
    def naarWie(self):
        """Definitie nog toe te voegen voor eigenschap Naar wie"""
        return self._naarWie.waarde

    @naarWie.setter
    def naarWie(self, value):
        self._naarWie.set_waarde(value, owner=self)

    @property
    def opmerkingenAtos1(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 1)"""
        return self._opmerkingenAtos1.waarde

    @opmerkingenAtos1.setter
    def opmerkingenAtos1(self, value):
        self._opmerkingenAtos1.set_waarde(value, owner=self)

    @property
    def opmerkingenAtos10(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 10)"""
        return self._opmerkingenAtos10.waarde

    @opmerkingenAtos10.setter
    def opmerkingenAtos10(self, value):
        self._opmerkingenAtos10.set_waarde(value, owner=self)

    @property
    def opmerkingenAtos11(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 11)"""
        return self._opmerkingenAtos11.waarde

    @opmerkingenAtos11.setter
    def opmerkingenAtos11(self, value):
        self._opmerkingenAtos11.set_waarde(value, owner=self)

    @property
    def opmerkingenAtos12(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 12)"""
        return self._opmerkingenAtos12.waarde

    @opmerkingenAtos12.setter
    def opmerkingenAtos12(self, value):
        self._opmerkingenAtos12.set_waarde(value, owner=self)

    @property
    def opmerkingenAtos13(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 13)"""
        return self._opmerkingenAtos13.waarde

    @opmerkingenAtos13.setter
    def opmerkingenAtos13(self, value):
        self._opmerkingenAtos13.set_waarde(value, owner=self)

    @property
    def opmerkingenAtos15(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 15)"""
        return self._opmerkingenAtos15.waarde

    @opmerkingenAtos15.setter
    def opmerkingenAtos15(self, value):
        self._opmerkingenAtos15.set_waarde(value, owner=self)

    @property
    def opmerkingenAtos16(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 16)"""
        return self._opmerkingenAtos16.waarde

    @opmerkingenAtos16.setter
    def opmerkingenAtos16(self, value):
        self._opmerkingenAtos16.set_waarde(value, owner=self)

    @property
    def opmerkingenAtos17(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 17)"""
        return self._opmerkingenAtos17.waarde

    @opmerkingenAtos17.setter
    def opmerkingenAtos17(self, value):
        self._opmerkingenAtos17.set_waarde(value, owner=self)

    @property
    def opmerkingenAtos18(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 18)"""
        return self._opmerkingenAtos18.waarde

    @opmerkingenAtos18.setter
    def opmerkingenAtos18(self, value):
        self._opmerkingenAtos18.set_waarde(value, owner=self)

    @property
    def opmerkingenAtos19(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 19)"""
        return self._opmerkingenAtos19.waarde

    @opmerkingenAtos19.setter
    def opmerkingenAtos19(self, value):
        self._opmerkingenAtos19.set_waarde(value, owner=self)

    @property
    def opmerkingenAtos2(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 2)"""
        return self._opmerkingenAtos2.waarde

    @opmerkingenAtos2.setter
    def opmerkingenAtos2(self, value):
        self._opmerkingenAtos2.set_waarde(value, owner=self)

    @property
    def opmerkingenAtos20(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 20)"""
        return self._opmerkingenAtos20.waarde

    @opmerkingenAtos20.setter
    def opmerkingenAtos20(self, value):
        self._opmerkingenAtos20.set_waarde(value, owner=self)

    @property
    def opmerkingenAtos21(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 21)"""
        return self._opmerkingenAtos21.waarde

    @opmerkingenAtos21.setter
    def opmerkingenAtos21(self, value):
        self._opmerkingenAtos21.set_waarde(value, owner=self)

    @property
    def opmerkingenAtos3(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 3)"""
        return self._opmerkingenAtos3.waarde

    @opmerkingenAtos3.setter
    def opmerkingenAtos3(self, value):
        self._opmerkingenAtos3.set_waarde(value, owner=self)

    @property
    def opmerkingenAtos4(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 4)"""
        return self._opmerkingenAtos4.waarde

    @opmerkingenAtos4.setter
    def opmerkingenAtos4(self, value):
        self._opmerkingenAtos4.set_waarde(value, owner=self)

    @property
    def opmerkingenAtos5(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 5)"""
        return self._opmerkingenAtos5.waarde

    @opmerkingenAtos5.setter
    def opmerkingenAtos5(self, value):
        self._opmerkingenAtos5.set_waarde(value, owner=self)

    @property
    def opmerkingenAtos6(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 6)"""
        return self._opmerkingenAtos6.waarde

    @opmerkingenAtos6.setter
    def opmerkingenAtos6(self, value):
        self._opmerkingenAtos6.set_waarde(value, owner=self)

    @property
    def opmerkingenAtos7(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 7)"""
        return self._opmerkingenAtos7.waarde

    @opmerkingenAtos7.setter
    def opmerkingenAtos7(self, value):
        self._opmerkingenAtos7.set_waarde(value, owner=self)

    @property
    def opmerkingenAtos8(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 8)"""
        return self._opmerkingenAtos8.waarde

    @opmerkingenAtos8.setter
    def opmerkingenAtos8(self, value):
        self._opmerkingenAtos8.set_waarde(value, owner=self)

    @property
    def opmerkingenAtos9(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS 9)"""
        return self._opmerkingenAtos9.waarde

    @opmerkingenAtos9.setter
    def opmerkingenAtos9(self, value):
        self._opmerkingenAtos9.set_waarde(value, owner=self)

    @property
    def opmerkingenAtos(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (ATOS)"""
        return self._opmerkingenAtos.waarde

    @opmerkingenAtos.setter
    def opmerkingenAtos(self, value):
        self._opmerkingenAtos.set_waarde(value, owner=self)

    @property
    def opmerkingenInspectie(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen inspectie"""
        return self._opmerkingenInspectie.waarde

    @opmerkingenInspectie.setter
    def opmerkingenInspectie(self, value):
        self._opmerkingenInspectie.set_waarde(value, owner=self)

    @property
    def startAtos1(self):
        """Definitie nog toe te voegen voor eigenschap Start (ATOS 1)"""
        return self._startAtos1.waarde

    @startAtos1.setter
    def startAtos1(self, value):
        self._startAtos1.set_waarde(value, owner=self)

    @property
    def startAtos(self):
        """Definitie nog toe te voegen voor eigenschap Start (ATOS)"""
        return self._startAtos.waarde

    @startAtos.setter
    def startAtos(self, value):
        self._startAtos.set_waarde(value, owner=self)

    @property
    def upsOk(self):
        """Definitie nog toe te voegen voor eigenschap UPS OK"""
        return self._upsOk.waarde

    @upsOk.setter
    def upsOk(self, value):
        self._upsOk.set_waarde(value, owner=self)

    @property
    def upsOkOud(self):
        """Definitie nog toe te voegen voor eigenschap UPS OK oud"""
        return self._upsOkOud.waarde

    @upsOkOud.setter
    def upsOkOud(self, value):
        self._upsOkOud.set_waarde(value, owner=self)

    @property
    def ventilatieLocatieOk(self):
        """Definitie nog toe te voegen voor eigenschap Ventilatie locatie OK"""
        return self._ventilatieLocatieOk.waarde

    @ventilatieLocatieOk.setter
    def ventilatieLocatieOk(self, value):
        self._ventilatieLocatieOk.set_waarde(value, owner=self)

    @property
    def verlichtingLocatieOk(self):
        """Definitie nog toe te voegen voor eigenschap Verlichting locatie OK"""
        return self._verlichtingLocatieOk.waarde

    @verlichtingLocatieOk.setter
    def verlichtingLocatieOk(self, value):
        self._verlichtingLocatieOk.set_waarde(value, owner=self)

    @property
    def voedingskabelsOk(self):
        """Definitie nog toe te voegen voor eigenschap Voedingskabels OK"""
        return self._voedingskabelsOk.waarde

    @voedingskabelsOk.setter
    def voedingskabelsOk(self, value):
        self._voedingskabelsOk.set_waarde(value, owner=self)

    @property
    def voedingsstekkersOk(self):
        """Definitie nog toe te voegen voor eigenschap Voedingsstekkers OK"""
        return self._voedingsstekkersOk.waarde

    @voedingsstekkersOk.setter
    def voedingsstekkersOk(self, value):
        self._voedingsstekkersOk.set_waarde(value, owner=self)

    @property
    def einde(self):
        """Definitie nog toe te voegen voor eigenschap einde"""
        return self._einde.waarde

    @einde.setter
    def einde(self, value):
        self._einde.set_waarde(value, owner=self)

    @property
    def labelContactInfoApparatuurOk(self):
        """Definitie nog toe te voegen voor eigenschap label contact info apparatuur OK"""
        return self._labelContactInfoApparatuurOk.waarde

    @labelContactInfoApparatuurOk.setter
    def labelContactInfoApparatuurOk(self, value):
        self._labelContactInfoApparatuurOk.set_waarde(value, owner=self)

    @property
    def labelInstallatieNrApparatuurOk(self):
        """Definitie nog toe te voegen voor eigenschap label installatie nr apparatuur OK"""
        return self._labelInstallatieNrApparatuurOk.waarde

    @labelInstallatieNrApparatuurOk.setter
    def labelInstallatieNrApparatuurOk(self, value):
        self._labelInstallatieNrApparatuurOk.set_waarde(value, owner=self)

    @property
    def opmerkingenAtos14(self):
        """Definitie nog toe te voegen voor eigenschap opmerkingen (ATOS 14)"""
        return self._opmerkingenAtos14.waarde

    @opmerkingenAtos14.setter
    def opmerkingenAtos14(self, value):
        self._opmerkingenAtos14.set_waarde(value, owner=self)

    @property
    def start(self):
        """Definitie nog toe te voegen voor eigenschap start"""
        return self._start.waarde

    @start.setter
    def start(self, value):
        self._start.set_waarde(value, owner=self)

