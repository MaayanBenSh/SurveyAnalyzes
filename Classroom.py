class Classroom:
    def __init__(self, name):
        self.serveys = []
        self.name = name

    def get_serveys(self):
        return self.serveys

    def add_servey(self, servey):
        self.serveys.append(servey)

