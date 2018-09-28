class Fact(object):
    def __init__(self, measure, attributes: list):
        self.measure = measure
        self.attributes = attributes

    def __str__(self):
        return self.measure + " -> " + str(self.attributes)