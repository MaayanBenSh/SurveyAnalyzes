import Classroom

class Class:
    def __init__(self):
        # Max => 15 classrooms
        self.classrooms = []

    def get_classrooms(self):
        return self.classrooms

    def set_classrooms(self):
        for classrooms in range(15):
            self.classrooms.append(Classroom.Classroom(f"classroom{classrooms+1}"))

    def get_classroom(self, name):
        for classroom in self.classrooms:
            if classroom.name == name:
                return classroom

        # Classroom name not found.
        return None

