import json

from OTLMOW.Facility.AssetFactory import AssetFactory
from OTLMOW.Facility.FileFormats.DictDecoder import DictDecoder
from OTLMOW.OEFModel.OEFClassLoader import OEFClassLoader
from OTLMOW.OTLModel.BaseClasses.OTLObject import OTLObject


class EMInfraDecoder:
    def decodeGraph(self, responseString):
        dict_obj = json.loads(responseString)
        lijst = []
        for obj in dict_obj["@graph"]:
            lijst.append(self.decode_json_object(obj))

        return lijst

    def decode_object(self, objString):
        obj = json.loads(objString)
        return self.decode_json_object(obj)

    def decode_json_object(self, obj) -> OTLObject:
        typeURI = next(value for key, value in obj.items() if 'typeURI' in key)

        if 'https://wegenenverkeer.data.vlaanderen.be/ns' in typeURI:
            instance = AssetFactory().dynamic_create_instance_from_uri(typeURI)
        else:
            instance = OEFClassLoader().dynamic_create_instance_from_uri(typeURI)

        if instance is None:
            raise NotImplementedError(f'Could not create a class for {typeURI}')

        # trim dict
        trimmed_dict = self.trim_json_ld_dict(obj)

        # make changes to dict (geometry + tz etc)
        self.best_effort_fill_geometry_in_instance(instance, trimmed_dict)

        # then apply dict (json encoder)
        for key, value in trimmed_dict.items():
            if key.startswith(
                    '@') or 'typeURI' in key or value == '' or value == [] or key == 'bron' or key == 'doel' or ':' in key:
                continue

            DictDecoder.set_value_by_dictitem(instance, key, value, True)

        return instance

    @staticmethod
    def best_effort_fill_geometry_in_instance(instance, trimmed_dict):
        if not hasattr(instance, 'geometry'):
            return

        if 'geo:log' in trimmed_dict and len(trimmed_dict['geo:log']) > 0:
            geo_logs = trimmed_dict['geo:log']
            if len(geo_logs) > 1:
                geo_logs = sorted(geo_logs, key=lambda g: int(g['geo:niveau']), reverse=True)
            highest_geo_log = geo_logs[0]
            if highest_geo_log['geo:geometrie'] is not None and len(highest_geo_log['geo:geometrie'].items()) > 0:
                wktstring = list(highest_geo_log['geo:geometrie'].values())[0]
                if 'Z(' in wktstring:
                    wktstring = wktstring.replace('Z(', 'Z (')
                instance.geometry = wktstring

        if instance.geometry is None:
            if 'loc:geometrie' in trimmed_dict and trimmed_dict['loc:geometrie'] is None:
                instance.geometry = trimmed_dict['loc:geometrie']

        if instance.geometry is None:
            if 'loc:puntlocatie' in trimmed_dict and 'loc:puntgeometrie' in trimmed_dict['loc:puntlocatie'] and \
                    'loc:lambert72' in trimmed_dict['loc:puntlocatie']['loc:puntgeometrie']:
                coords = trimmed_dict['loc:puntlocatie']['loc:puntgeometrie']['loc:lambert72']
                wktstring = f"POINT Z ({coords['loc:xcoordinaat']} {coords['loc:ycoordinaat']} {coords['loc:zcoordinaat']})"
                instance.geometry = wktstring

    @classmethod
    def trim_json_ld_dict(cls, value) -> dict | list | object:
        if isinstance(value, dict):
            for k, v in list(value.items()):
                if '.' not in k:
                    continue
                if v is not None:
                    v = cls.trim_json_ld_dict(v)
                ns = ''
                if ':' in k:
                    ns = k.split(':')[0]
                if ns == '':
                    value[k.split('.')[-1]] = v
                else:
                    value[ns + ':' + k.split('.')[-1]] = v
                value.pop(k)
            return value

        if isinstance(value, list):
            for index, item in enumerate(value):
                if isinstance(item, dict):
                    value[index] = cls.trim_json_ld_dict(item)

            return value

        return cls.trim_keuzelijst_from_jsonld(value)

    @classmethod
    def trim_keuzelijst_from_jsonld(cls, value):
        if isinstance(value, str) and (
                'https://wegenenverkeer.data.vlaanderen.be/id/concept' in value or 'https://geo.data.wegenenverkeer.be/id/concept' in value):
            return value.split('/')[-1]
        return value
