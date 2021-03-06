import ratemyprofessor

from professor import Professor


class Course:
    def __init__(self, name, code, cores) -> None:
        self.name = name
        self.code = code
        self.cores = cores

        # TODO: gets hairy with different sections
        # self.time = None
        # self.location = None
        # self.status = None
        # self.index = None

        self.professors = []

    def __eq__(self, other):
        return self.code == other.code

    def __hash__(self):
        return hash(self.code)

    def __str__(self) -> str:
        return self.name + ": " + self.core
