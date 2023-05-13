from anki.notes import Note
from aqt import mw

class ChemStructureCard:
    # Define constants for note type name and field names
    MODEL_NAME = "ChemPaintAnki"
    QUESTION_FIELD_NAME = "Question"
    STRUCTURE_FIELD_NAME = "Structure"
    ANSWER_FIELD_NAME = "Answer"

    def __init__(self, question: str, structure: str, answer: str):
        self.question = question
        self.structure = structure
        self.answer = answer

    def __repr__(self):
        return f"ChemStructureCard({self.question}, {self.structure}, {self.answer})"

    def set_question(self, question: str) -> None:
        self.question = question

    def get_question(self) -> str:
        return self.question

    def set_answer(self, answer: str) -> None:
        self.answer = answer

    def get_answer(self) -> str:
        return self.answer

    def set_structure(self, structure: str) -> None:
        self.structure = structure

    def get_structure(self) -> str:
        return self.structure

    def to_note(self) -> Note:
        # Create a new note of the ChemPaintAnki model
        note = Note()
        note.model()['name'] = self.MODEL_NAME

        # Set the question, structure, and answer fields of the note
        note[self.QUESTION_FIELD_NAME] = self.question
        note[self.STRUCTURE_FIELD_NAME] = self.structure
        note[self.ANSWER_FIELD_NAME] = self.answer

        return note

    @classmethod
    def from_note(cls, note: Note) -> "ChemStructureCard":
        # Extract the question, structure, and answer from the note
        question = note[cls.QUESTION_FIELD_NAME]
        structure = note[cls.STRUCTURE_FIELD_NAME]
        answer = note[cls.ANSWER_FIELD_NAME]

        # Create a new ChemStructureCard object
        return cls(question, structure, answer)

    def is_correct(self, user_input: str) -> bool:
        return self.answer == user_input
