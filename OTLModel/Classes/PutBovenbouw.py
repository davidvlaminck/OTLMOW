# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KlDekselKaderType import KlDekselKaderType
from OTLModel.Datatypes.KlDekselKlasse import KlDekselKlasse
from OTLModel.Datatypes.KlDekselMateriaal import KlDekselMateriaal
from OTLModel.Datatypes.KlDekselRegeling import KlDekselRegeling
from OTLModel.Datatypes.KlDekselVergrendeling import KlDekselVergrendeling
from OTLModel.Datatypes.KlRioleringVorm import KlRioleringVorm
from OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class PutBovenbouw(AIMObject):
    """Een combinatie van het riooldeksel met de kader en de regeling."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._breedte = OTLAttribuut(field=KwantWrdInCentimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.breedte',
                                     definition='Breedte-afmeting van het deksel in centimeter. Bij vierkante en cirkelvormige deksels is deze waarde gelijk aan de hoogte.')

        self._dekselklasse = OTLAttribuut(field=KlDekselKlasse,
                                          naam='dekselklasse',
                                          label='dekselklasse',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.dekselklasse',
                                          definition='Bepaalt de mate waarin het deksel van de bovenbouw belast kan worden door voertuigen.')

        self._dekselvorm = OTLAttribuut(field=KlRioleringVorm,
                                        naam='dekselvorm',
                                        label='dekselvorm',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.dekselvorm',
                                        definition='Bepaalt de vorm van het deksel.')

        self._hoogte = OTLAttribuut(field=KwantWrdInCentimeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.hoogte',
                                    definition='Hoogte-afmeting van het deksel in centimeter. Bij vierkante en cirkelvormige deksels is deze waarde gelijk aan de breedte.')

        self._isAfgesloten = OTLAttribuut(field=BooleanField,
                                          naam='isAfgesloten',
                                          label='is afgesloten',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.isAfgesloten',
                                          definition='Bepaling of de afsluitinrichting vergrendeld is of niet.')

        self._isScharnierend = OTLAttribuut(field=BooleanField,
                                            naam='isScharnierend',
                                            label='is scharnierend',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.isScharnierend',
                                            definition='Het deksel is al of niet bevestigd met een scharnier.')

        self._isWaterdichtVergrendeld = OTLAttribuut(field=BooleanField,
                                                     naam='isWaterdichtVergrendeld',
                                                     label='Is waterdicht vergrendeld',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.isWaterdichtVergrendeld',
                                                     definition='Geeft aan of de bovenbouw al dan niet waterdicht vergrendeld is zodat het water zich niet boven de bovenbouw kan begeven.')

        self._kader = OTLAttribuut(field=KlDekselKaderType,
                                   naam='kader',
                                   label='kader',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.kader',
                                   definition='Bepaalt het type van het dekselkader.')

        self._materiaal = OTLAttribuut(field=KlDekselMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.materiaal',
                                       definition='Het materiaal waaruit het deksel van de bovenbouw is vervaardigd.')

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.oppervlakte',
                                         definition='De oppervlakte van het zichtbare deel van de bovenbouw in vierkante meter.')

        self._regeling = OTLAttribuut(field=KlDekselRegeling,
                                      naam='regeling',
                                      label='regeling',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.regeling',
                                      definition='De wijze hoe de regeling van het deksel is uitgevoerd.')

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.technischeFiche',
                                             usagenote='Bestanden van het type xlsx of pdf.',
                                             kardinaliteit_max='*',
                                             definition='De technische fiche van de bovenbouw.')

        self._vergrendeling = OTLAttribuut(field=KlDekselVergrendeling,
                                           naam='vergrendeling',
                                           label='vergrendeling',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.vergrendeling',
                                           definition='Bepaalt het type sleutel voor het ontgrendelen van het deksel.')

    @property
    def breedte(self):
        """Breedte-afmeting van het deksel in centimeter. Bij vierkante en cirkelvormige deksels is deze waarde gelijk aan de hoogte."""
        return self._breedte.waarde

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def dekselklasse(self):
        """Bepaalt de mate waarin het deksel van de bovenbouw belast kan worden door voertuigen."""
        return self._dekselklasse.waarde

    @dekselklasse.setter
    def dekselklasse(self, value):
        self._dekselklasse.set_waarde(value, owner=self)

    @property
    def dekselvorm(self):
        """Bepaalt de vorm van het deksel."""
        return self._dekselvorm.waarde

    @dekselvorm.setter
    def dekselvorm(self, value):
        self._dekselvorm.set_waarde(value, owner=self)

    @property
    def hoogte(self):
        """Hoogte-afmeting van het deksel in centimeter. Bij vierkante en cirkelvormige deksels is deze waarde gelijk aan de breedte."""
        return self._hoogte.waarde

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self)

    @property
    def isAfgesloten(self):
        """Bepaling of de afsluitinrichting vergrendeld is of niet."""
        return self._isAfgesloten.waarde

    @isAfgesloten.setter
    def isAfgesloten(self, value):
        self._isAfgesloten.set_waarde(value, owner=self)

    @property
    def isScharnierend(self):
        """Het deksel is al of niet bevestigd met een scharnier."""
        return self._isScharnierend.waarde

    @isScharnierend.setter
    def isScharnierend(self, value):
        self._isScharnierend.set_waarde(value, owner=self)

    @property
    def isWaterdichtVergrendeld(self):
        """Geeft aan of de bovenbouw al dan niet waterdicht vergrendeld is zodat het water zich niet boven de bovenbouw kan begeven."""
        return self._isWaterdichtVergrendeld.waarde

    @isWaterdichtVergrendeld.setter
    def isWaterdichtVergrendeld(self, value):
        self._isWaterdichtVergrendeld.set_waarde(value, owner=self)

    @property
    def kader(self):
        """Bepaalt het type van het dekselkader."""
        return self._kader.waarde

    @kader.setter
    def kader(self, value):
        self._kader.set_waarde(value, owner=self)

    @property
    def materiaal(self):
        """Het materiaal waaruit het deksel van de bovenbouw is vervaardigd."""
        return self._materiaal.waarde

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def oppervlakte(self):
        """De oppervlakte van het zichtbare deel van de bovenbouw in vierkante meter."""
        return self._oppervlakte.waarde

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)

    @property
    def regeling(self):
        """De wijze hoe de regeling van het deksel is uitgevoerd."""
        return self._regeling.waarde

    @regeling.setter
    def regeling(self, value):
        self._regeling.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """De technische fiche van de bovenbouw."""
        return self._technischeFiche.waarde

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def vergrendeling(self):
        """Bepaalt het type sleutel voor het ontgrendelen van het deksel."""
        return self._vergrendeling.waarde

    @vergrendeling.setter
    def vergrendeling(self, value):
        self._vergrendeling.set_waarde(value, owner=self)
