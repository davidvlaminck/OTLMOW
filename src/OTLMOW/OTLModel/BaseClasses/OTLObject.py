import warnings
from datetime import date, time, datetime


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
        for dotnotatie, waarde in self.attributes_by_dotnotatie(asset):
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

    def attributes_by_dotnotatie(self, asset=None):
        var = vars(asset)
        for k, v in vars(asset).items():
            if k in ['_parent', '_geometry_types']:
                continue
            if v.waarde is None:
                continue

            if isinstance(v.waarde, list):
                # kard > 0
                if v.field.waardeObject is not None:
                    if not v.field.waarde_shortcut_applicable:
                        for count, item in enumerate(v.waarde):
                            for k1, v1 in self.attributes_by_dotnotatie(asset=item):
                                yield k1.replace('[]', f'[{count}]'), v1
                    else:
                        for count, item in enumerate(v.waarde.waarde):
                            for k1, v1 in self.attributes_by_dotnotatie(asset=item):
                                yield k1.replace('[]', f'[{count}]'), v1
                else:
                    for count, item in enumerate(v.waarde):
                        yield v.dotnotatie.replace('[]', f'[{count}]'), item
            else:
                if v.field.waardeObject is not None:
                    if not v.field.waarde_shortcut_applicable:
                        for k1, v1 in self.attributes_by_dotnotatie(asset=v.waarde):
                            yield k1, v1
                    else:
                        if v.waarde.waarde is not None:
                            yield v.waarde._waarde.dotnotatie, v.waarde.waarde
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

    def __str__(self, use_dotnotatie=False):
        return f'information about {self.__class__.__name__} {self.__hash__()}:\n' + \
               OTLObjectHelper().build_string_version(asset=self, indent=4, use_dotnotatie=use_dotnotatie)
