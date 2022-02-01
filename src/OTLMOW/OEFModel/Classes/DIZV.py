# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DateTimeField import DateTimeField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class DIZV(EMObject):
    """VHS handhaving : Deze installaties meten de tussenafstand van vrachtwagens en verzamelen opnames en gegevens voor politie die eventueel een vaststelling kan opmaken."""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#DIZV'
    label = 'Detectie inbreuken zwaar verkeer'

    def __init__(self):
        super().__init__()

        self._1WaaromNiet = EMAttribuut(field=StringField,
                                        naam='1. Waarom niet?',
                                        label='1. Waarom niet?',
                                        objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#EMObject.1WaaromNiet',
                                        definitie='Definitie nog toe te voegen voor eigenschap Waarom niet?')

        self._5OmschrijfBeschadiging = EMAttribuut(field=StringField,
                                                   naam='5. Omschrijf beschadiging',
                                                   label='5. Omschrijf beschadiging',
                                                   objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#DIZV.5OmschrijfBeschadiging',
                                                   definitie='Definitie nog toe te voegen voor eigenschap Omschrijf beschadiging')

        self._6OmschrijfBeschadiging = EMAttribuut(field=StringField,
                                                   naam='6. Omschrijf beschadiging',
                                                   label='6. Omschrijf beschadiging',
                                                   objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#DIZV.6OmschrijfBeschadiging',
                                                   definitie='Definitie nog toe te voegen voor eigenschap Omschrijf beschadiging')

        self._7OmschrijfBeschadiging = EMAttribuut(field=StringField,
                                                   naam='7. Omschrijf beschadiging',
                                                   label='7. Omschrijf beschadiging',
                                                   objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#DIZV.7OmschrijfBeschadiging',
                                                   definitie='Definitie nog toe te voegen voor eigenschap Omschrijf beschadiging')

        self._9WaaromNiet = EMAttribuut(field=StringField,
                                        naam='9. Waarom niet?',
                                        label='9. Waarom niet?',
                                        objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#DIZV.9WaaromNiet',
                                        definitie='Definitie nog toe te voegen voor eigenschap Waarom niet?')

        self._aanmeldenOnderhoudBijVtc034436331 = EMAttribuut(field=BooleanField,
                                                              naam='Aanmelden onderhoud bij VTC 03/443 63 31',
                                                              label='Aanmelden onderhoud bij VTC 03/443 63 31',
                                                              objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#DIZV.aanmeldenOnderhoudBijVtc034436331',
                                                              definitie='Definitie nog toe te voegen voor eigenschap Aanmelden onderhoud bij VTC 03/443 63 31')

        self._afmeldenOnderhoudBijVtc034436331 = EMAttribuut(field=BooleanField,
                                                             naam='Afmelden onderhoud bij VTC 03/443 63 31',
                                                             label='Afmelden onderhoud bij VTC 03/443 63 31',
                                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#DIZV.afmeldenOnderhoudBijVtc034436331',
                                                             definitie='Definitie nog toe te voegen voor eigenschap Afmelden onderhoud bij VTC 03/443 63 31')

        self._bijkomendeUitlegOpmerkingen = EMAttribuut(field=BooleanField,
                                                        naam='Bijkomende uitleg/opmerkingen',
                                                        label='Bijkomende uitleg/opmerkingen',
                                                        objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#DIZV.bijkomendeUitlegOpmerkingen',
                                                        definitie='Definitie nog toe te voegen voor eigenschap Bijkomende uitleg/opmerkingen')

        self._checkAlgemeneReinheidWegkantkast = EMAttribuut(field=StringField,
                                                             naam='Check algemene reinheid wegkantkast',
                                                             label='Check algemene reinheid wegkantkast',
                                                             objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#DIZV.checkAlgemeneReinheidWegkantkast',
                                                             definitie='Definitie nog toe te voegen voor eigenschap Check algemene reinheid wegkantkast')

        self._checkDataStroomMiv = EMAttribuut(field=StringField,
                                               naam='Check data stroom MIV',
                                               label='Check data stroom MIV',
                                               objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#DIZV.checkDataStroomMiv',
                                               definitie='Definitie nog toe te voegen voor eigenschap Check data stroom MIV')

        self._checkInkomendeSignalenCctv = EMAttribuut(field=StringField,
                                                       naam='Check inkomende signalen CCTV',
                                                       label='Check inkomende signalen CCTV',
                                                       objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#DIZV.checkInkomendeSignalenCctv',
                                                       definitie='Definitie nog toe te voegen voor eigenschap Check inkomende signalen CCTV')

        self._checkVentilatorComputer = EMAttribuut(field=StringField,
                                                    naam='Check ventilator computer',
                                                    label='Check ventilator computer',
                                                    objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#DIZV.checkVentilatorComputer',
                                                    definitie='Definitie nog toe te voegen voor eigenschap Check ventilator computer')

        self._checkenBevestigingspuntenAanCameraS = EMAttribuut(field=StringField,
                                                                naam="Checken bevestigingspunten aan camera's",
                                                                label="Checken bevestigingspunten aan camera's",
                                                                objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#DIZV.checkenBevestigingspuntenAanCameraS',
                                                                definitie="Definitie nog toe te voegen voor eigenschap Checken bevestigingspunten aan camera\'s")

        self._checkenConnectiesAnprCameraS = EMAttribuut(field=StringField,
                                                         naam="Checken connecties ANPR camera's",
                                                         label="Checken connecties ANPR camera's",
                                                         objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#DIZV.checkenConnectiesAnprCameraS',
                                                         definitie="Definitie nog toe te voegen voor eigenschap Checken connecties ANPR camera\'s")

        self._checkenVerankeringBeugelThvDeBrug = EMAttribuut(field=StringField,
                                                              naam='Checken verankering beugel thv de brug',
                                                              label='Checken verankering beugel thv de brug',
                                                              objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#DIZV.checkenVerankeringBeugelThvDeBrug',
                                                              definitie='Definitie nog toe te voegen voor eigenschap Checken verankering beugel thv de brug')

        self._checkenWaterdichteBehuizingRj45Anpr = EMAttribuut(field=StringField,
                                                                naam='Checken waterdichte behuizing RJ 45 ANPR',
                                                                label='Checken waterdichte behuizing RJ 45 ANPR',
                                                                objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#DIZV.checkenWaterdichteBehuizingRj45Anpr',
                                                                definitie='Definitie nog toe te voegen voor eigenschap Checken waterdichte behuizing RJ 45 ANPR')

        self._controleBedrijfstemperatuurComputer = EMAttribuut(field=StringField,
                                                                naam='Controle bedrijfstemperatuur computer',
                                                                label='Controle bedrijfstemperatuur computer',
                                                                objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#DIZV.controleBedrijfstemperatuurComputer',
                                                                definitie='Definitie nog toe te voegen voor eigenschap Controle bedrijfstemperatuur computer')

        self._controleSpanningsomvormers12v = EMAttribuut(field=StringField,
                                                          naam='Controle spanningsomvormers 12V',
                                                          label='Controle spanningsomvormers 12V',
                                                          objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#DIZV.controleSpanningsomvormers12v',
                                                          definitie='Definitie nog toe te voegen voor eigenschap Controle spanningsomvormers 12V')

        self._controleStaatWegkantkast = EMAttribuut(field=BooleanField,
                                                     naam='Controle staat wegkantkast',
                                                     label='Controle staat wegkantkast',
                                                     objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#DIZV.controleStaatWegkantkast',
                                                     definitie='Definitie nog toe te voegen voor eigenschap Controle staat wegkantkast')

        self._controleVerbindingTelematicanetwerk = EMAttribuut(field=StringField,
                                                                naam='Controle verbinding Telematicanetwerk',
                                                                label='Controle verbinding Telematicanetwerk',
                                                                objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#DIZV.controleVerbindingTelematicanetwerk',
                                                                definitie='Definitie nog toe te voegen voor eigenschap Controle verbinding Telematicanetwerk')

        self._controleerDatapakketAnprCameras = EMAttribuut(field=StringField,
                                                            naam='Controleer datapakket ANPR cameras',
                                                            label='Controleer datapakket ANPR cameras',
                                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#DIZV.controleerDatapakketAnprCameras',
                                                            definitie='Definitie nog toe te voegen voor eigenschap Controleer datapakket ANPR cameras')

        self._eindeDizv = EMAttribuut(field=DateTimeField,
                                      naam='Einde (DIZV)',
                                      label='Einde (DIZV)',
                                      objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#DIZV.eindeDizv',
                                      definitie='Definitie nog toe te voegen voor eigenschap Einde (DIZV)')

        self._geefUitlegOpmerkingen = EMAttribuut(field=StringField,
                                                  naam='Geef uitleg/opmerkingen',
                                                  label='Geef uitleg/opmerkingen',
                                                  objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#DIZV.geefUitlegOpmerkingen',
                                                  definitie='Definitie nog toe te voegen voor eigenschap Geef uitleg/opmerkingen')

        self._goedeWerkingSoftwareNagekeken = EMAttribuut(field=BooleanField,
                                                          naam='Goede werking software nagekeken',
                                                          label='Goede werking software nagekeken',
                                                          objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#DIZV.goedeWerkingSoftwareNagekeken',
                                                          definitie='Definitie nog toe te voegen voor eigenschap Goede werking software nagekeken')

        self._reinigingLensEnControleBehuizingCam = EMAttribuut(field=BooleanField,
                                                                naam='Reiniging lens en controle behuizing cam',
                                                                label='Reiniging lens en controle behuizing cam',
                                                                objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#DIZV.reinigingLensEnControleBehuizingCam',
                                                                definitie='Definitie nog toe te voegen voor eigenschap Reiniging lens en controle behuizing cam')

        self._spanningsomvormerVervangen = EMAttribuut(field=BooleanField,
                                                       naam='Spanningsomvormer vervangen?',
                                                       label='Spanningsomvormer vervangen?',
                                                       objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#DIZV.spanningsomvormerVervangen',
                                                       definitie='Definitie nog toe te voegen voor eigenschap Spanningsomvormer vervangen?')

        self._startDizv = EMAttribuut(field=DateTimeField,
                                      naam='Start (DIZV)',
                                      label='Start (DIZV)',
                                      objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#DIZV.startDizv',
                                      definitie='Definitie nog toe te voegen voor eigenschap Start (DIZV)')

        self._stofVerwijderenVanDeComponenten = EMAttribuut(field=BooleanField,
                                                            naam='Stof verwijderen van de componenten',
                                                            label='Stof verwijderen van de componenten',
                                                            objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#DIZV.stofVerwijderenVanDeComponenten',
                                                            definitie='Definitie nog toe te voegen voor eigenschap Stof verwijderen van de componenten')

        self._visueleControleBevestigingsbeugelBrug = EMAttribuut(field=StringField,
                                                                  naam='Visuele controle bevestigingsbeugel brug',
                                                                  label='Visuele controle bevestigingsbeugel brug',
                                                                  objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#DIZV.visueleControleBevestigingsbeugelBrug',
                                                                  definitie='Definitie nog toe te voegen voor eigenschap Visuele controle bevestigingsbeugel brug')

        self._vochtigheidOpBodemKast = EMAttribuut(field=BooleanField,
                                                   naam='Vochtigheid op bodem kast',
                                                   label='Vochtigheid op bodem kast',
                                                   objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#DIZV.vochtigheidOpBodemKast',
                                                   definitie='Definitie nog toe te voegen voor eigenschap Vochtigheid op bodem kast')

        self._invullenVanDeBezoekersfiche = EMAttribuut(field=BooleanField,
                                                        naam='invullen van de bezoekersfiche',
                                                        label='invullen van de bezoekersfiche',
                                                        objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#DIZV.invullenVanDeBezoekersfiche',
                                                        definitie='Definitie nog toe te voegen voor eigenschap invullen van de bezoekersfiche')

    @property
    def 1WaaromNiet(self):
        """Definitie nog toe te voegen voor eigenschap Waarom niet?"""
        return self._1WaaromNiet.waarde

    @1WaaromNiet.setter
    def 1WaaromNiet(self, value):
        self._1WaaromNiet.set_waarde(value, owner=self)

    @property
    def 5OmschrijfBeschadiging(self):
        """Definitie nog toe te voegen voor eigenschap Omschrijf beschadiging"""
        return self._5OmschrijfBeschadiging.waarde

    @5OmschrijfBeschadiging.setter
    def 5OmschrijfBeschadiging(self, value):
        self._5OmschrijfBeschadiging.set_waarde(value, owner=self)

    @property
    def 6OmschrijfBeschadiging(self):
        """Definitie nog toe te voegen voor eigenschap Omschrijf beschadiging"""
        return self._6OmschrijfBeschadiging.waarde

    @6OmschrijfBeschadiging.setter
    def 6OmschrijfBeschadiging(self, value):
        self._6OmschrijfBeschadiging.set_waarde(value, owner=self)

    @property
    def 7OmschrijfBeschadiging(self):
        """Definitie nog toe te voegen voor eigenschap Omschrijf beschadiging"""
        return self._7OmschrijfBeschadiging.waarde

    @7OmschrijfBeschadiging.setter
    def 7OmschrijfBeschadiging(self, value):
        self._7OmschrijfBeschadiging.set_waarde(value, owner=self)

    @property
    def 9WaaromNiet(self):
        """Definitie nog toe te voegen voor eigenschap Waarom niet?"""
        return self._9WaaromNiet.waarde

    @9WaaromNiet.setter
    def 9WaaromNiet(self, value):
        self._9WaaromNiet.set_waarde(value, owner=self)

    @property
    def aanmeldenOnderhoudBijVtc034436331(self):
        """Definitie nog toe te voegen voor eigenschap Aanmelden onderhoud bij VTC 03/443 63 31"""
        return self._aanmeldenOnderhoudBijVtc034436331.waarde

    @aanmeldenOnderhoudBijVtc034436331.setter
    def aanmeldenOnderhoudBijVtc034436331(self, value):
        self._aanmeldenOnderhoudBijVtc034436331.set_waarde(value, owner=self)

    @property
    def afmeldenOnderhoudBijVtc034436331(self):
        """Definitie nog toe te voegen voor eigenschap Afmelden onderhoud bij VTC 03/443 63 31"""
        return self._afmeldenOnderhoudBijVtc034436331.waarde

    @afmeldenOnderhoudBijVtc034436331.setter
    def afmeldenOnderhoudBijVtc034436331(self, value):
        self._afmeldenOnderhoudBijVtc034436331.set_waarde(value, owner=self)

    @property
    def bijkomendeUitlegOpmerkingen(self):
        """Definitie nog toe te voegen voor eigenschap Bijkomende uitleg/opmerkingen"""
        return self._bijkomendeUitlegOpmerkingen.waarde

    @bijkomendeUitlegOpmerkingen.setter
    def bijkomendeUitlegOpmerkingen(self, value):
        self._bijkomendeUitlegOpmerkingen.set_waarde(value, owner=self)

    @property
    def checkAlgemeneReinheidWegkantkast(self):
        """Definitie nog toe te voegen voor eigenschap Check algemene reinheid wegkantkast"""
        return self._checkAlgemeneReinheidWegkantkast.waarde

    @checkAlgemeneReinheidWegkantkast.setter
    def checkAlgemeneReinheidWegkantkast(self, value):
        self._checkAlgemeneReinheidWegkantkast.set_waarde(value, owner=self)

    @property
    def checkDataStroomMiv(self):
        """Definitie nog toe te voegen voor eigenschap Check data stroom MIV"""
        return self._checkDataStroomMiv.waarde

    @checkDataStroomMiv.setter
    def checkDataStroomMiv(self, value):
        self._checkDataStroomMiv.set_waarde(value, owner=self)

    @property
    def checkInkomendeSignalenCctv(self):
        """Definitie nog toe te voegen voor eigenschap Check inkomende signalen CCTV"""
        return self._checkInkomendeSignalenCctv.waarde

    @checkInkomendeSignalenCctv.setter
    def checkInkomendeSignalenCctv(self, value):
        self._checkInkomendeSignalenCctv.set_waarde(value, owner=self)

    @property
    def checkVentilatorComputer(self):
        """Definitie nog toe te voegen voor eigenschap Check ventilator computer"""
        return self._checkVentilatorComputer.waarde

    @checkVentilatorComputer.setter
    def checkVentilatorComputer(self, value):
        self._checkVentilatorComputer.set_waarde(value, owner=self)

    @property
    def checkenBevestigingspuntenAanCameraS(self):
        """Definitie nog toe te voegen voor eigenschap Checken bevestigingspunten aan camera\'s"""
        return self._checkenBevestigingspuntenAanCameraS.waarde

    @checkenBevestigingspuntenAanCameraS.setter
    def checkenBevestigingspuntenAanCameraS(self, value):
        self._checkenBevestigingspuntenAanCameraS.set_waarde(value, owner=self)

    @property
    def checkenConnectiesAnprCameraS(self):
        """Definitie nog toe te voegen voor eigenschap Checken connecties ANPR camera\'s"""
        return self._checkenConnectiesAnprCameraS.waarde

    @checkenConnectiesAnprCameraS.setter
    def checkenConnectiesAnprCameraS(self, value):
        self._checkenConnectiesAnprCameraS.set_waarde(value, owner=self)

    @property
    def checkenVerankeringBeugelThvDeBrug(self):
        """Definitie nog toe te voegen voor eigenschap Checken verankering beugel thv de brug"""
        return self._checkenVerankeringBeugelThvDeBrug.waarde

    @checkenVerankeringBeugelThvDeBrug.setter
    def checkenVerankeringBeugelThvDeBrug(self, value):
        self._checkenVerankeringBeugelThvDeBrug.set_waarde(value, owner=self)

    @property
    def checkenWaterdichteBehuizingRj45Anpr(self):
        """Definitie nog toe te voegen voor eigenschap Checken waterdichte behuizing RJ 45 ANPR"""
        return self._checkenWaterdichteBehuizingRj45Anpr.waarde

    @checkenWaterdichteBehuizingRj45Anpr.setter
    def checkenWaterdichteBehuizingRj45Anpr(self, value):
        self._checkenWaterdichteBehuizingRj45Anpr.set_waarde(value, owner=self)

    @property
    def controleBedrijfstemperatuurComputer(self):
        """Definitie nog toe te voegen voor eigenschap Controle bedrijfstemperatuur computer"""
        return self._controleBedrijfstemperatuurComputer.waarde

    @controleBedrijfstemperatuurComputer.setter
    def controleBedrijfstemperatuurComputer(self, value):
        self._controleBedrijfstemperatuurComputer.set_waarde(value, owner=self)

    @property
    def controleSpanningsomvormers12v(self):
        """Definitie nog toe te voegen voor eigenschap Controle spanningsomvormers 12V"""
        return self._controleSpanningsomvormers12v.waarde

    @controleSpanningsomvormers12v.setter
    def controleSpanningsomvormers12v(self, value):
        self._controleSpanningsomvormers12v.set_waarde(value, owner=self)

    @property
    def controleStaatWegkantkast(self):
        """Definitie nog toe te voegen voor eigenschap Controle staat wegkantkast"""
        return self._controleStaatWegkantkast.waarde

    @controleStaatWegkantkast.setter
    def controleStaatWegkantkast(self, value):
        self._controleStaatWegkantkast.set_waarde(value, owner=self)

    @property
    def controleVerbindingTelematicanetwerk(self):
        """Definitie nog toe te voegen voor eigenschap Controle verbinding Telematicanetwerk"""
        return self._controleVerbindingTelematicanetwerk.waarde

    @controleVerbindingTelematicanetwerk.setter
    def controleVerbindingTelematicanetwerk(self, value):
        self._controleVerbindingTelematicanetwerk.set_waarde(value, owner=self)

    @property
    def controleerDatapakketAnprCameras(self):
        """Definitie nog toe te voegen voor eigenschap Controleer datapakket ANPR cameras"""
        return self._controleerDatapakketAnprCameras.waarde

    @controleerDatapakketAnprCameras.setter
    def controleerDatapakketAnprCameras(self, value):
        self._controleerDatapakketAnprCameras.set_waarde(value, owner=self)

    @property
    def eindeDizv(self):
        """Definitie nog toe te voegen voor eigenschap Einde (DIZV)"""
        return self._eindeDizv.waarde

    @eindeDizv.setter
    def eindeDizv(self, value):
        self._eindeDizv.set_waarde(value, owner=self)

    @property
    def geefUitlegOpmerkingen(self):
        """Definitie nog toe te voegen voor eigenschap Geef uitleg/opmerkingen"""
        return self._geefUitlegOpmerkingen.waarde

    @geefUitlegOpmerkingen.setter
    def geefUitlegOpmerkingen(self, value):
        self._geefUitlegOpmerkingen.set_waarde(value, owner=self)

    @property
    def goedeWerkingSoftwareNagekeken(self):
        """Definitie nog toe te voegen voor eigenschap Goede werking software nagekeken"""
        return self._goedeWerkingSoftwareNagekeken.waarde

    @goedeWerkingSoftwareNagekeken.setter
    def goedeWerkingSoftwareNagekeken(self, value):
        self._goedeWerkingSoftwareNagekeken.set_waarde(value, owner=self)

    @property
    def reinigingLensEnControleBehuizingCam(self):
        """Definitie nog toe te voegen voor eigenschap Reiniging lens en controle behuizing cam"""
        return self._reinigingLensEnControleBehuizingCam.waarde

    @reinigingLensEnControleBehuizingCam.setter
    def reinigingLensEnControleBehuizingCam(self, value):
        self._reinigingLensEnControleBehuizingCam.set_waarde(value, owner=self)

    @property
    def spanningsomvormerVervangen(self):
        """Definitie nog toe te voegen voor eigenschap Spanningsomvormer vervangen?"""
        return self._spanningsomvormerVervangen.waarde

    @spanningsomvormerVervangen.setter
    def spanningsomvormerVervangen(self, value):
        self._spanningsomvormerVervangen.set_waarde(value, owner=self)

    @property
    def startDizv(self):
        """Definitie nog toe te voegen voor eigenschap Start (DIZV)"""
        return self._startDizv.waarde

    @startDizv.setter
    def startDizv(self, value):
        self._startDizv.set_waarde(value, owner=self)

    @property
    def stofVerwijderenVanDeComponenten(self):
        """Definitie nog toe te voegen voor eigenschap Stof verwijderen van de componenten"""
        return self._stofVerwijderenVanDeComponenten.waarde

    @stofVerwijderenVanDeComponenten.setter
    def stofVerwijderenVanDeComponenten(self, value):
        self._stofVerwijderenVanDeComponenten.set_waarde(value, owner=self)

    @property
    def visueleControleBevestigingsbeugelBrug(self):
        """Definitie nog toe te voegen voor eigenschap Visuele controle bevestigingsbeugel brug"""
        return self._visueleControleBevestigingsbeugelBrug.waarde

    @visueleControleBevestigingsbeugelBrug.setter
    def visueleControleBevestigingsbeugelBrug(self, value):
        self._visueleControleBevestigingsbeugelBrug.set_waarde(value, owner=self)

    @property
    def vochtigheidOpBodemKast(self):
        """Definitie nog toe te voegen voor eigenschap Vochtigheid op bodem kast"""
        return self._vochtigheidOpBodemKast.waarde

    @vochtigheidOpBodemKast.setter
    def vochtigheidOpBodemKast(self, value):
        self._vochtigheidOpBodemKast.set_waarde(value, owner=self)

    @property
    def invullenVanDeBezoekersfiche(self):
        """Definitie nog toe te voegen voor eigenschap invullen van de bezoekersfiche"""
        return self._invullenVanDeBezoekersfiche.waarde

    @invullenVanDeBezoekersfiche.setter
    def invullenVanDeBezoekersfiche(self, value):
        self._invullenVanDeBezoekersfiche.set_waarde(value, owner=self)

