class UnionWaarden:
    def clear_other_props(self, prop_name):
        other_prop_keys = list(filter(lambda x: x != prop_name, vars(self).keys()))
        for key in other_prop_keys:
            setattr(self, key[1:], None)