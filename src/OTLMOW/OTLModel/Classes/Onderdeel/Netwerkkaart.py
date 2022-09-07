# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.KlNetwerkMerk import KlNetwerkMerk
from OTLMOW.OTLModel.Datatypes.KlNetwerkTechnologie import KlNetwerkTechnologie
from OTLMOW.OTLModel.Datatypes.KlNetwerkkaartModelnaam import KlNetwerkkaartModelnaam
from OTLMOW.OTLModel.Datatypes.StringField import StringField
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Netwerkkaart(AIMNaamObject, PuntGeometrie):
    """Component van een NetwerkElement om specifieke verbindingen te leggen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkkaart'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort')

        self._beschrijvingFabrikant = OTLAttribuut(field=StringField,
                                                   naam='beschrijvingFabrikant',
                                                   label='beschrijving fabrikant',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkkaart.beschrijvingFabrikant',
                                                   definition='Bijkomende specificaties over het apparaat of onderdeel type van de fabrikant.',
                                                   owner=self)

        self._merk = OTLAttribuut(field=KlNetwerkMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkkaart.merk',
                                  definition='Merk waarmee de fabrikant de netwerkkaart identificeert.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlNetwerkkaartModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkkaart.modelnaam',
                                       definition='Modelnaam waarmee de fabrikant dit type toestel identificeert.',
                                       owner=self)

        self._serienummer = OTLAttribuut(field=StringField,
                                         naam='serienummer',
                                         label='serienummer',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkkaart.serienummer',
                                         definition='Unieke identificatiecode van het toestel, toegekend door de fabrikant.',
                                         owner=self)

        self._softwareVersie = OTLAttribuut(field=StringField,
                                            naam='softwareVersie',
                                            label='software versie',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkkaart.softwareVersie',
                                            definition='Identificatie van de softwareversie die op dit apparaat of onderdeel geladen is. Dit kan ook een firmwareversie zijn.',
                                            owner=self)

        self._technologie = OTLAttribuut(field=KlNetwerkTechnologie,
                                         naam='technologie',
                                         label='technologie',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkkaart.technologie',
                                         definition='Intern gebruikte netwerk protocol.',
                                         owner=self)

    @property
    def beschrijvingFabrikant(self):
        """Bijkomende specificaties over het apparaat of onderdeel type van de fabrikant."""
        return self._beschrijvingFabrikant.get_waarde()

    @beschrijvingFabrikant.setter
    def beschrijvingFabrikant(self, value):
        self._beschrijvingFabrikant.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Merk waarmee de fabrikant de netwerkkaart identificeert."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """Modelnaam waarmee de fabrikant dit type toestel identificeert."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def serienummer(self):
        """Unieke identificatiecode van het toestel, toegekend door de fabrikant."""
        return self._serienummer.get_waarde()

    @serienummer.setter
    def serienummer(self, value):
        self._serienummer.set_waarde(value, owner=self)

    @property
    def softwareVersie(self):
        """Identificatie van de softwareversie die op dit apparaat of onderdeel geladen is. Dit kan ook een firmwareversie zijn."""
        return self._softwareVersie.get_waarde()

    @softwareVersie.setter
    def softwareVersie(self, value):
        self._softwareVersie.set_waarde(value, owner=self)

    @property
    def technologie(self):
        """Intern gebruikte netwerk protocol."""
        return self._technologie.get_waarde()

    @technologie.setter
    def technologie(self, value):
        self._technologie.set_waarde(value, owner=self)
