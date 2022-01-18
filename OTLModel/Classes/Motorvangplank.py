# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AfschermendeConstructie import AfschermendeConstructie
from OTLModel.Datatypes.KlLEACSchokindexMVP import KlLEACSchokindexMVP
from OTLModel.Datatypes.KlLEACSnelheidsklasse import KlLEACSnelheidsklasse
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Motorvangplank(AfschermendeConstructie, AttributeInfo):
    """Een constructie geïnstalleerd aan een geleideconstructie of in de onmiddellijke omgeving ervan,met als doel de ernst van een botsing van een motorrijder met de geleideconstructie te reduceren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Motorvangplank'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AfschermendeConstructie.__init__(self)
        AttributeInfo.__init__(self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Motorvangplank.lengte',
                                    definition='De lengte van de motorvangplank in meter.')

        self._schokindexMvp = OTLAttribuut(field=KlLEACSchokindexMVP,
                                           naam='schokindexMvp',
                                           label='schokindex motorvangplank',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Motorvangplank.schokindexMvp',
                                           definition='Head injury criterium (HIC) van een motorvangplank.')

        self._snelheidsklasse = OTLAttribuut(field=KlLEACSnelheidsklasse,
                                             naam='snelheidsklasse',
                                             label='snelheidsklasse',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Motorvangplank.snelheidsklasse',
                                             definition='De snelheid waarmee de testen uitgevoerd worden en of deze plaatsvinden op een continu of discontinu (niet in gebruik bij AWV) systeem.')

        self._werkingsbreedteMvpwd = OTLAttribuut(field=KwantWrdInMeter,
                                                  naam='werkingsbreedteMvpwd',
                                                  label='werkingsbreedte mvpwd',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Motorvangplank.werkingsbreedteMvpwd',
                                                  definition='De afstand tussen de voorkant van het onvervormd systeem tot de maximale dynamische laterale positie van elk onderdeel van het systeem.')

    @property
    def lengte(self):
        """De lengte van de motorvangplank in meter."""
        return self._lengte.waarde

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def schokindexMvp(self):
        """Head injury criterium (HIC) van een motorvangplank."""
        return self._schokindexMvp.waarde

    @schokindexMvp.setter
    def schokindexMvp(self, value):
        self._schokindexMvp.set_waarde(value, owner=self)

    @property
    def snelheidsklasse(self):
        """De snelheid waarmee de testen uitgevoerd worden en of deze plaatsvinden op een continu of discontinu (niet in gebruik bij AWV) systeem."""
        return self._snelheidsklasse.waarde

    @snelheidsklasse.setter
    def snelheidsklasse(self, value):
        self._snelheidsklasse.set_waarde(value, owner=self)

    @property
    def werkingsbreedteMvpwd(self):
        """De afstand tussen de voorkant van het onvervormd systeem tot de maximale dynamische laterale positie van elk onderdeel van het systeem."""
        return self._werkingsbreedteMvpwd.waarde

    @werkingsbreedteMvpwd.setter
    def werkingsbreedteMvpwd(self, value):
        self._werkingsbreedteMvpwd.set_waarde(value, owner=self)
