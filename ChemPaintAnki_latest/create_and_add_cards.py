from aqt import mw
from aqt.qt import QDialog, QVBoxLayout, QLabel, QLineEdit, QDialogButtonBox
from anki.notes import Note

def create_chemstructure_card() -> ChemStructureCard:
    # Create a dialog window to collect the information
    dialog = QDialog(mw)
    dialog.setWindowTitle("Create ChemStructure Card")
    layout = QVBoxLayout(dialog)

    # Prompt the user for the necessary information
    question_label = QLabel("Question:")
    question_input = QLineEdit()
    layout.addWidget(question_label)
    layout.addWidget(question_input)

    structure_label = QLabel("Structure:")
    structure_input = QLineEdit()
    layout.addWidget(structure_label)
    layout.addWidget(structure_input)

    answer_label = QLabel("Answer:")
    answer_input = QLineEdit()
    layout.addWidget(answer_label)
    layout.addWidget(answer_input)

    button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    button_box.accepted.connect(dialog.accept)
    button_box.rejected.connect(dialog.reject)
    layout.addWidget(button_box)

    # Show the dialog and wait for user input
    if dialog.exec_() == QDialog.Accepted:
        # Retrieve the user's input
        question = question_input.text()
        structure = structure_input.text()
        answer = answer_input.text()

        # Create a new ChemStructureCard object
        card = ChemStructureCard(question, structure, answer)

        return card
    else:
        return None


def edit_chemstructure_card(card: ChemStructureCard) -> ChemStructureCard:
    # Create a dialog window to edit the information
    dialog = QDialog(mw)
    dialog.setWindowTitle("Edit ChemStructure Card")
    layout = QVBoxLayout(dialog)

    # Display the current information
    question_label = QLabel(f"Question: {card.question}")
    layout.addWidget(question_label)

    structure_label = QLabel(f"Structure: {card.structure}")
    layout.addWidget(structure_label)

    answer_label = QLabel(f"Answer: {card.answer}")
    layout.addWidget(answer_label)

    # Prompt the user for the updated information
    question_input = QLineEdit()
    structure_input = QLineEdit()
    answer_input = QLineEdit()

    layout.addWidget(question_input)
    layout.addWidget(structure_input)
    layout.addWidget(answer_input)

    button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    button_box.accepted.connect(dialog.accept)
    button_box.rejected.connect(dialog.reject)
    layout.addWidget(button_box)

    # Show the dialog and wait for user input
    if dialog.exec_() == QDialog.Accepted:
        # Retrieve the user's input
        question = question_input.text() or card.question
        structure = structure_input.text() or card.structure
        answer = answer_input.text() or card.answer

        # Update the card with the new information
        card.set_question(question)
        card.set_structure(structure)
        card.set_answer(answer)

        return card
    else:
        return None
