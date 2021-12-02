from abc import ABC

from ModelGenerator.BaseClasses.AbstractRelatieInteractor import AbstractRelatieInteractor
from ModelGenerator.BaseClasses.GeldigeRelatie import GeldigeRelatie
from ModelGenerator.BaseClasses.ListField import ListField


class RelatieInteractor(AbstractRelatieInteractor):
    geldige_relaties: ListField() = []

    def add_geldige_relatie(self, relatie, doel, richting):
        self.geldige_relaties.append(GeldigeRelatie(relatie, doel, richting))


