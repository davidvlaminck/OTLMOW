# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.DtcBeschermingVraatschade import DtcBeschermingVraatschade
from OTLModel.Datatypes.KlBeschermingMaaischade import KlBeschermingMaaischade
from OTLModel.Datatypes.KlMateriaalBeschermingVraatschade import KlMateriaalBeschermingVraatschade
from OTLModel.Datatypes.KlPlantmaatHoogte import KlPlantmaatHoogte
from OTLModel.Datatypes.KlPlantmaatOmtrek import KlPlantmaatOmtrek
from OTLModel.Datatypes.KlVegetatiePlantverband import KlVegetatiePlantverband
from OTLModel.Datatypes.KlVegetatieWortel import KlVegetatieWortel
from OTLModel.Datatypes.KlVormAanleveringHoutigeVegetatie import KlVormAanleveringHoutigeVegetatie
from OTLModel.Datatypes.NonNegIntegerField import NonNegIntegerField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcHoutigeAanlegWaarden(AttributeInfo):
    def __init__(self):
        self._beschermingVraatschade = OTLAttribuut(field=DtcBeschermingVraatschade,
                                                    naam='beschermingVraatschade',
                                                    label='bescherming vraatschade',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.beschermingVraatschade',
                                                    usagenote_nl='Attribuut uit gebruik sinds versie 2.0.0',
                                                    deprecated_version='2.0.0',
                                                    definition='Bescherming van de stam tegen knaagdieren.')

        self._heeftBoomplaat = OTLAttribuut(field=BooleanField,
                                            naam='heeftBoomplaat',
                                            label='heeft boomplaat',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.heeftBoomplaat',
                                            definition='Boomplaten worden aangebracht rond de stam van bomen, bosgoed en heesters en eventueel vastgezet met piketten. Ze hebben een centrale opening en een rechte snede, zodat ze op eenvoudige wijze rond de planten kunnen aangebracht worden.')

        self._heeftHaagsteun = OTLAttribuut(field=BooleanField,
                                            naam='heeftHaagsteun',
                                            label='heeft haagsteun',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.heeftHaagsteun',
                                            definition='Duidt op de aanezigheid van een constructie van palen en bedrading die haagbeplanting ondersteunt.')

        self._heeftWortelgeleidingwortelwering = OTLAttribuut(field=BooleanField,
                                                              naam='heeftWortelgeleidingwortelwering',
                                                              label='heeft wortelgeleiding-wortelwering',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.heeftWortelgeleidingwortelwering',
                                                              definition='Wortelgeleiding en –wering moet voorkomen dat boomwortels het trottoir, de middenberm, het fietspad, de rijweg, andere wegverhardingen en leidingstelsels beschadigen. Het heeft als doel om boomwortels naar beneden te leiden, waar ze onder een obstakel verder kunnen groeien.')

        self._maaischadeBescherming = OTLAttribuut(field=KlBeschermingMaaischade,
                                                   naam='maaischadeBescherming',
                                                   label='maaischade bescherming',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.maaischadeBescherming',
                                                   definition='Bescherming van de stam tegen maaimachines.')

        self._plantafstand = OTLAttribuut(field=NonNegIntegerField,
                                          naam='plantafstand',
                                          label='plantafstand',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.plantafstand',
                                          definition='Aantal planten per lopende meter.')

        self._plantdichtheid = OTLAttribuut(field=NonNegIntegerField,
                                            naam='plantdichtheid',
                                            label='plantdichtheid',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.plantdichtheid',
                                            definition='Aantal planten per vierkante meter.')

        self._plantmaatHoogte = OTLAttribuut(field=KlPlantmaatHoogte,
                                             naam='plantmaatHoogte',
                                             label='plantmaat hoogte',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.plantmaatHoogte',
                                             definition='De hoogte van de plant in cm gemeten tussen een minimum en maximum waarde.')

        self._plantmaatOmtrek = OTLAttribuut(field=KlPlantmaatOmtrek,
                                             naam='plantmaatOmtrek',
                                             label='plantmaat omtrek',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.plantmaatOmtrek',
                                             definition='De stamomtrek in centimeter  (gemeten op 1 m boven het maaiveld) met een minimum en maximum waarde.')

        self._plantverband = OTLAttribuut(field=KlVegetatiePlantverband,
                                          naam='plantverband',
                                          label='plantverband',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.plantverband',
                                          definition='De wijze waarop de planten zijn geschikt.')

        self._vormAanlevering = OTLAttribuut(field=KlVormAanleveringHoutigeVegetatie,
                                             naam='vormAanlevering',
                                             label='vorm aanlevering',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.vormAanlevering',
                                             definition='De wijze waarop het plantgoed wordt aangeleverd.')

        self._vraatschadeBescherming = OTLAttribuut(field=KlMateriaalBeschermingVraatschade,
                                                    naam='vraatschadeBescherming',
                                                    label='vraatschade bescherming',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.vraatschadeBescherming',
                                                    definition='Bescherming van de stam tegen knaagdieren.')

        self._wortel = OTLAttribuut(field=KlVegetatieWortel,
                                    naam='wortel',
                                    label='wortel',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.wortel',
                                    definition='De manier van levering en aanplanting van het wortelgestel van de boom of plant.')

    @property
    def beschermingVraatschade(self):
        """Bescherming van de stam tegen knaagdieren."""
        return self._beschermingVraatschade.waarde

    @beschermingVraatschade.setter
    def beschermingVraatschade(self, value):
        self._beschermingVraatschade.set_waarde(value)

    @property
    def heeftBoomplaat(self):
        """Boomplaten worden aangebracht rond de stam van bomen, bosgoed en heesters en eventueel vastgezet met piketten. Ze hebben een centrale opening en een rechte snede, zodat ze op eenvoudige wijze rond de planten kunnen aangebracht worden."""
        return self._heeftBoomplaat.waarde

    @heeftBoomplaat.setter
    def heeftBoomplaat(self, value):
        self._heeftBoomplaat.set_waarde(value)

    @property
    def heeftHaagsteun(self):
        """Duidt op de aanezigheid van een constructie van palen en bedrading die haagbeplanting ondersteunt."""
        return self._heeftHaagsteun.waarde

    @heeftHaagsteun.setter
    def heeftHaagsteun(self, value):
        self._heeftHaagsteun.set_waarde(value)

    @property
    def heeftWortelgeleidingwortelwering(self):
        """Wortelgeleiding en –wering moet voorkomen dat boomwortels het trottoir, de middenberm, het fietspad, de rijweg, andere wegverhardingen en leidingstelsels beschadigen. Het heeft als doel om boomwortels naar beneden te leiden, waar ze onder een obstakel verder kunnen groeien."""
        return self._heeftWortelgeleidingwortelwering.waarde

    @heeftWortelgeleidingwortelwering.setter
    def heeftWortelgeleidingwortelwering(self, value):
        self._heeftWortelgeleidingwortelwering.set_waarde(value)

    @property
    def maaischadeBescherming(self):
        """Bescherming van de stam tegen maaimachines."""
        return self._maaischadeBescherming.waarde

    @maaischadeBescherming.setter
    def maaischadeBescherming(self, value):
        self._maaischadeBescherming.set_waarde(value)

    @property
    def plantafstand(self):
        """Aantal planten per lopende meter."""
        return self._plantafstand.waarde

    @plantafstand.setter
    def plantafstand(self, value):
        self._plantafstand.set_waarde(value)

    @property
    def plantdichtheid(self):
        """Aantal planten per vierkante meter."""
        return self._plantdichtheid.waarde

    @plantdichtheid.setter
    def plantdichtheid(self, value):
        self._plantdichtheid.set_waarde(value)

    @property
    def plantmaatHoogte(self):
        """De hoogte van de plant in cm gemeten tussen een minimum en maximum waarde."""
        return self._plantmaatHoogte.waarde

    @plantmaatHoogte.setter
    def plantmaatHoogte(self, value):
        self._plantmaatHoogte.set_waarde(value)

    @property
    def plantmaatOmtrek(self):
        """De stamomtrek in centimeter  (gemeten op 1 m boven het maaiveld) met een minimum en maximum waarde."""
        return self._plantmaatOmtrek.waarde

    @plantmaatOmtrek.setter
    def plantmaatOmtrek(self, value):
        self._plantmaatOmtrek.set_waarde(value)

    @property
    def plantverband(self):
        """De wijze waarop de planten zijn geschikt."""
        return self._plantverband.waarde

    @plantverband.setter
    def plantverband(self, value):
        self._plantverband.set_waarde(value)

    @property
    def vormAanlevering(self):
        """De wijze waarop het plantgoed wordt aangeleverd."""
        return self._vormAanlevering.waarde

    @vormAanlevering.setter
    def vormAanlevering(self, value):
        self._vormAanlevering.set_waarde(value)

    @property
    def vraatschadeBescherming(self):
        """Bescherming van de stam tegen knaagdieren."""
        return self._vraatschadeBescherming.waarde

    @vraatschadeBescherming.setter
    def vraatschadeBescherming(self, value):
        self._vraatschadeBescherming.set_waarde(value)

    @property
    def wortel(self):
        """De manier van levering en aanplanting van het wortelgestel van de boom of plant."""
        return self._wortel.waarde

    @wortel.setter
    def wortel(self, value):
        self._wortel.set_waarde(value)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcHoutigeAanleg(ComplexField, AttributeInfo):
    """Complex datatype dat de aanleg van houtige vegetatie beschrijft."""
    naam = 'DtcHoutigeAanleg'
    label = 'Houtige aanleg'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg'
    definition = 'Complex datatype dat de aanleg van houtige vegetatie beschrijft.'
    waardeObject = DtcHoutigeAanlegWaarden

    def __str__(self):
        return ComplexField.__str__(self)

