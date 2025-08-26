from Note import Note
from Notebook import Notebook

first_note = Note('Моя заметка', 'Описание моей заметки')

first_notebook = Notebook()
first_notebook.add_note(first_note)
first_notebook.show_notes()
