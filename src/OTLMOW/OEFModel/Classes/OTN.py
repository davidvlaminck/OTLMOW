# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from OTLMOW.OTLModel.Datatypes.DateTimeField import DateTimeField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class OTN(EMObject):
    """Optical Transport Network"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#OTN'
    label = 'Optical transport network'

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

        self._eindeOtn1 = EMAttribuut(field=DateTimeField,
                                      naam='Einde (OTN 1)',
                                      label='Einde (OTN 1)',
                                      objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#OTN.eindeOtn1',
                                      definitie='Definitie nog toe te voegen voor eigenschap Einde (OTN 1)')

        self._eindeOtn = EMAttribuut(field=DateTimeField,
                                     naam='Einde (OTN)',
                                     label='Einde (OTN)',
                                     objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#OTN.eindeOtn',
                                     definitie='Definitie nog toe te voegen voor eigenschap Einde (OTN)')

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

        self._glasvezelConnectorsOkOud = EMAttribuut(field=StringField,
                                                     naam='Glasvezel connectors OK oud',
                                                     label='Glasvezel connectors OK oud',
                                                     objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.glasvezelConnectorsOkOud',
                                                     definitie='Definitie nog toe te voegen voor eigenschap Glasvezel connectors OK oud')

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

        self._koperkabelOkSelectielijst = EMAttribuut(field=StringField,
                                                      naam='Koperkabel OK selectielijst',
                                                      label='Koperkabel OK selectielijst',
                                                      objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.koperkabelOkSelectielijst',
                                                      definitie='Definitie nog toe te voegen voor eigenschap Koperkabel OK selectielijst')

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

        self._nazichtUps = EMAttribuut(field=StringField,
                                       naam='Nazicht UPS',
                                       label='Nazicht UPS',
                                       objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.nazichtUps',
                                       definitie='Definitie nog toe te voegen voor eigenschap Nazicht UPS')

        self._opmerkingenOtn1 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (OTN 1)',
                                            label='Opmerkingen (OTN 1)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#OTN.opmerkingenOtn1',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 1)')

        self._opmerkingenOtn10 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (OTN 10)',
                                             label='Opmerkingen (OTN 10)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#OTN.opmerkingenOtn10',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 10)')

        self._opmerkingenOtn11 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (OTN 11)',
                                             label='Opmerkingen (OTN 11)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#OTN.opmerkingenOtn11',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 11)')

        self._opmerkingenOtn12 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (OTN 12)',
                                             label='Opmerkingen (OTN 12)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#OTN.opmerkingenOtn12',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 12)')

        self._opmerkingenOtn13 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (OTN 13)',
                                             label='Opmerkingen (OTN 13)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#OTN.opmerkingenOtn13',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 13)')

        self._opmerkingenOtn15 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (OTN 15)',
                                             label='Opmerkingen (OTN 15)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#OTN.opmerkingenOtn15',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 15)')

        self._opmerkingenOtn16 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (OTN 16)',
                                             label='Opmerkingen (OTN 16)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#OTN.opmerkingenOtn16',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 16)')

        self._opmerkingenOtn17 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (OTN 17)',
                                             label='Opmerkingen (OTN 17)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#OTN.opmerkingenOtn17',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 17)')

        self._opmerkingenOtn18 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (OTN 18)',
                                             label='Opmerkingen (OTN 18)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#OTN.opmerkingenOtn18',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 18)')

        self._opmerkingenOtn19 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (OTN 19)',
                                             label='Opmerkingen (OTN 19)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#OTN.opmerkingenOtn19',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 19)')

        self._opmerkingenOtn2 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (OTN 2)',
                                            label='Opmerkingen (OTN 2)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#OTN.opmerkingenOtn2',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 2)')

        self._opmerkingenOtn20 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (OTN 20)',
                                             label='Opmerkingen (OTN 20)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#OTN.opmerkingenOtn20',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 20)')

        self._opmerkingenOtn21 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (OTN 21)',
                                             label='Opmerkingen (OTN 21)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#OTN.opmerkingenOtn21',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 21)')

        self._opmerkingenOtn3 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (OTN 3)',
                                            label='Opmerkingen (OTN 3)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#OTN.opmerkingenOtn3',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 3)')

        self._opmerkingenOtn4 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (OTN 4)',
                                            label='Opmerkingen (OTN 4)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#OTN.opmerkingenOtn4',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 4)')

        self._opmerkingenOtn5 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (OTN 5)',
                                            label='Opmerkingen (OTN 5)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#OTN.opmerkingenOtn5',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 5)')

        self._opmerkingenOtn6 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (OTN 6)',
                                            label='Opmerkingen (OTN 6)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#OTN.opmerkingenOtn6',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 6)')

        self._opmerkingenOtn7 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (OTN 7)',
                                            label='Opmerkingen (OTN 7)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#OTN.opmerkingenOtn7',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 7)')

        self._opmerkingenOtn8 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (OTN 8)',
                                            label='Opmerkingen (OTN 8)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#OTN.opmerkingenOtn8',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 8)')

        self._opmerkingenOtn9 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (OTN 9)',
                                            label='Opmerkingen (OTN 9)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#OTN.opmerkingenOtn9',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 9)')

        self._opmerkingenOtn = EMAttribuut(field=StringField,
                                           naam='Opmerkingen (OTN)',
                                           label='Opmerkingen (OTN)',
                                           objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#OTN.opmerkingenOtn',
                                           definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN)')

        self._opmerkingenInspectie = EMAttribuut(field=StringField,
                                                 naam='Opmerkingen inspectie',
                                                 label='Opmerkingen inspectie',
                                                 objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.opmerkingenInspectie',
                                                 definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen inspectie')

        self._startOtn1 = EMAttribuut(field=DateTimeField,
                                      naam='Start (OTN 1)',
                                      label='Start (OTN 1)',
                                      objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#OTN.startOtn1',
                                      definitie='Definitie nog toe te voegen voor eigenschap Start (OTN 1)')

        self._startOtn = EMAttribuut(field=DateTimeField,
                                     naam='Start (OTN)',
                                     label='Start (OTN)',
                                     objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#OTN.startOtn',
                                     definitie='Definitie nog toe te voegen voor eigenschap Start (OTN)')

        self._upsOk = EMAttribuut(field=StringField,
                                  naam='UPS OK',
                                  label='UPS OK',
                                  objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.upsOk',
                                  definitie='Definitie nog toe te voegen voor eigenschap UPS OK')

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

        self._opmerkingenOtn14 = EMAttribuut(field=StringField,
                                             naam='opmerkingen (OTN 14)',
                                             label='opmerkingen (OTN 14)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#OTN.opmerkingenOtn14',
                                             definitie='Definitie nog toe te voegen voor eigenschap opmerkingen (OTN 14)')

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
    def eindeOtn1(self):
        """Definitie nog toe te voegen voor eigenschap Einde (OTN 1)"""
        return self._eindeOtn1.waarde

    @eindeOtn1.setter
    def eindeOtn1(self, value):
        self._eindeOtn1.set_waarde(value, owner=self)

    @property
    def eindeOtn(self):
        """Definitie nog toe te voegen voor eigenschap Einde (OTN)"""
        return self._eindeOtn.waarde

    @eindeOtn.setter
    def eindeOtn(self, value):
        self._eindeOtn.set_waarde(value, owner=self)

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
    def opmerkingenOtn1(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 1)"""
        return self._opmerkingenOtn1.waarde

    @opmerkingenOtn1.setter
    def opmerkingenOtn1(self, value):
        self._opmerkingenOtn1.set_waarde(value, owner=self)

    @property
    def opmerkingenOtn10(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 10)"""
        return self._opmerkingenOtn10.waarde

    @opmerkingenOtn10.setter
    def opmerkingenOtn10(self, value):
        self._opmerkingenOtn10.set_waarde(value, owner=self)

    @property
    def opmerkingenOtn11(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 11)"""
        return self._opmerkingenOtn11.waarde

    @opmerkingenOtn11.setter
    def opmerkingenOtn11(self, value):
        self._opmerkingenOtn11.set_waarde(value, owner=self)

    @property
    def opmerkingenOtn12(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 12)"""
        return self._opmerkingenOtn12.waarde

    @opmerkingenOtn12.setter
    def opmerkingenOtn12(self, value):
        self._opmerkingenOtn12.set_waarde(value, owner=self)

    @property
    def opmerkingenOtn13(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 13)"""
        return self._opmerkingenOtn13.waarde

    @opmerkingenOtn13.setter
    def opmerkingenOtn13(self, value):
        self._opmerkingenOtn13.set_waarde(value, owner=self)

    @property
    def opmerkingenOtn15(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 15)"""
        return self._opmerkingenOtn15.waarde

    @opmerkingenOtn15.setter
    def opmerkingenOtn15(self, value):
        self._opmerkingenOtn15.set_waarde(value, owner=self)

    @property
    def opmerkingenOtn16(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 16)"""
        return self._opmerkingenOtn16.waarde

    @opmerkingenOtn16.setter
    def opmerkingenOtn16(self, value):
        self._opmerkingenOtn16.set_waarde(value, owner=self)

    @property
    def opmerkingenOtn17(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 17)"""
        return self._opmerkingenOtn17.waarde

    @opmerkingenOtn17.setter
    def opmerkingenOtn17(self, value):
        self._opmerkingenOtn17.set_waarde(value, owner=self)

    @property
    def opmerkingenOtn18(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 18)"""
        return self._opmerkingenOtn18.waarde

    @opmerkingenOtn18.setter
    def opmerkingenOtn18(self, value):
        self._opmerkingenOtn18.set_waarde(value, owner=self)

    @property
    def opmerkingenOtn19(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 19)"""
        return self._opmerkingenOtn19.waarde

    @opmerkingenOtn19.setter
    def opmerkingenOtn19(self, value):
        self._opmerkingenOtn19.set_waarde(value, owner=self)

    @property
    def opmerkingenOtn2(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 2)"""
        return self._opmerkingenOtn2.waarde

    @opmerkingenOtn2.setter
    def opmerkingenOtn2(self, value):
        self._opmerkingenOtn2.set_waarde(value, owner=self)

    @property
    def opmerkingenOtn20(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 20)"""
        return self._opmerkingenOtn20.waarde

    @opmerkingenOtn20.setter
    def opmerkingenOtn20(self, value):
        self._opmerkingenOtn20.set_waarde(value, owner=self)

    @property
    def opmerkingenOtn21(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 21)"""
        return self._opmerkingenOtn21.waarde

    @opmerkingenOtn21.setter
    def opmerkingenOtn21(self, value):
        self._opmerkingenOtn21.set_waarde(value, owner=self)

    @property
    def opmerkingenOtn3(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 3)"""
        return self._opmerkingenOtn3.waarde

    @opmerkingenOtn3.setter
    def opmerkingenOtn3(self, value):
        self._opmerkingenOtn3.set_waarde(value, owner=self)

    @property
    def opmerkingenOtn4(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 4)"""
        return self._opmerkingenOtn4.waarde

    @opmerkingenOtn4.setter
    def opmerkingenOtn4(self, value):
        self._opmerkingenOtn4.set_waarde(value, owner=self)

    @property
    def opmerkingenOtn5(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 5)"""
        return self._opmerkingenOtn5.waarde

    @opmerkingenOtn5.setter
    def opmerkingenOtn5(self, value):
        self._opmerkingenOtn5.set_waarde(value, owner=self)

    @property
    def opmerkingenOtn6(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 6)"""
        return self._opmerkingenOtn6.waarde

    @opmerkingenOtn6.setter
    def opmerkingenOtn6(self, value):
        self._opmerkingenOtn6.set_waarde(value, owner=self)

    @property
    def opmerkingenOtn7(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 7)"""
        return self._opmerkingenOtn7.waarde

    @opmerkingenOtn7.setter
    def opmerkingenOtn7(self, value):
        self._opmerkingenOtn7.set_waarde(value, owner=self)

    @property
    def opmerkingenOtn8(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 8)"""
        return self._opmerkingenOtn8.waarde

    @opmerkingenOtn8.setter
    def opmerkingenOtn8(self, value):
        self._opmerkingenOtn8.set_waarde(value, owner=self)

    @property
    def opmerkingenOtn9(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN 9)"""
        return self._opmerkingenOtn9.waarde

    @opmerkingenOtn9.setter
    def opmerkingenOtn9(self, value):
        self._opmerkingenOtn9.set_waarde(value, owner=self)

    @property
    def opmerkingenOtn(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (OTN)"""
        return self._opmerkingenOtn.waarde

    @opmerkingenOtn.setter
    def opmerkingenOtn(self, value):
        self._opmerkingenOtn.set_waarde(value, owner=self)

    @property
    def opmerkingenInspectie(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen inspectie"""
        return self._opmerkingenInspectie.waarde

    @opmerkingenInspectie.setter
    def opmerkingenInspectie(self, value):
        self._opmerkingenInspectie.set_waarde(value, owner=self)

    @property
    def startOtn1(self):
        """Definitie nog toe te voegen voor eigenschap Start (OTN 1)"""
        return self._startOtn1.waarde

    @startOtn1.setter
    def startOtn1(self, value):
        self._startOtn1.set_waarde(value, owner=self)

    @property
    def startOtn(self):
        """Definitie nog toe te voegen voor eigenschap Start (OTN)"""
        return self._startOtn.waarde

    @startOtn.setter
    def startOtn(self, value):
        self._startOtn.set_waarde(value, owner=self)

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
    def opmerkingenOtn14(self):
        """Definitie nog toe te voegen voor eigenschap opmerkingen (OTN 14)"""
        return self._opmerkingenOtn14.waarde

    @opmerkingenOtn14.setter
    def opmerkingenOtn14(self, value):
        self._opmerkingenOtn14.set_waarde(value, owner=self)

    @property
    def start(self):
        """Definitie nog toe te voegen voor eigenschap start"""
        return self._start.waarde

    @start.setter
    def start(self, value):
        self._start.set_waarde(value, owner=self)

