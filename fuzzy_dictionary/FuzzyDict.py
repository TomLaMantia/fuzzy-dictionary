from fuzzywuzzy import process


class FuzzyDict(dict):

    def __init__(self, threshold=75):
        super().__init__()
        self.data = dict()
        self.threshold = threshold

    def __getitem__(self, key):
        keylist = list(self.data.keys())
        if not keylist:
            raise KeyError
        best_match, score = process.extractOne(key, keylist)
        if score > self.threshold:
            return self.data[best_match]
        else:
            raise KeyError

    def __setitem__(self, key, value):
        self.data[key] = value
        return

    def get(self, target, default=None):
        try:
            result = self.__getitem__(target)
        except KeyError:
            result = default
        return result
