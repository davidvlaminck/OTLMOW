# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from OTLMOW.OTLModel.Datatypes.DateTimeField import DateTimeField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class WDM(EMObject):
    """Wave Division Multiplexing"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#WDM'
    label = 'Wave division multiplexing'

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

        self._eindeWdm1 = EMAttribuut(field=DateTimeField,
                                      naam='Einde (WDM 1)',
                                      label='Einde (WDM 1)',
                                      objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#WDM.eindeWdm1',
                                      definitie='Definitie nog toe te voegen voor eigenschap Einde (WDM 1)',
                                      owner=self)

        self._eindeWdm = EMAttribuut(field=DateTimeField,
                                     naam='Einde (WDM)',
                                     label='Einde (WDM)',
                                     objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#WDM.eindeWdm',
                                     definitie='Definitie nog toe te voegen voor eigenschap Einde (WDM)',
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

        self._glasvezelConnectorsOkOud = EMAttribuut(field=StringField,
                                                     naam='Glasvezel connectors OK oud',
                                                     label='Glasvezel connectors OK oud',
                                                     objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.glasvezelConnectorsOkOud',
                                                     definitie='Definitie nog toe te voegen voor eigenschap Glasvezel connectors OK oud',
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

        self._nazichtUps = EMAttribuut(field=StringField,
                                       naam='Nazicht UPS',
                                       label='Nazicht UPS',
                                       objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.nazichtUps',
                                       definitie='Definitie nog toe te voegen voor eigenschap Nazicht UPS',
                                       owner=self)

        self._opmerkingenWdm1 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (WDM 1)',
                                            label='Opmerkingen (WDM 1)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#WDM.opmerkingenWdm1',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 1)',
                                            owner=self)

        self._opmerkingenWdm10 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (WDM 10)',
                                             label='Opmerkingen (WDM 10)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#WDM.opmerkingenWdm10',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 10)',
                                             owner=self)

        self._opmerkingenWdm11 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (WDM 11)',
                                             label='Opmerkingen (WDM 11)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#WDM.opmerkingenWdm11',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 11)',
                                             owner=self)

        self._opmerkingenWdm12 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (WDM 12)',
                                             label='Opmerkingen (WDM 12)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#WDM.opmerkingenWdm12',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 12)',
                                             owner=self)

        self._opmerkingenWdm13 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (WDM 13)',
                                             label='Opmerkingen (WDM 13)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#WDM.opmerkingenWdm13',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 13)',
                                             owner=self)

        self._opmerkingenWdm15 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (WDM 15)',
                                             label='Opmerkingen (WDM 15)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#WDM.opmerkingenWdm15',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 15)',
                                             owner=self)

        self._opmerkingenWdm16 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (WDM 16)',
                                             label='Opmerkingen (WDM 16)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#WDM.opmerkingenWdm16',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 16)',
                                             owner=self)

        self._opmerkingenWdm17 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (WDM 17)',
                                             label='Opmerkingen (WDM 17)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#WDM.opmerkingenWdm17',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 17)',
                                             owner=self)

        self._opmerkingenWdm18 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (WDM 18)',
                                             label='Opmerkingen (WDM 18)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#WDM.opmerkingenWdm18',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 18)',
                                             owner=self)

        self._opmerkingenWdm19 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (WDM 19)',
                                             label='Opmerkingen (WDM 19)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#WDM.opmerkingenWdm19',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 19)',
                                             owner=self)

        self._opmerkingenWdm2 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (WDM 2)',
                                            label='Opmerkingen (WDM 2)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#WDM.opmerkingenWdm2',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 2)',
                                            owner=self)

        self._opmerkingenWdm20 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (WDM 20)',
                                             label='Opmerkingen (WDM 20)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#WDM.opmerkingenWdm20',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 20)',
                                             owner=self)

        self._opmerkingenWdm21 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (WDM 21)',
                                             label='Opmerkingen (WDM 21)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#WDM.opmerkingenWdm21',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 21)',
                                             owner=self)

        self._opmerkingenWdm3 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (WDM 3)',
                                            label='Opmerkingen (WDM 3)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#WDM.opmerkingenWdm3',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 3)',
                                            owner=self)

        self._opmerkingenWdm4 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (WDM 4)',
                                            label='Opmerkingen (WDM 4)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#WDM.opmerkingenWdm4',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 4)',
                                            owner=self)

        self._opmerkingenWdm5 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (WDM 5)',
                                            label='Opmerkingen (WDM 5)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#WDM.opmerkingenWdm5',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 5)',
                                            owner=self)

        self._opmerkingenWdm6 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (WDM 6)',
                                            label='Opmerkingen (WDM 6)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#WDM.opmerkingenWdm6',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 6)',
                                            owner=self)

        self._opmerkingenWdm7 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (WDM 7)',
                                            label='Opmerkingen (WDM 7)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#WDM.opmerkingenWdm7',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 7)',
                                            owner=self)

        self._opmerkingenWdm8 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (WDM 8)',
                                            label='Opmerkingen (WDM 8)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#WDM.opmerkingenWdm8',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 8)',
                                            owner=self)

        self._opmerkingenWdm9 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (WDM 9)',
                                            label='Opmerkingen (WDM 9)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#WDM.opmerkingenWdm9',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 9)',
                                            owner=self)

        self._opmerkingenWdm = EMAttribuut(field=StringField,
                                           naam='Opmerkingen (WDM)',
                                           label='Opmerkingen (WDM)',
                                           objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#WDM.opmerkingenWdm',
                                           definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM)',
                                           owner=self)

        self._opmerkingenInspectie = EMAttribuut(field=StringField,
                                                 naam='Opmerkingen inspectie',
                                                 label='Opmerkingen inspectie',
                                                 objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.opmerkingenInspectie',
                                                 definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen inspectie',
                                                 owner=self)

        self._startWdm1 = EMAttribuut(field=DateTimeField,
                                      naam='Start (WDM 1)',
                                      label='Start (WDM 1)',
                                      objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#WDM.startWdm1',
                                      definitie='Definitie nog toe te voegen voor eigenschap Start (WDM 1)',
                                      owner=self)

        self._startWdm = EMAttribuut(field=DateTimeField,
                                     naam='Start (WDM)',
                                     label='Start (WDM)',
                                     objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#WDM.startWdm',
                                     definitie='Definitie nog toe te voegen voor eigenschap Start (WDM)',
                                     owner=self)

        self._upsOk = EMAttribuut(field=StringField,
                                  naam='UPS OK',
                                  label='UPS OK',
                                  objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.upsOk',
                                  definitie='Definitie nog toe te voegen voor eigenschap UPS OK',
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

        self._opmerkingenWdm14 = EMAttribuut(field=StringField,
                                             naam='opmerkingen (WDM 14)',
                                             label='opmerkingen (WDM 14)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#WDM.opmerkingenWdm14',
                                             definitie='Definitie nog toe te voegen voor eigenschap opmerkingen (WDM 14)',
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
    def eindeWdm1(self):
        """Definitie nog toe te voegen voor eigenschap Einde (WDM 1)"""
        return self._eindeWdm1.waarde

    @eindeWdm1.setter
    def eindeWdm1(self, value):
        self._eindeWdm1.set_waarde(value, owner=self)

    @property
    def eindeWdm(self):
        """Definitie nog toe te voegen voor eigenschap Einde (WDM)"""
        return self._eindeWdm.waarde

    @eindeWdm.setter
    def eindeWdm(self, value):
        self._eindeWdm.set_waarde(value, owner=self)

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
    def glasvezelConnectorsOkOud(self):
        """Definitie nog toe te voegen voor eigenschap Glasvezel connectors OK oud"""
        return self._glasvezelConnectorsOkOud.waarde

    @glasvezelConnectorsOkOud.setter
    def glasvezelConnectorsOkOud(self, value):
        self._glasvezelConnectorsOkOud.set_waarde(value, owner=self)

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
    def nazichtUps(self):
        """Definitie nog toe te voegen voor eigenschap Nazicht UPS"""
        return self._nazichtUps.waarde

    @nazichtUps.setter
    def nazichtUps(self, value):
        self._nazichtUps.set_waarde(value, owner=self)

    @property
    def opmerkingenWdm1(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 1)"""
        return self._opmerkingenWdm1.waarde

    @opmerkingenWdm1.setter
    def opmerkingenWdm1(self, value):
        self._opmerkingenWdm1.set_waarde(value, owner=self)

    @property
    def opmerkingenWdm10(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 10)"""
        return self._opmerkingenWdm10.waarde

    @opmerkingenWdm10.setter
    def opmerkingenWdm10(self, value):
        self._opmerkingenWdm10.set_waarde(value, owner=self)

    @property
    def opmerkingenWdm11(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 11)"""
        return self._opmerkingenWdm11.waarde

    @opmerkingenWdm11.setter
    def opmerkingenWdm11(self, value):
        self._opmerkingenWdm11.set_waarde(value, owner=self)

    @property
    def opmerkingenWdm12(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 12)"""
        return self._opmerkingenWdm12.waarde

    @opmerkingenWdm12.setter
    def opmerkingenWdm12(self, value):
        self._opmerkingenWdm12.set_waarde(value, owner=self)

    @property
    def opmerkingenWdm13(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 13)"""
        return self._opmerkingenWdm13.waarde

    @opmerkingenWdm13.setter
    def opmerkingenWdm13(self, value):
        self._opmerkingenWdm13.set_waarde(value, owner=self)

    @property
    def opmerkingenWdm15(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 15)"""
        return self._opmerkingenWdm15.waarde

    @opmerkingenWdm15.setter
    def opmerkingenWdm15(self, value):
        self._opmerkingenWdm15.set_waarde(value, owner=self)

    @property
    def opmerkingenWdm16(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 16)"""
        return self._opmerkingenWdm16.waarde

    @opmerkingenWdm16.setter
    def opmerkingenWdm16(self, value):
        self._opmerkingenWdm16.set_waarde(value, owner=self)

    @property
    def opmerkingenWdm17(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 17)"""
        return self._opmerkingenWdm17.waarde

    @opmerkingenWdm17.setter
    def opmerkingenWdm17(self, value):
        self._opmerkingenWdm17.set_waarde(value, owner=self)

    @property
    def opmerkingenWdm18(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 18)"""
        return self._opmerkingenWdm18.waarde

    @opmerkingenWdm18.setter
    def opmerkingenWdm18(self, value):
        self._opmerkingenWdm18.set_waarde(value, owner=self)

    @property
    def opmerkingenWdm19(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 19)"""
        return self._opmerkingenWdm19.waarde

    @opmerkingenWdm19.setter
    def opmerkingenWdm19(self, value):
        self._opmerkingenWdm19.set_waarde(value, owner=self)

    @property
    def opmerkingenWdm2(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 2)"""
        return self._opmerkingenWdm2.waarde

    @opmerkingenWdm2.setter
    def opmerkingenWdm2(self, value):
        self._opmerkingenWdm2.set_waarde(value, owner=self)

    @property
    def opmerkingenWdm20(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 20)"""
        return self._opmerkingenWdm20.waarde

    @opmerkingenWdm20.setter
    def opmerkingenWdm20(self, value):
        self._opmerkingenWdm20.set_waarde(value, owner=self)

    @property
    def opmerkingenWdm21(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 21)"""
        return self._opmerkingenWdm21.waarde

    @opmerkingenWdm21.setter
    def opmerkingenWdm21(self, value):
        self._opmerkingenWdm21.set_waarde(value, owner=self)

    @property
    def opmerkingenWdm3(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 3)"""
        return self._opmerkingenWdm3.waarde

    @opmerkingenWdm3.setter
    def opmerkingenWdm3(self, value):
        self._opmerkingenWdm3.set_waarde(value, owner=self)

    @property
    def opmerkingenWdm4(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 4)"""
        return self._opmerkingenWdm4.waarde

    @opmerkingenWdm4.setter
    def opmerkingenWdm4(self, value):
        self._opmerkingenWdm4.set_waarde(value, owner=self)

    @property
    def opmerkingenWdm5(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 5)"""
        return self._opmerkingenWdm5.waarde

    @opmerkingenWdm5.setter
    def opmerkingenWdm5(self, value):
        self._opmerkingenWdm5.set_waarde(value, owner=self)

    @property
    def opmerkingenWdm6(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 6)"""
        return self._opmerkingenWdm6.waarde

    @opmerkingenWdm6.setter
    def opmerkingenWdm6(self, value):
        self._opmerkingenWdm6.set_waarde(value, owner=self)

    @property
    def opmerkingenWdm7(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 7)"""
        return self._opmerkingenWdm7.waarde

    @opmerkingenWdm7.setter
    def opmerkingenWdm7(self, value):
        self._opmerkingenWdm7.set_waarde(value, owner=self)

    @property
    def opmerkingenWdm8(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 8)"""
        return self._opmerkingenWdm8.waarde

    @opmerkingenWdm8.setter
    def opmerkingenWdm8(self, value):
        self._opmerkingenWdm8.set_waarde(value, owner=self)

    @property
    def opmerkingenWdm9(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM 9)"""
        return self._opmerkingenWdm9.waarde

    @opmerkingenWdm9.setter
    def opmerkingenWdm9(self, value):
        self._opmerkingenWdm9.set_waarde(value, owner=self)

    @property
    def opmerkingenWdm(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (WDM)"""
        return self._opmerkingenWdm.waarde

    @opmerkingenWdm.setter
    def opmerkingenWdm(self, value):
        self._opmerkingenWdm.set_waarde(value, owner=self)

    @property
    def opmerkingenInspectie(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen inspectie"""
        return self._opmerkingenInspectie.waarde

    @opmerkingenInspectie.setter
    def opmerkingenInspectie(self, value):
        self._opmerkingenInspectie.set_waarde(value, owner=self)

    @property
    def startWdm1(self):
        """Definitie nog toe te voegen voor eigenschap Start (WDM 1)"""
        return self._startWdm1.waarde

    @startWdm1.setter
    def startWdm1(self, value):
        self._startWdm1.set_waarde(value, owner=self)

    @property
    def startWdm(self):
        """Definitie nog toe te voegen voor eigenschap Start (WDM)"""
        return self._startWdm.waarde

    @startWdm.setter
    def startWdm(self, value):
        self._startWdm.set_waarde(value, owner=self)

    @property
    def upsOk(self):
        """Definitie nog toe te voegen voor eigenschap UPS OK"""
        return self._upsOk.waarde

    @upsOk.setter
    def upsOk(self, value):
        self._upsOk.set_waarde(value, owner=self)

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
    def opmerkingenWdm14(self):
        """Definitie nog toe te voegen voor eigenschap opmerkingen (WDM 14)"""
        return self._opmerkingenWdm14.waarde

    @opmerkingenWdm14.setter
    def opmerkingenWdm14(self, value):
        self._opmerkingenWdm14.set_waarde(value, owner=self)

    @property
    def start(self):
        """Definitie nog toe te voegen voor eigenschap start"""
        return self._start.waarde

    @start.setter
    def start(self, value):
        self._start.set_waarde(value, owner=self)

