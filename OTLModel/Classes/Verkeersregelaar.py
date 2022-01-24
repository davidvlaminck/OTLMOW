# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.DateField import DateField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.DtcExterneReferentie import DtcExterneReferentie
from OTLModel.Datatypes.KlRegelaarRegelaartype import KlRegelaarRegelaartype
from OTLModel.Datatypes.KlVerkeersregelaarCoordinatiewijze import KlVerkeersregelaarCoordinatiewijze
from OTLModel.Datatypes.KlVerkeersregelaarMerk import KlVerkeersregelaarMerk
from OTLModel.Datatypes.KlVerkeersregelaarModelnaam import KlVerkeersregelaarModelnaam
from OTLModel.Datatypes.KlVerkeersregelaarVoltage import KlVerkeersregelaarVoltage
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verkeersregelaar(AIMNaamObject):
    """Een verkeersregelaar is een programmeerbaar toestel dat de verkeerslichten op kruispunten kan regelen overeenkomstig een goedgekeurd verkeersplan. Een verkeersregelaar is bedoeld om het verkeer verkeersafhankelijk te sturen overeenkomstig het gedetecteerde verkeer. Verkeersregelaars kunnen op zichzelf werken of in groep ingeschakeld worden, zodoende op een gecoördineerde wijze de verkeersstromen te verwerken.
Eveneens detecteert een verkeersregelaar defecte onderdelen, van zichzelf of van aangesloten installaties. Afhankelijk van het soort defect stuurt een verkeersregelaar een code uit opdat het euvel hersteld kan worden. Bij welbepaalde defecten worden verkeerslichten uitgeschakeld of op knipperstand gezet.
Volgende documenten zijn specifiek van toepassing voor verkeersregelaars:
*Koninklijk Besluit van 01.12.1975 (wegcode), aangevuld met alle officiële documenten hierover gepubliceerd;
*NBN EN 12675:2000 (Verkeersregelapparaten - Functionele veiligheidseisen);
*NBN EN 50556:2011 (Signalisatie voor wegverkeer;
*NBN EN 12368:2006 (Verkeersregelinstallaties - Verkeerslantaars);
*NBN EN 50293:2012 (Verkeersregelinstallaties - Elektromagnetische compatibiliteit)"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._coordinatiewijze = OTLAttribuut(field=KlVerkeersregelaarCoordinatiewijze,
                                              naam='coordinatiewijze',
                                              label='coördinatiewijze',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.coordinatiewijze',
                                              kardinaliteit_max='*',
                                              definition='Wijze waarop de coördinatie is opgezet en de eventuele rol die de verkeersregelaar hierin speelt.')

        self._externeReferentie = OTLAttribuut(field=DtcExterneReferentie,
                                               naam='externeReferentie',
                                               label='externe referentie',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.externeReferentie',
                                               kardinaliteit_max='*',
                                               definition='Referentie zoals gekend bij een externe partij bv. aannemer, VLCC, ...')

        self._kabelaansluitschema = OTLAttribuut(field=DtcDocument,
                                                 naam='kabelaansluitschema',
                                                 label='kabelaansluitschema',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.kabelaansluitschema',
                                                 definition='Document met het kabelaansluitschema.')

        self._merk = OTLAttribuut(field=KlVerkeersregelaarMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.merk',
                                  definition='Het merk van een verkeersregelaar.')

        self._modelnaam = OTLAttribuut(field=KlVerkeersregelaarModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.modelnaam',
                                       definition='De modelnaam/product range van een verkeersregelaar.')

        self._programmeertool = OTLAttribuut(field=StringField,
                                             naam='programmeertool',
                                             label='programmeertool',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.programmeertool',
                                             definition='Software waarmee de verkeersregelaar geprogrammeerd kan worden.')

        self._regelaartype = OTLAttribuut(field=KlRegelaarRegelaartype,
                                          naam='regelaartype',
                                          label='regelaartype',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.regelaartype',
                                          definition='Onderverdeling in type regelaar volgens het maximale aantal aan te sluiten seingroepen en kruispuntdetectoren.')

        self._technischeDocumentatie = OTLAttribuut(field=DtcDocument,
                                                    naam='technischeDocumentatie',
                                                    label='technische documentatie',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.technischeDocumentatie',
                                                    definition='Document met technische informatie.')

        self._voltageLampen = OTLAttribuut(field=KlVerkeersregelaarVoltage,
                                           naam='voltageLampen',
                                           label='voltage lampen',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.voltageLampen',
                                           definition='Voltage van de verkeerslichten.')

        self._vplanDatum = OTLAttribuut(field=DateField,
                                        naam='vplanDatum',
                                        label='vplan datum',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.vplanDatum',
                                        definition='Datum van het V-plan.')

        self._vplanNummer = OTLAttribuut(field=StringField,
                                         naam='vplanNummer',
                                         label='vplan nummer',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.vplanNummer',
                                         definition='Nummer van het V-plan.')

    @property
    def coordinatiewijze(self):
        """Wijze waarop de coördinatie is opgezet en de eventuele rol die de verkeersregelaar hierin speelt."""
        return self._coordinatiewijze.waarde

    @coordinatiewijze.setter
    def coordinatiewijze(self, value):
        self._coordinatiewijze.set_waarde(value, owner=self)

    @property
    def externeReferentie(self):
        """Referentie zoals gekend bij een externe partij bv. aannemer, VLCC, ..."""
        return self._externeReferentie.waarde

    @externeReferentie.setter
    def externeReferentie(self, value):
        self._externeReferentie.set_waarde(value, owner=self)

    @property
    def kabelaansluitschema(self):
        """Document met het kabelaansluitschema."""
        return self._kabelaansluitschema.waarde

    @kabelaansluitschema.setter
    def kabelaansluitschema(self, value):
        self._kabelaansluitschema.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Het merk van een verkeersregelaar."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam/product range van een verkeersregelaar."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def programmeertool(self):
        """Software waarmee de verkeersregelaar geprogrammeerd kan worden."""
        return self._programmeertool.waarde

    @programmeertool.setter
    def programmeertool(self, value):
        self._programmeertool.set_waarde(value, owner=self)

    @property
    def regelaartype(self):
        """Onderverdeling in type regelaar volgens het maximale aantal aan te sluiten seingroepen en kruispuntdetectoren."""
        return self._regelaartype.waarde

    @regelaartype.setter
    def regelaartype(self, value):
        self._regelaartype.set_waarde(value, owner=self)

    @property
    def technischeDocumentatie(self):
        """Document met technische informatie."""
        return self._technischeDocumentatie.waarde

    @technischeDocumentatie.setter
    def technischeDocumentatie(self, value):
        self._technischeDocumentatie.set_waarde(value, owner=self)

    @property
    def voltageLampen(self):
        """Voltage van de verkeerslichten."""
        return self._voltageLampen.waarde

    @voltageLampen.setter
    def voltageLampen(self, value):
        self._voltageLampen.set_waarde(value, owner=self)

    @property
    def vplanDatum(self):
        """Datum van het V-plan."""
        return self._vplanDatum.waarde

    @vplanDatum.setter
    def vplanDatum(self, value):
        self._vplanDatum.set_waarde(value, owner=self)

    @property
    def vplanNummer(self):
        """Nummer van het V-plan."""
        return self._vplanNummer.waarde

    @vplanNummer.setter
    def vplanNummer(self, value):
        self._vplanNummer.set_waarde(value, owner=self)
