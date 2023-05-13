from chemstructure_methods import ChemStructure

class ChemStructureCard:
    def __init__(self, question: str, structure: str, answer: str):
        self.question = question
        self.structure = ChemStructure(question, answer, structure)
        self.answer = answer

    def __repr__(self):
        return f'ChemStructureCard({self.question}, {self.structure}, {self.answer})'

    def set_question(self, question: str) -> None:
        self.question = question
        self.structure.set_question(question)

    def get_question(self) -> str:
        return self.question

    def set_answer(self, answer: str) -> None:
        self.answer = answer
        self.structure.answer = answer

    def get_answer(self) -> str:
        return self.answer

    def set_structure(self, structure: str) -> None:
        self.structure.set_structure(structure)

    def get_structure(self) -> str:
        return self.structure.get_structure()

    def to_jcp(self) -> str:
        return self.structure.to_jcp()

    def is_correct(self, user_input: str) -> bool:
        return self.structure.is_correct(user_input)