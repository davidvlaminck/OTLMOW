from abc import ABC

from ModelGenerator.BaseClasses.AbstractRelatieInteractor import AbstractRelatieInteractor
from ModelGenerator.BaseClasses.GeldigeRelatie import GeldigeRelatie


class RelatieInteractor(AbstractRelatieInteractor):
    geldige_relaties: []

    def __init__(self):
        self.geldige_relaties = []

    def add_geldige_relatie(self, relatie, doel, richting):
        self.geldige_relaties.append(GeldigeRelatie(relatie, doel, richting))


