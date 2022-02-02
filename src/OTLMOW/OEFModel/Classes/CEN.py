# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from OTLMOW.OTLModel.Datatypes.DateTimeField import DateTimeField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class CEN(EMObject):
    """CE Netwerk"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#CEN'
    label = 'CE netwerk'

    def __init__(self):
        super().__init__()

        self._DubbeleVoedingOk = EMAttribuut(field=StringField,
                                             naam='(Dubbele) voeding OK',
                                             label='(Dubbele) voeding OK',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.DubbeleVoedingOk',
                                             definitie='Definitie nog toe te voegen voor eigenschap (Dubbele) voeding OK')

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

        self._eindeCen1 = EMAttribuut(field=DateTimeField,
                                      naam='Einde (CEN 1)',
                                      label='Einde (CEN 1)',
                                      objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#CEN.eindeCen1',
                                      definitie='Definitie nog toe te voegen voor eigenschap Einde (CEN 1)')

        self._eindeCen = EMAttribuut(field=DateTimeField,
                                     naam='Einde (CEN)',
                                     label='Einde (CEN)',
                                     objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#CEN.eindeCen',
                                     definitie='Definitie nog toe te voegen voor eigenschap Einde (CEN)')

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

        self._nazichtUpsOud = EMAttribuut(field=StringField,
                                          naam='Nazicht UPS oud',
                                          label='Nazicht UPS oud',
                                          objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#CEN.nazichtUpsOud',
                                          definitie='Definitie nog toe te voegen voor eigenschap Nazicht UPS oud')

        self._opmerkingenCen1 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (CEN 1)',
                                            label='Opmerkingen (CEN 1)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#CEN.opmerkingenCen1',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 1)')

        self._opmerkingenCen10 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (CEN 10)',
                                             label='Opmerkingen (CEN 10)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#CEN.opmerkingenCen10',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 10)')

        self._opmerkingenCen11 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (CEN 11)',
                                             label='Opmerkingen (CEN 11)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#CEN.opmerkingenCen11',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 11)')

        self._opmerkingenCen12 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (CEN 12)',
                                             label='Opmerkingen (CEN 12)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#CEN.opmerkingenCen12',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 12)')

        self._opmerkingenCen13 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (CEN 13)',
                                             label='Opmerkingen (CEN 13)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#CEN.opmerkingenCen13',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 13)')

        self._opmerkingenCen15 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (CEN 15)',
                                             label='Opmerkingen (CEN 15)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#CEN.opmerkingenCen15',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 15)')

        self._opmerkingenCen16 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (CEN 16)',
                                             label='Opmerkingen (CEN 16)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#CEN.opmerkingenCen16',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 16)')

        self._opmerkingenCen17 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (CEN 17)',
                                             label='Opmerkingen (CEN 17)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#CEN.opmerkingenCen17',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 17)')

        self._opmerkingenCen18 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (CEN 18)',
                                             label='Opmerkingen (CEN 18)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#CEN.opmerkingenCen18',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 18)')

        self._opmerkingenCen19 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (CEN 19)',
                                             label='Opmerkingen (CEN 19)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#CEN.opmerkingenCen19',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 19)')

        self._opmerkingenCen2 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (CEN 2)',
                                            label='Opmerkingen (CEN 2)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#CEN.opmerkingenCen2',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 2)')

        self._opmerkingenCen20 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (CEN 20)',
                                             label='Opmerkingen (CEN 20)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#CEN.opmerkingenCen20',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 20)')

        self._opmerkingenCen21 = EMAttribuut(field=StringField,
                                             naam='Opmerkingen (CEN 21)',
                                             label='Opmerkingen (CEN 21)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#CEN.opmerkingenCen21',
                                             definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 21)')

        self._opmerkingenCen3 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (CEN 3)',
                                            label='Opmerkingen (CEN 3)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#CEN.opmerkingenCen3',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 3)')

        self._opmerkingenCen4 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (CEN 4)',
                                            label='Opmerkingen (CEN 4)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#CEN.opmerkingenCen4',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 4)')

        self._opmerkingenCen5 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (CEN 5)',
                                            label='Opmerkingen (CEN 5)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#CEN.opmerkingenCen5',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 5)')

        self._opmerkingenCen6 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (CEN 6)',
                                            label='Opmerkingen (CEN 6)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#CEN.opmerkingenCen6',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 6)')

        self._opmerkingenCen7 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (CEN 7)',
                                            label='Opmerkingen (CEN 7)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#CEN.opmerkingenCen7',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 7)')

        self._opmerkingenCen8 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (CEN 8)',
                                            label='Opmerkingen (CEN 8)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#CEN.opmerkingenCen8',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 8)')

        self._opmerkingenCen9 = EMAttribuut(field=StringField,
                                            naam='Opmerkingen (CEN 9)',
                                            label='Opmerkingen (CEN 9)',
                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#CEN.opmerkingenCen9',
                                            definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 9)')

        self._opmerkingenCen = EMAttribuut(field=StringField,
                                           naam='Opmerkingen (CEN)',
                                           label='Opmerkingen (CEN)',
                                           objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#CEN.opmerkingenCen',
                                           definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN)')

        self._opmerkingenInspectie = EMAttribuut(field=StringField,
                                                 naam='Opmerkingen inspectie',
                                                 label='Opmerkingen inspectie',
                                                 objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.opmerkingenInspectie',
                                                 definitie='Definitie nog toe te voegen voor eigenschap Opmerkingen inspectie')

        self._startCen1 = EMAttribuut(field=DateTimeField,
                                      naam='Start (CEN 1)',
                                      label='Start (CEN 1)',
                                      objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#CEN.startCen1',
                                      definitie='Definitie nog toe te voegen voor eigenschap Start (CEN 1)')

        self._startCen = EMAttribuut(field=DateTimeField,
                                     naam='Start (CEN)',
                                     label='Start (CEN)',
                                     objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#CEN.startCen',
                                     definitie='Definitie nog toe te voegen voor eigenschap Start (CEN)')

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

        self._opmerkingenCen14 = EMAttribuut(field=StringField,
                                             naam='opmerkingen (CEN 14)',
                                             label='opmerkingen (CEN 14)',
                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#CEN.opmerkingenCen14',
                                             definitie='Definitie nog toe te voegen voor eigenschap opmerkingen (CEN 14)')

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
    def eindeCen1(self):
        """Definitie nog toe te voegen voor eigenschap Einde (CEN 1)"""
        return self._eindeCen1.waarde

    @eindeCen1.setter
    def eindeCen1(self, value):
        self._eindeCen1.set_waarde(value, owner=self)

    @property
    def eindeCen(self):
        """Definitie nog toe te voegen voor eigenschap Einde (CEN)"""
        return self._eindeCen.waarde

    @eindeCen.setter
    def eindeCen(self, value):
        self._eindeCen.set_waarde(value, owner=self)

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
    def nazichtUpsOud(self):
        """Definitie nog toe te voegen voor eigenschap Nazicht UPS oud"""
        return self._nazichtUpsOud.waarde

    @nazichtUpsOud.setter
    def nazichtUpsOud(self, value):
        self._nazichtUpsOud.set_waarde(value, owner=self)

    @property
    def opmerkingenCen1(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 1)"""
        return self._opmerkingenCen1.waarde

    @opmerkingenCen1.setter
    def opmerkingenCen1(self, value):
        self._opmerkingenCen1.set_waarde(value, owner=self)

    @property
    def opmerkingenCen10(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 10)"""
        return self._opmerkingenCen10.waarde

    @opmerkingenCen10.setter
    def opmerkingenCen10(self, value):
        self._opmerkingenCen10.set_waarde(value, owner=self)

    @property
    def opmerkingenCen11(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 11)"""
        return self._opmerkingenCen11.waarde

    @opmerkingenCen11.setter
    def opmerkingenCen11(self, value):
        self._opmerkingenCen11.set_waarde(value, owner=self)

    @property
    def opmerkingenCen12(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 12)"""
        return self._opmerkingenCen12.waarde

    @opmerkingenCen12.setter
    def opmerkingenCen12(self, value):
        self._opmerkingenCen12.set_waarde(value, owner=self)

    @property
    def opmerkingenCen13(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 13)"""
        return self._opmerkingenCen13.waarde

    @opmerkingenCen13.setter
    def opmerkingenCen13(self, value):
        self._opmerkingenCen13.set_waarde(value, owner=self)

    @property
    def opmerkingenCen15(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 15)"""
        return self._opmerkingenCen15.waarde

    @opmerkingenCen15.setter
    def opmerkingenCen15(self, value):
        self._opmerkingenCen15.set_waarde(value, owner=self)

    @property
    def opmerkingenCen16(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 16)"""
        return self._opmerkingenCen16.waarde

    @opmerkingenCen16.setter
    def opmerkingenCen16(self, value):
        self._opmerkingenCen16.set_waarde(value, owner=self)

    @property
    def opmerkingenCen17(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 17)"""
        return self._opmerkingenCen17.waarde

    @opmerkingenCen17.setter
    def opmerkingenCen17(self, value):
        self._opmerkingenCen17.set_waarde(value, owner=self)

    @property
    def opmerkingenCen18(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 18)"""
        return self._opmerkingenCen18.waarde

    @opmerkingenCen18.setter
    def opmerkingenCen18(self, value):
        self._opmerkingenCen18.set_waarde(value, owner=self)

    @property
    def opmerkingenCen19(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 19)"""
        return self._opmerkingenCen19.waarde

    @opmerkingenCen19.setter
    def opmerkingenCen19(self, value):
        self._opmerkingenCen19.set_waarde(value, owner=self)

    @property
    def opmerkingenCen2(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 2)"""
        return self._opmerkingenCen2.waarde

    @opmerkingenCen2.setter
    def opmerkingenCen2(self, value):
        self._opmerkingenCen2.set_waarde(value, owner=self)

    @property
    def opmerkingenCen20(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 20)"""
        return self._opmerkingenCen20.waarde

    @opmerkingenCen20.setter
    def opmerkingenCen20(self, value):
        self._opmerkingenCen20.set_waarde(value, owner=self)

    @property
    def opmerkingenCen21(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 21)"""
        return self._opmerkingenCen21.waarde

    @opmerkingenCen21.setter
    def opmerkingenCen21(self, value):
        self._opmerkingenCen21.set_waarde(value, owner=self)

    @property
    def opmerkingenCen3(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 3)"""
        return self._opmerkingenCen3.waarde

    @opmerkingenCen3.setter
    def opmerkingenCen3(self, value):
        self._opmerkingenCen3.set_waarde(value, owner=self)

    @property
    def opmerkingenCen4(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 4)"""
        return self._opmerkingenCen4.waarde

    @opmerkingenCen4.setter
    def opmerkingenCen4(self, value):
        self._opmerkingenCen4.set_waarde(value, owner=self)

    @property
    def opmerkingenCen5(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 5)"""
        return self._opmerkingenCen5.waarde

    @opmerkingenCen5.setter
    def opmerkingenCen5(self, value):
        self._opmerkingenCen5.set_waarde(value, owner=self)

    @property
    def opmerkingenCen6(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 6)"""
        return self._opmerkingenCen6.waarde

    @opmerkingenCen6.setter
    def opmerkingenCen6(self, value):
        self._opmerkingenCen6.set_waarde(value, owner=self)

    @property
    def opmerkingenCen7(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 7)"""
        return self._opmerkingenCen7.waarde

    @opmerkingenCen7.setter
    def opmerkingenCen7(self, value):
        self._opmerkingenCen7.set_waarde(value, owner=self)

    @property
    def opmerkingenCen8(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 8)"""
        return self._opmerkingenCen8.waarde

    @opmerkingenCen8.setter
    def opmerkingenCen8(self, value):
        self._opmerkingenCen8.set_waarde(value, owner=self)

    @property
    def opmerkingenCen9(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN 9)"""
        return self._opmerkingenCen9.waarde

    @opmerkingenCen9.setter
    def opmerkingenCen9(self, value):
        self._opmerkingenCen9.set_waarde(value, owner=self)

    @property
    def opmerkingenCen(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen (CEN)"""
        return self._opmerkingenCen.waarde

    @opmerkingenCen.setter
    def opmerkingenCen(self, value):
        self._opmerkingenCen.set_waarde(value, owner=self)

    @property
    def opmerkingenInspectie(self):
        """Definitie nog toe te voegen voor eigenschap Opmerkingen inspectie"""
        return self._opmerkingenInspectie.waarde

    @opmerkingenInspectie.setter
    def opmerkingenInspectie(self, value):
        self._opmerkingenInspectie.set_waarde(value, owner=self)

    @property
    def startCen1(self):
        """Definitie nog toe te voegen voor eigenschap Start (CEN 1)"""
        return self._startCen1.waarde

    @startCen1.setter
    def startCen1(self, value):
        self._startCen1.set_waarde(value, owner=self)

    @property
    def startCen(self):
        """Definitie nog toe te voegen voor eigenschap Start (CEN)"""
        return self._startCen.waarde

    @startCen.setter
    def startCen(self, value):
        self._startCen.set_waarde(value, owner=self)

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
    def opmerkingenCen14(self):
        """Definitie nog toe te voegen voor eigenschap opmerkingen (CEN 14)"""
        return self._opmerkingenCen14.waarde

    @opmerkingenCen14.setter
    def opmerkingenCen14(self, value):
        self._opmerkingenCen14.set_waarde(value, owner=self)

    @property
    def start(self):
        """Definitie nog toe te voegen voor eigenschap start"""
        return self._start.waarde

    @start.setter
    def start(self, value):
        self._start.set_waarde(value, owner=self)

