# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from src.OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from src.OTLMOW.OTLModel.Datatypes.DtcBeschermingVraatschade import DtcBeschermingVraatschade
from src.OTLMOW.OTLModel.Datatypes.KlAantalBoompalen import KlAantalBoompalen
from src.OTLMOW.OTLModel.Datatypes.KlBeschermingMaaischade import KlBeschermingMaaischade
from src.OTLMOW.OTLModel.Datatypes.KlBoomVerankering import KlBoomVerankering
from src.OTLMOW.OTLModel.Datatypes.KlBoomVerankeringtype import KlBoomVerankeringtype
from src.OTLMOW.OTLModel.Datatypes.KlGroeiplaatsverbetering import KlGroeiplaatsverbetering
from src.OTLMOW.OTLModel.Datatypes.KlMateriaalBeschermingVraatschade import KlMateriaalBeschermingVraatschade
from src.OTLMOW.OTLModel.Datatypes.KlPlantmaatHoogte import KlPlantmaatHoogte
from src.OTLMOW.OTLModel.Datatypes.KlPlantmaatOmtrek import KlPlantmaatOmtrek
from src.OTLMOW.OTLModel.Datatypes.KlVegetatieWortel import KlVegetatieWortel
from src.OTLMOW.OTLModel.Datatypes.KlVormAanleveringHoutigeVegetatie import KlVormAanleveringHoutigeVegetatie


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAanlegBoomvormWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._beschermingVraatschade = OTLAttribuut(field=DtcBeschermingVraatschade,
                                                    naam='beschermingVraatschade',
                                                    label='bescherming vraatschade',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAanlegBoomvorm.beschermingVraatschade',
                                                    usagenote='Attribuut uit gebruik sinds versie 2.0.0 ',
                                                    deprecated_version='2.0.0',
                                                    definition='Bescherming van de stam tegen knaagdieren.')

        self._boompaalconstructie = OTLAttribuut(field=KlAantalBoompalen,
                                                 naam='boompaalconstructie',
                                                 label='boompaalconstructie',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAanlegBoomvorm.boompaalconstructie',
                                                 definition='Een constructie om de wortels van de aangeplante boom vast te zetten of te fixeren met oa. palen.')

        self._groeiplaatsverbetering = OTLAttribuut(field=KlGroeiplaatsverbetering,
                                                    naam='groeiplaatsverbetering',
                                                    label='groeiplaatsverbetering',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAanlegBoomvorm.groeiplaatsverbetering',
                                                    definition='De techniek waarmee de groeiplaats wordt verbeterd met als doel de levensverwachting en de conditie van de vegetatie te verbeteren.')

        self._heeftBoomplaat = OTLAttribuut(field=BooleanField,
                                            naam='heeftBoomplaat',
                                            label='heeft boomplaat',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAanlegBoomvorm.heeftBoomplaat',
                                            definition='Boomplaten worden aangebracht rond de stam van bomen, bosgoed en heesters en eventueel vastgezet met piketten. Ze hebben een centrale opening en een rechte snede, zodat ze op eenvoudige wijze rond de planten kunnen aangebracht worden.')

        self._heeftWortelgeleidingwortelwering = OTLAttribuut(field=BooleanField,
                                                              naam='heeftWortelgeleidingwortelwering',
                                                              label='heeft wortelgeleiding wortelwering',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAanlegBoomvorm.heeftWortelgeleidingwortelwering',
                                                              definition='Aanduiding of de boom wortelwering heeft. Wortelgeleiding en –wering moet voorkomen dat boomwortels het trottoir, de middenberm, het fietspad, de rijweg, andere wegverhardingen en leidingstelsels beschadigen.')

        self._maaischadeBescherming = OTLAttribuut(field=KlBeschermingMaaischade,
                                                   naam='maaischadeBescherming',
                                                   label='maaischade bescherming',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAanlegBoomvorm.maaischadeBescherming',
                                                   definition='Bescherming van de stam tegen maaimachines.')

        self._plantmaatHoogte = OTLAttribuut(field=KlPlantmaatHoogte,
                                             naam='plantmaatHoogte',
                                             label='plantmaat hoogte',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAanlegBoomvorm.plantmaatHoogte',
                                             definition='De hoogte in meter gemeten van de stamvoet tot de top met een minimum en maximum waarde.')

        self._plantmaatOmtrek = OTLAttribuut(field=KlPlantmaatOmtrek,
                                             naam='plantmaatOmtrek',
                                             label='plantmaat omtrek',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAanlegBoomvorm.plantmaatOmtrek',
                                             definition='De stamomtrek in centimeter  (gemeten op 1 m boven het maaiveld) met een minimum en maximum waarde.')

        self._verankering = OTLAttribuut(field=KlBoomVerankering,
                                         naam='verankering',
                                         label='verankering',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAanlegBoomvorm.verankering',
                                         definition='Aanduiding of de boom onder- of bovengronds gefixeerd wordt.')

        self._verankeringstype = OTLAttribuut(field=KlBoomVerankeringtype,
                                              naam='verankeringstype',
                                              label='verankeringstype',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAanlegBoomvorm.verankeringstype',
                                              definition='Het materiaal van de fixering of verankering.')

        self._vormAanlevering = OTLAttribuut(field=KlVormAanleveringHoutigeVegetatie,
                                             naam='vormAanlevering',
                                             label='vorm aanlevering',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAanlegBoomvorm.vormAanlevering',
                                             definition='De wijze waarop het plantgoed wordt aangeleverd.')

        self._vraatschadeBescherming = OTLAttribuut(field=KlMateriaalBeschermingVraatschade,
                                                    naam='vraatschadeBescherming',
                                                    label='vraatschade bescherming',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAanlegBoomvorm.vraatschadeBescherming',
                                                    definition='Bescherming van de stam tegen knaagdieren.')

        self._wortelAanplant = OTLAttribuut(field=KlVegetatieWortel,
                                            naam='wortelAanplant',
                                            label='wortel aanplant',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAanlegBoomvorm.wortelAanplant',
                                            definition='De manier van levering en aanplanting van het wortelgestel van de boom of plant.')

    @property
    def beschermingVraatschade(self):
        """Bescherming van de stam tegen knaagdieren."""
        return self._beschermingVraatschade.waarde

    @beschermingVraatschade.setter
    def beschermingVraatschade(self, value):
        self._beschermingVraatschade.set_waarde(value, owner=self._parent)

    @property
    def boompaalconstructie(self):
        """Een constructie om de wortels van de aangeplante boom vast te zetten of te fixeren met oa. palen."""
        return self._boompaalconstructie.waarde

    @boompaalconstructie.setter
    def boompaalconstructie(self, value):
        self._boompaalconstructie.set_waarde(value, owner=self._parent)

    @property
    def groeiplaatsverbetering(self):
        """De techniek waarmee de groeiplaats wordt verbeterd met als doel de levensverwachting en de conditie van de vegetatie te verbeteren."""
        return self._groeiplaatsverbetering.waarde

    @groeiplaatsverbetering.setter
    def groeiplaatsverbetering(self, value):
        self._groeiplaatsverbetering.set_waarde(value, owner=self._parent)

    @property
    def heeftBoomplaat(self):
        """Boomplaten worden aangebracht rond de stam van bomen, bosgoed en heesters en eventueel vastgezet met piketten. Ze hebben een centrale opening en een rechte snede, zodat ze op eenvoudige wijze rond de planten kunnen aangebracht worden."""
        return self._heeftBoomplaat.waarde

    @heeftBoomplaat.setter
    def heeftBoomplaat(self, value):
        self._heeftBoomplaat.set_waarde(value, owner=self._parent)

    @property
    def heeftWortelgeleidingwortelwering(self):
        """Aanduiding of de boom wortelwering heeft. Wortelgeleiding en –wering moet voorkomen dat boomwortels het trottoir, de middenberm, het fietspad, de rijweg, andere wegverhardingen en leidingstelsels beschadigen."""
        return self._heeftWortelgeleidingwortelwering.waarde

    @heeftWortelgeleidingwortelwering.setter
    def heeftWortelgeleidingwortelwering(self, value):
        self._heeftWortelgeleidingwortelwering.set_waarde(value, owner=self._parent)

    @property
    def maaischadeBescherming(self):
        """Bescherming van de stam tegen maaimachines."""
        return self._maaischadeBescherming.waarde

    @maaischadeBescherming.setter
    def maaischadeBescherming(self, value):
        self._maaischadeBescherming.set_waarde(value, owner=self._parent)

    @property
    def plantmaatHoogte(self):
        """De hoogte in meter gemeten van de stamvoet tot de top met een minimum en maximum waarde."""
        return self._plantmaatHoogte.waarde

    @plantmaatHoogte.setter
    def plantmaatHoogte(self, value):
        self._plantmaatHoogte.set_waarde(value, owner=self._parent)

    @property
    def plantmaatOmtrek(self):
        """De stamomtrek in centimeter  (gemeten op 1 m boven het maaiveld) met een minimum en maximum waarde."""
        return self._plantmaatOmtrek.waarde

    @plantmaatOmtrek.setter
    def plantmaatOmtrek(self, value):
        self._plantmaatOmtrek.set_waarde(value, owner=self._parent)

    @property
    def verankering(self):
        """Aanduiding of de boom onder- of bovengronds gefixeerd wordt."""
        return self._verankering.waarde

    @verankering.setter
    def verankering(self, value):
        self._verankering.set_waarde(value, owner=self._parent)

    @property
    def verankeringstype(self):
        """Het materiaal van de fixering of verankering."""
        return self._verankeringstype.waarde

    @verankeringstype.setter
    def verankeringstype(self, value):
        self._verankeringstype.set_waarde(value, owner=self._parent)

    @property
    def vormAanlevering(self):
        """De wijze waarop het plantgoed wordt aangeleverd."""
        return self._vormAanlevering.waarde

    @vormAanlevering.setter
    def vormAanlevering(self, value):
        self._vormAanlevering.set_waarde(value, owner=self._parent)

    @property
    def vraatschadeBescherming(self):
        """Bescherming van de stam tegen knaagdieren."""
        return self._vraatschadeBescherming.waarde

    @vraatschadeBescherming.setter
    def vraatschadeBescherming(self, value):
        self._vraatschadeBescherming.set_waarde(value, owner=self._parent)

    @property
    def wortelAanplant(self):
        """De manier van levering en aanplanting van het wortelgestel van de boom of plant."""
        return self._wortelAanplant.waarde

    @wortelAanplant.setter
    def wortelAanplant(self, value):
        self._wortelAanplant.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAanlegBoomvorm(ComplexField, AttributeInfo):
    """Complex datatype om alle eigenschappen van de aanleg van een opgaande boom onder 1 noemer te houden."""
    naam = 'DtcAanlegBoomvorm'
    label = 'aanleg boomvorm'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAanlegBoomvorm'
    definition = 'Complex datatype om alle eigenschappen van de aanleg van een opgaande boom onder 1 noemer te houden.'
    waardeObject = DtcAanlegBoomvormWaarden

    def __str__(self):
        return ComplexField.__str__(self)

