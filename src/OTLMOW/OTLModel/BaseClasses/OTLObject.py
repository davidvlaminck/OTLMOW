import warnings
from datetime import date, time, datetime

from OTLMOW.Facility.Exceptions.HasNoDotNotatieException import HasNoDotNotatieException


class OTLObjectHelper:
    def create_dict_from_asset(self, asset):
        return self.clean_dict(self.recursive_create_dict_from_asset(asset))

    def recursive_create_dict_from_asset(self, asset=None):
        if isinstance(asset, list) and not isinstance(asset, dict):
            l = []
            for item in asset:
                l.append(self.recursive_create_dict_from_asset(asset=item))
            return l
        d = {}
        for k, v in vars(asset).items():
            if k in ['_parent', '_geometry_types']:
                continue
            if v.waarde is not None and v.waarde != []:
                if v.field.waardeObject is not None:
                    if v.field._uses_waarde_object:
                        d[k[1:]] = self.recursive_create_dict_from_asset(asset=v.waarde)
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

        return self.clean_dict(d)

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

    def build_string_version(self, asset, indent=4) -> str:
        lines = []
        asset_dict = self.create_dict_from_asset(asset)
        lines.extend(
            self.make_string_version_from_dict(
                d=asset_dict,
                level=1,
                indent=indent))

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

    def attributes_by_dotnotatie(self, asset=None):
        for k, v in sorted(vars(asset).items()):
            if k in ['_parent', '_geometry_types']:
                continue
            if v.waarde is None:
                continue
            if v.field.waardeObject is not None:
                if v.field._uses_waarde_object:
                    for k1, v1 in self.attributes_by_dotnotatie(asset=v.waarde):
                        yield k1, v1
                else:
                    if v.waarde.waarde is not None:
                        yield v.waarde._waarde.dotnotatie, v.waarde.waarde
            else:
                if isinstance(v.waarde, list):
                    if len(v.waarde) > 0:
                        yield v.dotnotatie, '|'.join(v.waarde)
                else:
                    yield v.dotnotatie, v.waarde


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

    def attributes_by_dotnotatie(self):
        for k, v in OTLObjectHelper().attributes_by_dotnotatie(asset=self):
            yield k, v

    def __str__(self):
        return f'information about {self.__class__.__name__} {self.__hash__()}:\n' + \
               OTLObjectHelper().build_string_version(asset=self, indent=4)
