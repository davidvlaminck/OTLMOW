import warnings
from datetime import date, time, datetime
from typing import Generator, Iterable

from OTLMOW.Facility.DotnotationHelper import DotnotationHelper
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from OTLMOW.OTLModel.Datatypes.DateTimeField import DateTimeField
from OTLMOW.OTLModel.Datatypes.TimeField import TimeField


class OTLObjectHelper:
    @classmethod
    def create_dict_from_asset(cls, asset, waarde_shortcut=False) -> dict:
        return cls.recursive_create_dict_from_asset(asset, waarde_shortcut=waarde_shortcut)

    @classmethod
    def recursive_create_dict_from_asset(cls, asset=None, waarde_shortcut=False):
        if isinstance(asset, list) and not isinstance(asset, dict):
            l = []
            for item in asset:
                dict_item = cls.recursive_create_dict_from_asset(asset=item, waarde_shortcut=waarde_shortcut)
                if dict_item is not None:
                    l.append(dict_item)
            if len(l) > 0:
                return l
            return
        d = {}
        for k, v in vars(asset).items():
            if k in ['_parent', '_geometry_types', '_valid_relations']:
                continue
            if v.waarde is None or v.waarde == []:
                continue

            if v.field.waardeObject is not None: # complex
                if waarde_shortcut and v.field.waarde_shortcut_applicable:
                    if isinstance(v.waarde, list):
                        dict_item = []
                        for item in v.waarde:
                            dict_item.append(item.waarde)
                        if len(dict_item) > 0:
                            d[k[1:]] = dict_item
                    else:
                        dict_item = v.waarde.waarde
                        if dict_item is not None:
                            d[k[1:]] = dict_item
                else:
                    dict_item = cls.recursive_create_dict_from_asset(asset=v.waarde, waarde_shortcut=waarde_shortcut)
                    if dict_item is not None:
                        d[k[1:]] = dict_item
            else:
                if v.field == TimeField:
                    d[k[1:]] = time.strftime(v.waarde, "%H:%M:%S")
                elif v.field == DateField:
                    d[k[1:]] = date.strftime(v.waarde, "%Y-%m-%d")
                elif v.field == DateTimeField:
                    d[k[1:]] = datetime.strftime(v.waarde, "%Y-%m-%d %H:%M:%S")
                else:
                    d[k[1:]] = v.waarde

        if len(d.items()) > 0:
            return d

    @classmethod
    def clean_dict(cls, d) -> dict | None:
        """Recursively remove None values and empty dicts from input dict"""
        if d is None:
            return None
        for k in list(d):
            v = d[k]
            if isinstance(v, dict):
                cls.clean_dict(v)
                if len(v.items()) == 0:
                    del d[k]
            if v is None:
                del d[k]
        return d

    @classmethod
    def build_string_version(cls, asset, indent=4, use_dotnotation=False) -> str:
        lines = []
        for dotnotation, waarde in cls.list_attributes_and_values_by_dotnotation(asset):
            lines.append(f'{dotnotation} : {waarde}')
        return '\n'.join(lines)

    @classmethod
    def make_string_version_from_dict(cls, d, level=0, indent=4) -> []:
        lines = []
        for key in sorted(d.keys()):
            value = d[key]
            if isinstance(value, dict):
                lines.append(' ' * indent * level + f'{key} :')
                lines.extend(cls.make_string_version_from_dict(value, level=level + 1, indent=indent))
            else:
                lines.append(' ' * indent * level + f'{key} : {value}')
        return lines

    @classmethod
    def list_attributes_and_values_by_dotnotation(cls, asset=None, waarde_shortcut: bool = False,
                                                  separator: str = '.',
                                                  cardinality_indicator: str = '[]') -> Iterable[tuple[str, object]]:
        sorted_attributes = sorted(list(vars(asset).items()), key=lambda i: i[0])

        for k, v in sorted_attributes:
            if k in ['_parent', '_geometry_types', '_valid_relations']:
                continue
            if v.waarde is None:
                continue

            if v.field.waardeObject is not None:
                if v.kardinaliteit_max != 1 and v.kardinaliteit_max != '1':
                    lijsten = []
                    for list_item in v.waarde:
                        lijsten.append(
                            list(cls.list_attributes_and_values_by_dotnotation(asset=list_item, waarde_shortcut=waarde_shortcut,
                                                                               separator=separator,
                                                                               cardinality_indicator=cardinality_indicator)))

                    combined_dict = {}
                    for lijst in lijsten:

                        for dotnotation, v in lijst:
                            if dotnotation not in combined_dict:
                                combined_dict[dotnotation] = [v]
                            else:
                                combined_dict[dotnotation].append(v)

                    for dict_k in sorted(combined_dict.keys()):
                        yield dict_k, combined_dict[dict_k]
                else:
                    for k1, v1 in cls.list_attributes_and_values_by_dotnotation(asset=v.waarde, waarde_shortcut=waarde_shortcut,
                                                                                separator=separator,
                                                                                cardinality_indicator=cardinality_indicator):
                        yield k1, v1

            else:
                dotnotation = DotnotationHelper.get_dotnotation(v, waarde_shortcut_applicable=waarde_shortcut,
                                                                separator=separator,
                                                                cardinality_indicator=cardinality_indicator)
                yield dotnotation, v.field.value_default(v.waarde)


class OTLObject:
    def __init__(self):
        if hasattr(self, 'deprecated_version'):
            if self.deprecated_version is not None:
                if hasattr(self, 'typeURI'):
                    warnings.warn(message=f'{self.typeURI} is deprecated since version {self.deprecated_version}',
                                  category=DeprecationWarning)
                else:
                    warnings.warn(message=f'used a class ({self.__class__.__name__}) that is deprecated since version {self.deprecated_version}',
                                  category=DeprecationWarning)

    def create_dict_from_asset(self, waarde_shortcut=False) -> dict:
        return OTLObjectHelper.create_dict_from_asset(asset=self, waarde_shortcut=waarde_shortcut)

    def list_attributes_and_values_by_dotnotation(self, waarde_shortcut: bool = False,
                                                  separator: str = '.',
                                                  cardinality_indicator: str = '[]') -> Iterable[tuple[str, object]]:
        for k, v in OTLObjectHelper.list_attributes_and_values_by_dotnotation(asset=self, waarde_shortcut=waarde_shortcut,
                                                                              separator=separator,
                                                                              cardinality_indicator=cardinality_indicator):
            yield k, v

    def __str__(self, use_dotnotation=False):
        return f'information about {self.__class__.__name__} {self.__hash__()}:\n' + \
               OTLObjectHelper.build_string_version(asset=self, indent=4, use_dotnotation=use_dotnotation)
