import openbabel

class ChemStructure:
    def __init__(self, question: str, answer: str, structure: str):
        self.question = question
        self.answer = answer
        self.structure = structure
        self.smiles = self.to_smiles()
        
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
        self.smiles = self.to_smiles()

    def get_structure(self) -> str:
        return self.structure

    def to_smiles(self) -> str:
    """
    Converts the molecule structure to SMILES format.
    """
    obConversion = openbabel.OBConversion()
    obConversion.SetInAndOutFormats("jcp", "smi")
    obMol = openbabel.OBMol()
    obConversion.ReadString(obMol, self.structure)
    smiles = obConversion.WriteString(obMol).strip()
    return smiles

    @classmethod
    def from_smiles(cls, question: str, answer: str, smiles: str) -> "ChemStructure":
        """Creates a ChemStructure object from a question prompt, the correct answer, and a SMILES string."""
        obConversion = openbabel.OBConversion()
        obConversion.SetInAndOutFormats("smi", "jcp")
        obMol = openbabel.OBMol()
        obConversion.ReadString(obMol, smiles)
        jcp = obConversion.WriteString(obMol)
        return cls(question, answer, jcp)
        
    def to_jcp(self) -> str:
        obConversion = openbabel.OBConversion()
        obConversion.SetInAndOutFormats("smi", "jcp")
        obMol = openbabel.OBMol()
        obConversion.ReadString(obMol, self.structure)
        jcp = obConversion.WriteString(obMol)
        return jcp

    def is_correct(self, user_input: str) -> bool:
        obConversion = openbabel.OBConversion()
        obConversion.SetInAndOutFormats("smi", "smi")
        obMol = openbabel.OBMol()
        obConversion.ReadString(obMol, self.answer)
        correct_answer_smi = obConversion.WriteString(obMol).strip()
        obConversion.ReadString(obMol, user_input)
        user_input_smi = obConversion.WriteString(obMol).strip()
        return correct_answer_smi == user_input_smi
