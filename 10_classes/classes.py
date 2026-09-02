"""Classes: creating custom data types with attributes and behavior."""


# A basic class
class Student:
    def __init__(self, name, track):
        # __init__ runs when a new object is created
        self.name = name           # attribute
        self.track = track         # attribute
        self.completed_modules = 0

    def complete_module(self):
        # a method — a function that belongs to the class
        self.completed_modules += 1
        print(f"{self.name} completed a module ({self.completed_modules} total)")

    def summary(self):
        return f"{self.name} — {self.track} — {self.completed_modules} modules done"


# Creating (instantiating) objects from the class
ada = Student("Ada", "AI/ML")
grace = Student("Grace", "Data Science")

ada.complete_module()
ada.complete_module()
print(ada.summary())
print(grace.summary())  # each instance keeps its own state


# Inheritance — building a more specific class on top of a general one
class MentoredStudent(Student):
    def __init__(self, name, track, mentor):
        super().__init__(name, track)  # reuse the parent's __init__
        self.mentor = mentor

    def summary(self):
        # overriding the parent's method
        base = super().summary()
        return f"{base} — mentored by {self.mentor}"


bootcamp_student = MentoredStudent("Ada", "AI/ML", mentor="Claude")
bootcamp_student.complete_module()
print(bootcamp_student.summary())

# isinstance checks
print(isinstance(bootcamp_student, Student))        # True — inherits from Student
print(isinstance(bootcamp_student, MentoredStudent))  # True


# When to use a class vs just a dict/function:
# - Use a class when you have data (attributes) AND behavior (methods) that
#   belong together and you'll create multiple instances of it.
# - If it's just data with no behavior, a dict (or dataclass) is often enough.
# - If it's just a stateless operation, a plain function is enough.
