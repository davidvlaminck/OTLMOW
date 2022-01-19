﻿class UnionWaarden:
    def clear_other_props(self, prop_name):
        other_prop_keys = list(filter(lambda x: x != prop_name, vars(self).keys()))
        for key in other_prop_keys:
            attr = getattr(self, key)
            if attr.field.waardeObject is not None and not attr.field._uses_waarde_object:
                attr = getattr(self, key[1:])
                setattr(attr, 'waarde', None)
            else:
                setattr(self, key[1:], None)