from abc import abstractmethod


# TODO rename (and validator)
class RelatieInteractor:
    typeURI = ''
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def add_valid_relation(self, relation: str, target: str, deprecated: str = ''):
        if relation not in self._valid_relations:
            self._valid_relations[relation] = {}
        self._valid_relations[relation][target] = deprecated

    @abstractmethod
    def __init__(self):
        self._valid_relations = {}
