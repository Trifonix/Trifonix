class Notebook:
    def __init__(self):
        self.notes = []
    
    def add_note(self, note):
        self.notes.append(f"{note.title}: {note.content} [{note.created_at}]")
    
    def show_notes(self):
        for note in self.notes:
            print(note)
