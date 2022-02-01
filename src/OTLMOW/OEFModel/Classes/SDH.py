# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from OTLMOW.OTLModel.Datatypes.DateTimeField import DateTimeField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class SDH(EMObject):
    """SDH-knoop"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#SDH'
    label = 'SDH-knoop'

    def __init__(self):
        super().__init__()

        self._DubbeleVoedingOk = EMAttribuut(field=StringField,
                                             naam='(Dubbele) voeding OK',
                                             label='(Dubbele) voeding OK',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.DubbeleVoedingOk',
                                             definitie='Definitie nog toe te voegen voor eigenschap (Dubbele) voeding OK')

        self._1WaaromNiet = EMAttribuut(field=StringField,
                                        naam='1. Waarom niet?',
                                        label='1. Waarom niet?',
                                        objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.1WaaromNiet',
                                        definitie='Definitie nog toe te voegen voor eigenschap Waarom niet?')

        self._101SiteVerantwoordelijkeGeNformeerd = EMAttribuut(field=BooleanField,
                                                                naam='101. Site verantwoordelijke geÃ¯nformeerd',
                                                                label='101. Site verantwoordelijke geÃ¯nformeerd',
                                                                objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.101SiteVerantwoordelijkeGeNformeerd',
                                                                definitie='Definitie nog toe te voegen voor eigenschap Site verantwoordelijke geÃ¯nformeerd')

        self._215Actie = EMAttribuut(field=StringField,
                                     naam='215. Actie',
                                     label='215. Actie',
                                     objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.215Actie',
                                     definitie='Definitie nog toe te voegen voor eigenschap Actie')

        self._601SiteVerantwoordelijkeGeNformeerd = EMAttribuut(field=BooleanField,
                                                                naam='601. Site verantwoordelijke geÃ¯nformeerd',
                                                                label='601. Site verantwoordelijke geÃ¯nformeerd',
                                                                objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.601SiteVerantwoordelijkeGeNformeerd',
                                                                definitie='Definitie nog toe te voegen voor eigenschap Site verantwoordelijke geÃ¯nformeerd')

        self._abbameldaInstallatieOk = EMAttribuut(field=BooleanField,
                                                   naam='ABBAMelda installatie OK',
                                                   label='ABBAMelda installatie OK',
                                                   objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.abbameldaInstallatieOk',
                                                   definitie='Definitie nog toe te voegen voor eigenschap ABBAMelda installatie OK')

        self._abbameldaOperoepGemaakt = EMAttribuut(field=BooleanField,
                                                    naam='ABBAMelda operoep gemaakt',
                                                    label='ABBAMelda operoep gemaakt',
                                                    objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.abbameldaOperoepGemaakt',
                                                    definitie='Definitie nog toe te voegen voor eigenschap ABBAMelda operoep gemaakt')

        self._aanpassingenNodig = EMAttribuut(field=StringField,
                                              naam='Aanpassingen nodig',
                                              label='Aanpassingen nodig',
                                              objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.aanpassingenNodig',
                                              definitie='Definitie nog toe te voegen voor eigenschap Aanpassingen nodig')

        self._algemeneToestandLocatieOk = EMAttribuut(field=BooleanField,
                                                      naam='Algemene toestand locatie OK',
                                                      label='Algemene toestand locatie OK',
                                                      objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.algemeneToestandLocatieOk',
                                                      definitie='Definitie nog toe te voegen voor eigenschap Algemene toestand locatie OK')

        self._apparatuurFiltersVervangen = EMAttribuut(field=BooleanField,
                                                       naam='Apparatuur filters vervangen',
                                                       label='Apparatuur filters vervangen',
                                                       objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.apparatuurFiltersVervangen',
                                                       definitie='Definitie nog toe te voegen voor eigenschap Apparatuur filters vervangen')

        self._apparatuurGereinigd = EMAttribuut(field=BooleanField,
                                                naam='Apparatuur gereinigd',
                                                label='Apparatuur gereinigd',
                                                objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.apparatuurGereinigd',
                                                definitie='Definitie nog toe te voegen voor eigenschap Apparatuur gereinigd')

        self._apparatuurVentilatieOk = EMAttribuut(field=BooleanField,
                                                   naam='Apparatuur ventilatie OK',
                                                   label='Apparatuur ventilatie OK',
                                                   objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.apparatuurVentilatieOk',
                                                   definitie='Definitie nog toe te voegen voor eigenschap Apparatuur ventilatie OK')

        self._apparatuurVrijVanAlarmen = EMAttribuut(field=BooleanField,
                                                     naam='Apparatuur vrij van alarmen',
                                                     label='Apparatuur vrij van alarmen',
                                                     objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.apparatuurVrijVanAlarmen',
                                                     definitie='Definitie nog toe te voegen voor eigenschap Apparatuur vrij van alarmen')

        self._batterijVervangen = EMAttribuut(field=BooleanField,
                                              naam='Batterij vervangen',
                                              label='Batterij vervangen',
                                              objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.batterijVervangen',
                                              definitie='Definitie nog toe te voegen voor eigenschap Batterij vervangen')

        self._batterijVervangenOp = EMAttribuut(field=DateField,
                                                naam='Batterij vervangen op',
                                                label='Batterij vervangen op',
                                                objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.batterijVervangenOp',
                                                definitie='Definitie nog toe te voegen voor eigenschap Batterij vervangen op')

        self._beschrijvingInterventie = EMAttribuut(field=StringField,
                                                    naam='Beschrijving interventie',
                                                    label='Beschrijving interventie',
                                                    objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.beschrijvingInterventie',
                                                    definitie='Definitie nog toe te voegen voor eigenschap Beschrijving interventie')

        self._eindeSdh1 = EMAttribuut(field=DateTimeField,
                                      naam='Einde (SDH 1)',
                                      label='Einde (SDH 1)',
                                      objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#SDH.eindeSdh1',
                                      definitie='Definitie nog toe te voegen voor eigenschap Einde (SDH 1)')

        self._eindeSdh = EMAttribuut(field=DateTimeField,
                                     naam='Einde (SDH)',
                                     label='Einde (SDH)',
                                     objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#SDH.eindeSdh',
                                     definitie='Definitie nog toe te voegen voor eigenschap Einde (SDH)')

        self._elektrischPlanInstallatieOk = EMAttribuut(field=BooleanField,
                                                        naam='Elektrisch plan / installatie OK',
                                                        label='Elektrisch plan / installatie OK',
                                                        objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.elektrischPlanInstallatieOk',
                                                        definitie='Definitie nog toe te voegen voor eigenschap Elektrisch plan / installatie OK')

        self._elektrischPlanInstallatieOkOud = EMAttribuut(field=StringField,
                                                           naam='Elektrisch plan/installatie OK oud',
                                                           label='Elektrisch plan/installatie OK oud',
                                                           objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.elektrischPlanInstallatieOkOud',
                                                           definitie='Definitie nog toe te voegen voor eigenschap Elektrisch plan/installatie OK oud')

        self._fotoSApparatuurGemaakt = EMAttribuut(field=BooleanField,
                                                   naam="Foto's apparatuur gemaakt",
                                                   label="Foto's apparatuur gemaakt",
                                                   objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.fotoSApparatuurGemaakt',
                                                   definitie="Definitie nog toe te voegen voor eigenschap Foto\'s apparatuur gemaakt")

        self._glasvezelOkBevestigingLabels = EMAttribuut(field=BooleanField,
                                                         naam='Glasvezel OK (bevestiging, labels)',
                                                         label='Glasvezel OK (bevestiging, labels)',
                                                         objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.glasvezelOkBevestigingLabels',
                                                         definitie='Definitie nog toe te voegen voor eigenschap Glasvezel OK (bevestiging, labels)')

        self._glasvezelOkSelectielijst = EMAttribuut(field=StringField,
                                                     naam='Glasvezel OK selectielijst',
                                                     label='Glasvezel OK selectielijst',
                                                     objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.glasvezelOkSelectielijst',
                                                     definitie='Definitie nog toe te voegen voor eigenschap Glasvezel OK selectielijst')

        self._glasvezelConnectorsOk = EMAttribuut(field=BooleanField,
                                                  naam='Glasvezel connectors OK',
                                                  label='Glasvezel connectors OK',
                                                  objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.glasvezelConnectorsOk',
                                                  definitie='Definitie nog toe te voegen voor eigenschap Glasvezel connectors OK')

        self._glasvezelConnectorsOkSelectie = EMAttribuut(field=StringField,
                                                          naam='Glasvezel connectors OK selectie',
                                                          label='Glasvezel connectors OK selectie',
                                                          objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#SDH.glasvezelConnectorsOkSelectie',
                                                          definitie='Definitie nog toe te voegen voor eigenschap Glasvezel connectors OK selectie')

        self._klimatiseringLocatieOk = EMAttribuut(field=BooleanField,
                                                   naam='Klimatisering locatie OK',
                                                   label='Klimatisering locatie OK',
                                                   objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.klimatiseringLocatieOk',
                                                   definitie='Definitie nog toe te voegen voor eigenschap Klimatisering locatie OK')

        self._koperkabelOkBevestigingLabels = EMAttribuut(field=BooleanField,
                                                          naam='Koperkabel OK (bevestiging,labels)',
                                                          label='Koperkabel OK (bevestiging,labels)',
                                                          objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.koperkabelOkBevestigingLabels',
                                                          definitie='Definitie nog toe te voegen voor eigenschap Koperkabel OK (bevestiging,labels)')

        self._koperkabelOkSelectie = EMAttribuut(field=StringField,
                                                 naam='Koperkabel OK selectie',
                                                 label='Koperkabel OK selectie',
                                                 objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#SDH.koperkabelOkSelectie',
                                                 definitie='Definitie nog toe te voegen voor eigenschap Koperkabel OK selectie')

        self._locatieBereikbaar = EMAttribuut(field=BooleanField,
                                              naam='Locatie bereikbaar',
                                              label='Locatie bereikbaar',
                                              objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.locatieBereikbaar',
                                              definitie='Definitie nog toe te voegen voor eigenschap Locatie bereikbaar')

        self._naarWie = EMAttribuut(field=StringField,
                                    naam='Naar wie',
                                    label='Naar wie',
                                    objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.naarWie',
                                    definitie='Definitie nog toe te voegen voor eigenschap Naar wie')

        self._opmerkingenSdh1 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (SDH 1)',
                                            label='Opmerkingen (SDH 1)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#SDH.opmerkingenSdh1',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 1)')

        self._opmerkingenSdh10 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (SDH 10)',
                                             label='Opmerkingen (SDH 10)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#SDH.opmerkingenSdh10',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 10)')

        self._opmerkingenSdh11 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (SDH 11)',
                                             label='Opmerkingen (SDH 11)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#SDH.opmerkingenSdh11',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 11)')

        self._opmerkingenSdh12 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (SDH 12)',
                                             label='Opmerkingen (SDH 12)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#SDH.opmerkingenSdh12',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 12)')

        self._opmerkingenSdh13 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (SDH 13)',
                                             label='Opmerkingen (SDH 13)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#SDH.opmerkingenSdh13',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 13)')

        self._opmerkingenSdh15 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (SDH 15)',
                                             label='Opmerkingen (SDH 15)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#SDH.opmerkingenSdh15',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 15)')

        self._opmerkingenSdh16 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (SDH 16)',
                                             label='Opmerkingen (SDH 16)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#SDH.opmerkingenSdh16',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 16)')

        self._opmerkingenSdh17 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (SDH 17)',
                                             label='Opmerkingen (SDH 17)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#SDH.opmerkingenSdh17',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 17)')

        self._opmerkingenSdh18 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (SDH 18)',
                                             label='Opmerkingen (SDH 18)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#SDH.opmerkingenSdh18',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 18)')

        self._opmerkingenSdh19 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (SDH 19)',
                                             label='Opmerkingen (SDH 19)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#SDH.opmerkingenSdh19',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 19)')

        self._opmerkingenSdh2 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (SDH 2)',
                                            label='Opmerkingen (SDH 2)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#SDH.opmerkingenSdh2',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 2)')

        self._opmerkingenSdh20 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (SDH 20)',
                                             label='Opmerkingen (SDH 20)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#SDH.opmerkingenSdh20',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 20)')

        self._opmerkingenSdh21 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (SDH 21)',
                                             label='Opmerkingen (SDH 21)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#SDH.opmerkingenSdh21',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 21)')

        self._opmerkingenSdh22 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (SDH 22)',
                                             label='Opmerkingen (SDH 22)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#SDH.opmerkingenSdh22',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 22)')

        self._opmerkingenSdh3 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (SDH 3)',
                                            label='Opmerkingen (SDH 3)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#SDH.opmerkingenSdh3',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 3)')

        self._opmerkingenSdh4 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (SDH 4)',
                                            label='Opmerkingen (SDH 4)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#SDH.opmerkingenSdh4',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 4)')

        self._opmerkingenSdh5 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (SDH 5)',
                                            label='Opmerkingen (SDH 5)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#SDH.opmerkingenSdh5',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 5)')

        self._opmerkingenSdh6 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (SDH 6)',
                                            label='Opmerkingen (SDH 6)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#SDH.opmerkingenSdh6',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 6)')

        self._opmerkingenSdh7 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (SDH 7)',
                                            label='Opmerkingen (SDH 7)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#SDH.opmerkingenSdh7',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 7)')

        self._opmerkingenSdh8 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (SDH 8)',
                                            label='Opmerkingen (SDH 8)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#SDH.opmerkingenSdh8',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 8)')

        self._opmerkingenSdh9 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (SDH 9)',
                                            label='Opmerkingen (SDH 9)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#SDH.opmerkingenSdh9',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 9)')

        self._opmerkingenSdh = EMAttribuut(field=StringField,
                                           naam='Opmerkingen (SDH)',
                                           label='Opmerkingen (SDH)',
                                           objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#SDH.opmerkingenSdh',
                                           definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH)')

        self._opmerkingenInspectie = EMAttribuut(field=StringField,
                                                 naam='Opmerkingen inspectie',
                                                 label='Opmerkingen inspectie',
                                                 objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.opmerkingenInspectie',
                                                 definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen inspectie')

        self._startSdh1 = EMAttribuut(field=DateTimeField,
                                      naam='Start (SDH 1)',
                                      label='Start (SDH 1)',
                                      objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#SDH.startSdh1',
                                      definitie='Definitie nog toe te voegen voor eigenschap Start (SDH 1)')

        self._startSdh = EMAttribuut(field=DateTimeField,
                                     naam='Start (SDH)',
                                     label='Start (SDH)',
                                     objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#SDH.startSdh',
                                     definitie='Definitie nog toe te voegen voor eigenschap Start (SDH)')

        self._upsOk = EMAttribuut(field=StringField,
                                  naam='UPS OK',
                                  label='UPS OK',
                                  objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.upsOk',
                                  definitie='Definitie nog toe te voegen voor eigenschap UPS OK')

        self._upsOkOud = EMAttribuut(field=StringField,
                                     naam='UPS OK oud',
                                     label='UPS OK oud',
                                     objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.upsOkOud',
                                     definitie='Definitie nog toe te voegen voor eigenschap UPS OK oud')

        self._ventilatieLocatieOk = EMAttribuut(field=BooleanField,
                                                naam='Ventilatie locatie OK',
                                                label='Ventilatie locatie OK',
                                                objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.ventilatieLocatieOk',
                                                definitie='Definitie nog toe te voegen voor eigenschap Ventilatie locatie OK')

        self._verlichtingLocatieOk = EMAttribuut(field=BooleanField,
                                                 naam='Verlichting locatie OK',
                                                 label='Verlichting locatie OK',
                                                 objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.verlichtingLocatieOk',
                                                 definitie='Definitie nog toe te voegen voor eigenschap Verlichting locatie OK')

        self._voedingskabelsOk = EMAttribuut(field=BooleanField,
                                             naam='Voedingskabels OK',
                                             label='Voedingskabels OK',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.voedingskabelsOk',
                                             definitie='Definitie nog toe te voegen voor eigenschap Voedingskabels OK')

        self._voedingsstekkersOk = EMAttribuut(field=BooleanField,
                                               naam='Voedingsstekkers OK',
                                               label='Voedingsstekkers OK',
                                               objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.voedingsstekkersOk',
                                               definitie='Definitie nog toe te voegen voor eigenschap Voedingsstekkers OK')

        self._einde = EMAttribuut(field=DateTimeField,
                                  naam='einde',
                                  label='einde',
                                  objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.einde',
                                  definitie='Definitie nog toe te voegen voor eigenschap einde')

        self._labelContactInfoApparatuurOk = EMAttribuut(field=BooleanField,
                                                         naam='label contact info apparatuur OK',
                                                         label='label contact info apparatuur OK',
                                                         objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.labelContactInfoApparatuurOk',
                                                         definitie='Definitie nog toe te voegen voor eigenschap label contact info apparatuur OK')

        self._labelInstallatieNrApparatuurOk = EMAttribuut(field=BooleanField,
                                                           naam='label installatie nr apparatuur OK',
                                                           label='label installatie nr apparatuur OK',
                                                           objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.labelInstallatieNrApparatuurOk',
                                                           definitie='Definitie nog toe te voegen voor eigenschap label installatie nr apparatuur OK')

        self._opmerkingenSdh14 = EMAttribuut(field=StringField,
                                             naam='opmerkingen (SDH 14)',
                                             label='opmerkingen (SDH 14)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#SDH.opmerkingenSdh14',
                                             definitie='Definitie nog toe te voegen voor eigenschap opmerkingen (SDH 14)')

        self._start = EMAttribuut(field=DateTimeField,
                                  naam='start',
                                  label='start',
                                  objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.start',
                                  definitie='Definitie nog toe te voegen voor eigenschap start')

    @property
    def DubbeleVoedingOk(self):
        """Definitie nog toe te voegen voor eigenschap (Dubbele) voeding OK"""
        return self._DubbeleVoedingOk.waarde

    @DubbeleVoedingOk.setter
    def DubbeleVoedingOk(self, value):
        self._DubbeleVoedingOk.set_waarde(value, owner=self)

    @property
    def 1WaaromNiet(self):
        """Definitie nog toe te voegen voor eigenschap Waarom niet?"""
        return self._1WaaromNiet.waarde

    @1WaaromNiet.setter
    def 1WaaromNiet(self, value):
        self._1WaaromNiet.set_waarde(value, owner=self)

    @property
    def 101SiteVerantwoordelijkeGeNformeerd(self):
        """Definitie nog toe te voegen voor eigenschap Site verantwoordelijke geÃ¯nformeerd"""
        return self._101SiteVerantwoordelijkeGeNformeerd.waarde

    @101SiteVerantwoordelijkeGeNformeerd.setter
    def 101SiteVerantwoordelijkeGeNformeerd(self, value):
        self._101SiteVerantwoordelijkeGeNformeerd.set_waarde(value, owner=self)

    @property
    def 215Actie(self):
        """Definitie nog toe te voegen voor eigenschap Actie"""
        return self._215Actie.waarde

    @215Actie.setter
    def 215Actie(self, value):
        self._215Actie.set_waarde(value, owner=self)

    @property
    def 601SiteVerantwoordelijkeGeNformeerd(self):
        """Definitie nog toe te voegen voor eigenschap Site verantwoordelijke geÃ¯nformeerd"""
        return self._601SiteVerantwoordelijkeGeNformeerd.waarde

    @601SiteVerantwoordelijkeGeNformeerd.setter
    def 601SiteVerantwoordelijkeGeNformeerd(self, value):
        self._601SiteVerantwoordelijkeGeNformeerd.set_waarde(value, owner=self)

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
    def eindeSdh1(self):
        """Definitie nog toe te voegen voor eigenschap Einde (SDH 1)"""
        return self._eindeSdh1.waarde

    @eindeSdh1.setter
    def eindeSdh1(self, value):
        self._eindeSdh1.set_waarde(value, owner=self)

    @property
    def eindeSdh(self):
        """Definitie nog toe te voegen voor eigenschap Einde (SDH)"""
        return self._eindeSdh.waarde

    @eindeSdh.setter
    def eindeSdh(self, value):
        self._eindeSdh.set_waarde(value, owner=self)

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
    def glasvezelConnectorsOkSelectie(self):
        """Definitie nog toe te voegen voor eigenschap Glasvezel connectors OK selectie"""
        return self._glasvezelConnectorsOkSelectie.waarde

    @glasvezelConnectorsOkSelectie.setter
    def glasvezelConnectorsOkSelectie(self, value):
        self._glasvezelConnectorsOkSelectie.set_waarde(value, owner=self)

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
    def koperkabelOkSelectie(self):
        """Definitie nog toe te voegen voor eigenschap Koperkabel OK selectie"""
        return self._koperkabelOkSelectie.waarde

    @koperkabelOkSelectie.setter
    def koperkabelOkSelectie(self, value):
        self._koperkabelOkSelectie.set_waarde(value, owner=self)

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
    def opmerkingenSdh1(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 1)"""
        return self._opmerkingenSdh1.waarde

    @opmerkingenSdh1.setter
    def opmerkingenSdh1(self, value):
        self._opmerkingenSdh1.set_waarde(value, owner=self)

    @property
    def opmerkingenSdh10(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 10)"""
        return self._opmerkingenSdh10.waarde

    @opmerkingenSdh10.setter
    def opmerkingenSdh10(self, value):
        self._opmerkingenSdh10.set_waarde(value, owner=self)

    @property
    def opmerkingenSdh11(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 11)"""
        return self._opmerkingenSdh11.waarde

    @opmerkingenSdh11.setter
    def opmerkingenSdh11(self, value):
        self._opmerkingenSdh11.set_waarde(value, owner=self)

    @property
    def opmerkingenSdh12(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 12)"""
        return self._opmerkingenSdh12.waarde

    @opmerkingenSdh12.setter
    def opmerkingenSdh12(self, value):
        self._opmerkingenSdh12.set_waarde(value, owner=self)

    @property
    def opmerkingenSdh13(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 13)"""
        return self._opmerkingenSdh13.waarde

    @opmerkingenSdh13.setter
    def opmerkingenSdh13(self, value):
        self._opmerkingenSdh13.set_waarde(value, owner=self)

    @property
    def opmerkingenSdh15(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 15)"""
        return self._opmerkingenSdh15.waarde

    @opmerkingenSdh15.setter
    def opmerkingenSdh15(self, value):
        self._opmerkingenSdh15.set_waarde(value, owner=self)

    @property
    def opmerkingenSdh16(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 16)"""
        return self._opmerkingenSdh16.waarde

    @opmerkingenSdh16.setter
    def opmerkingenSdh16(self, value):
        self._opmerkingenSdh16.set_waarde(value, owner=self)

    @property
    def opmerkingenSdh17(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 17)"""
        return self._opmerkingenSdh17.waarde

    @opmerkingenSdh17.setter
    def opmerkingenSdh17(self, value):
        self._opmerkingenSdh17.set_waarde(value, owner=self)

    @property
    def opmerkingenSdh18(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 18)"""
        return self._opmerkingenSdh18.waarde

    @opmerkingenSdh18.setter
    def opmerkingenSdh18(self, value):
        self._opmerkingenSdh18.set_waarde(value, owner=self)

    @property
    def opmerkingenSdh19(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 19)"""
        return self._opmerkingenSdh19.waarde

    @opmerkingenSdh19.setter
    def opmerkingenSdh19(self, value):
        self._opmerkingenSdh19.set_waarde(value, owner=self)

    @property
    def opmerkingenSdh2(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 2)"""
        return self._opmerkingenSdh2.waarde

    @opmerkingenSdh2.setter
    def opmerkingenSdh2(self, value):
        self._opmerkingenSdh2.set_waarde(value, owner=self)

    @property
    def opmerkingenSdh20(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 20)"""
        return self._opmerkingenSdh20.waarde

    @opmerkingenSdh20.setter
    def opmerkingenSdh20(self, value):
        self._opmerkingenSdh20.set_waarde(value, owner=self)

    @property
    def opmerkingenSdh21(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 21)"""
        return self._opmerkingenSdh21.waarde

    @opmerkingenSdh21.setter
    def opmerkingenSdh21(self, value):
        self._opmerkingenSdh21.set_waarde(value, owner=self)

    @property
    def opmerkingenSdh22(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 22)"""
        return self._opmerkingenSdh22.waarde

    @opmerkingenSdh22.setter
    def opmerkingenSdh22(self, value):
        self._opmerkingenSdh22.set_waarde(value, owner=self)

    @property
    def opmerkingenSdh3(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 3)"""
        return self._opmerkingenSdh3.waarde

    @opmerkingenSdh3.setter
    def opmerkingenSdh3(self, value):
        self._opmerkingenSdh3.set_waarde(value, owner=self)

    @property
    def opmerkingenSdh4(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 4)"""
        return self._opmerkingenSdh4.waarde

    @opmerkingenSdh4.setter
    def opmerkingenSdh4(self, value):
        self._opmerkingenSdh4.set_waarde(value, owner=self)

    @property
    def opmerkingenSdh5(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 5)"""
        return self._opmerkingenSdh5.waarde

    @opmerkingenSdh5.setter
    def opmerkingenSdh5(self, value):
        self._opmerkingenSdh5.set_waarde(value, owner=self)

    @property
    def opmerkingenSdh6(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 6)"""
        return self._opmerkingenSdh6.waarde

    @opmerkingenSdh6.setter
    def opmerkingenSdh6(self, value):
        self._opmerkingenSdh6.set_waarde(value, owner=self)

    @property
    def opmerkingenSdh7(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 7)"""
        return self._opmerkingenSdh7.waarde

    @opmerkingenSdh7.setter
    def opmerkingenSdh7(self, value):
        self._opmerkingenSdh7.set_waarde(value, owner=self)

    @property
    def opmerkingenSdh8(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 8)"""
        return self._opmerkingenSdh8.waarde

    @opmerkingenSdh8.setter
    def opmerkingenSdh8(self, value):
        self._opmerkingenSdh8.set_waarde(value, owner=self)

    @property
    def opmerkingenSdh9(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH 9)"""
        return self._opmerkingenSdh9.waarde

    @opmerkingenSdh9.setter
    def opmerkingenSdh9(self, value):
        self._opmerkingenSdh9.set_waarde(value, owner=self)

    @property
    def opmerkingenSdh(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (SDH)"""
        return self._opmerkingenSdh.waarde

    @opmerkingenSdh.setter
    def opmerkingenSdh(self, value):
        self._opmerkingenSdh.set_waarde(value, owner=self)

    @property
    def opmerkingenInspectie(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen inspectie"""
        return self._opmerkingenInspectie.waarde

    @opmerkingenInspectie.setter
    def opmerkingenInspectie(self, value):
        self._opmerkingenInspectie.set_waarde(value, owner=self)

    @property
    def startSdh1(self):
        """Definitie nog toe te voegen voor eigenschap Start (SDH 1)"""
        return self._startSdh1.waarde

    @startSdh1.setter
    def startSdh1(self, value):
        self._startSdh1.set_waarde(value, owner=self)

    @property
    def startSdh(self):
        """Definitie nog toe te voegen voor eigenschap Start (SDH)"""
        return self._startSdh.waarde

    @startSdh.setter
    def startSdh(self, value):
        self._startSdh.set_waarde(value, owner=self)

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
    def opmerkingenSdh14(self):
        """Definitie nog toe te voegen voor eigenschap opmerkingen (SDH 14)"""
        return self._opmerkingenSdh14.waarde

    @opmerkingenSdh14.setter
    def opmerkingenSdh14(self, value):
        self._opmerkingenSdh14.set_waarde(value, owner=self)

    @property
    def start(self):
        """Definitie nog toe te voegen voor eigenschap start"""
        return self._start.waarde

    @start.setter
    def start(self, value):
        self._start.set_waarde(value, owner=self)

