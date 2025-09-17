class School:
    def __init__(self):
        self.middle_school = []
        self.high_school = []

    def get_middle_school(self):
        return self.middle_school

    def get_high_school(self):
        return self.high_school

    def get_high_school_class(self, name):
        for class_year in self.high_school:
            if class_year == name:
                return class_year

        # Class name not found.
        return None

    def get_middle_school_class(self, name):
        for class_year in self.middle_school:
            if class_year == name:
                return class_year

        # Class name not found.
        return None

    def set_class(self, name):
        pass


