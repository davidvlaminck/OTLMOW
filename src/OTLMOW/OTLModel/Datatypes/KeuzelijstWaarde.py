class KeuzelijstWaarde:
    def __init__(self, invulwaarde='', label='', definitie='', objectUri='', status=''):
        self.invulwaarde = invulwaarde
        self.label = label
        self.definitie = definitie
        self.objectUri = objectUri
        self.status = status

    def print(self):
        if self.status == '' or self.status == 'ingebruik':
            return self.invulwaarde

        return self.invulwaarde + ' (' + self.status + ')'
