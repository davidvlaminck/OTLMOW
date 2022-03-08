class GenericHelper:
    @classmethod
    def remove_duplicates_in_iterable_based_on_property(cls, iterable: iter, prop: str) -> []:
        done = []
        new_iterable = []
        for item in iterable:
            item_prop = getattr(item, prop)
            if item_prop not in done:
                done.append(item_prop)
                new_iterable.append(item)
        return new_iterable


