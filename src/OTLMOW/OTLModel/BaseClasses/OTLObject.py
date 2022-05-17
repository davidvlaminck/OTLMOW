import warnings
from datetime import date, time, datetime

from OTLMOW.Facility.DotnotatieHelper import DotnotatieHelper


class OTLObjectHelper:
    def create_dict_from_asset(self, asset):
        return self.clean_dict(self.recursive_create_dict_from_asset(asset))

    def recursive_create_dict_from_asset(self, asset=None):
        if isinstance(asset, list) and not isinstance(asset, dict):
            l = []
            for item in asset:
                dict_item = self.recursive_create_dict_from_asset(asset=item)
                if dict_item is not None:
                    l.append(dict_item)
            if len(l) > 0:
                return l
            return
        d = {}
        for k, v in vars(asset).items():
            if k in ['_parent', '_geometry_types']:
                continue
            if v.waarde is not None and v.waarde != []:
                if v.field.waardeObject is not None:
                    if v.field.waarde_shortcut_applicable:
                        dict_item = self.recursive_create_dict_from_asset(asset=v.waarde)
                        if dict_item is not None:
                            d[k[1:]] = dict_item
                    else:
                        d[k[1:]] = v.waarde.waarde
                else:
                    if isinstance(v.waarde, time):
                        d[k[1:]] = time.strftime(v.waarde, "%H:%M:%S")
                    elif isinstance(v.waarde, date):
                        d[k[1:]] = date.strftime(v.waarde, "%Y-%m-%d")
                    elif isinstance(v.waarde, datetime):
                        d[k[1:]] = datetime.strftime(v.waarde, "%Y-%m-%d %H:%M:%S")
                    else:
                        d[k[1:]] = v.waarde

        d = self.clean_dict(d)
        if len(d.items()) > 0:
            return d

    def clean_dict(self, d):
        """Recursively remove None values and empty dicts from input dict"""
        for k in list(d):
            v = d[k]
            if isinstance(v, dict):
                self.clean_dict(v)
                if len(v.items()) == 0:
                    del d[k]
            if v is None:
                del d[k]
        return d

    def build_string_version(self, asset, indent=4, use_dotnotatie=False) -> str:
        lines = []
        for dotnotatie, waarde in self.list_attributes_and_values_by_dotnotatie(asset):
            lines.append(f'{dotnotatie} : {waarde}')
        return '\n'.join(lines)

    def make_string_version_from_dict(self, d, level=0, indent=4) -> []:
        lines = []
        for key in sorted(d.keys()):
            value = d[key]
            if isinstance(value, dict):
                lines.append(' ' * indent * level + f'{key} :')
                lines.extend(self.make_string_version_from_dict(value, level=level + 1, indent=indent))
            else:
                lines.append(' ' * indent * level + f'{key} : {value}')
        return lines

    def list_attributes_and_values_by_dotnotatie(self, asset=None, waarde_shortcut: bool = False):
        sorted_attributes = sorted(list(vars(asset).items()), key=lambda i: i[0])

        for k, v in sorted_attributes:
            if k in ['_parent', '_geometry_types']:
                continue
            if v.waarde is None:
                continue

            if v.field.waardeObject is not None:
                if v.kardinaliteit_max != '1':
                    lijsten = []
                    for list_item in v.waarde:
                        lijsten.append(
                            list(self.list_attributes_and_values_by_dotnotatie(asset=list_item,
                                                                               waarde_shortcut=waarde_shortcut)))

                    combined_dict = {}
                    for lijst in lijsten:

                        for dotnotatie, v in lijst:
                            if dotnotatie not in combined_dict:
                                combined_dict[dotnotatie] = [v]
                            else:
                                combined_dict[dotnotatie].append(v)

                    for dict_k in sorted(combined_dict.keys()):
                        yield dict_k, combined_dict[dict_k]
                else:
                    for k1, v1 in self.list_attributes_and_values_by_dotnotatie(asset=v.waarde, waarde_shortcut=waarde_shortcut):
                        yield k1, v1

            else:
                dotnotatie = DotnotatieHelper.get_dotnotatie(v, waarde_shortcut_applicable=waarde_shortcut)
                yield dotnotatie, v.waarde

class OTLObject:
    def __init__(self):
        if hasattr(self, 'deprecated_version'):
            if self.deprecated_version is not None:
                if hasattr(self, 'typeURI'):
                    warnings.warn(message=f'{self.typeURI} is deprecated since version {self.deprecated_version}',
                                  category=DeprecationWarning)
                else:
                    warnings.warn(message=f'used a class that is deprecated since version {self.deprecated_version}',
                                  category=DeprecationWarning)

    def create_dict_from_asset(self, exclude_nested_attributes=False):
        return OTLObjectHelper().recursive_create_dict_from_asset(asset=self)

    def list_attributes_and_values_by_dotnotatie(self, waarde_shortcut: bool = False):
        for k, v in OTLObjectHelper().list_attributes_and_values_by_dotnotatie(asset=self,
                                                                               waarde_shortcut=waarde_shortcut):
            yield k, v

    def __str__(self, use_dotnotatie=False):
        return f'information about {self.__class__.__name__} {self.__hash__()}:\n' + \
               OTLObjectHelper().build_string_version(asset=self, indent=4, use_dotnotatie=use_dotnotatie)
