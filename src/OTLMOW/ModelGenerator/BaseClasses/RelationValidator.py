import inspect
import warnings

from OTLMOW.OTLModel.BaseClasses.RelatieInteractor import RelatieInteractor
from OTLMOW.OTLModel.Classes.ImplementatieElement.RelatieObject import RelatieObject


class RelationValidator:
    @staticmethod
    def is_valid_relation(source: RelatieInteractor, relation: RelatieObject, target: RelatieInteractor):
        if 'lgc.' in source.typeURI or 'lgc.' in target.typeURI:
            return True

        targets = source._valid_relations[relation.typeURI].keys()
        if target.typeURI in targets:
            deprecated_value = source._valid_relations[relation.typeURI][target.typeURI]
            if deprecated_value != '':
                warnings.warn(
                    message=f'the relation of type {relation.typeURI} between assets of types {source.typeURI} and {target.typeURI} is deprecated since version {deprecated_value}',
                    category=DeprecationWarning)
            return True

        bases = inspect.getmro(type(target))
        for base in bases:
            base_type_uri = RelationValidator._get_member(base, 'typeURI')
            if base_type_uri in targets:
                deprecated_value = source._valid_relations[relation.typeURI][base_type_uri]
                if deprecated_value != '':
                    warnings.warn(
                        message=f'the relation of type {relation.typeURI} between assets of types {source.typeURI} and {target.typeURI} is deprecated since version {deprecated_value}',
                        category=DeprecationWarning)
                return True

        # print(bases)
        return False

    @staticmethod
    def _get_member(obj, name):
        return next(iter([member for _name, member in inspect.getmembers(obj) if name == _name]), None)
