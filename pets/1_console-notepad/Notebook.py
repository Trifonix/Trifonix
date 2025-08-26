class Notebook:
    def __init__(self):
        self.notes = []
    
    def add_note(self, note):
        self.notes.append(note)
    
    def show_notes(self):
        if not self.notes:
            print('Заметок нет.')
        for i, note in enumerate(self.notes):
            print(f'{i+1}) {note}')

    def delete_note(self, index):
        index -= 1
        if 0 <= index < len(self.notes):
            removed = self.notes.pop(index)
            print(f'Заметка "{removed.title}" была удалена')
        else:
            print('Неверный номер заметки.')

    def sort_notes(self, rev=True):
        self.notes.sort(key=lambda note: note.created_at, reverse=rev)
        print('Заметки отсортированы по дате создания.')
