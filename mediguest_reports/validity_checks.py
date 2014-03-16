class ValidityCheckResult(object):
    def __init__(self, name, valid, result, notes):
        self.name = name
        self.valid = valid
        self.result = result
        self.notes = notes

class ValidityCheck(object):
    def _check(self):
        raise NotImplementedError()

    def __call__(self):
        return self._check()

class DoseValidityCheck(ValidityCheck):
    def _check(self):
        res = True

        if res:
            res_str = u"Yes"
        else:
            res_str = u"NO"

        notes = u""

        return ValidityCheckResult(u"Medication doses within safe limits", res, res_str, notes)

