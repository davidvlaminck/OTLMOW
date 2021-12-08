class KwantWrd:
    def __setattr__(self, key, value):
        if key == "waarde":
            self.waarde.waarde = value
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, name):
        if name == "waarde":
            return self.waarde.waarde
        else:
            return object.__getattribute__(self, name)

    def __init__(self, waarde=None):
        if waarde is not None:
            self.waarde = waarde