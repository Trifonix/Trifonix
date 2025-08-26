from Note import Note
from Notebook import Notebook

'''
first_note = Note('Моя заметка', 'Описание моей заметки')
second_note = Note('Моя заметка2', 'Описание моей заметки2')

first_notebook = Notebook()

first_notebook.add_note(first_note)
first_notebook.add_note(second_note)

first_notebook.show_notes()
'''

notebook = Notebook()

while True:
    print('\nМеню:')
    print('1. Добавить заметку')
    print('2. Показать все заметки')
    print('3. Удалить заметку')
    print('4. Выйти')

    choice = input('Выберите действие: ')

    if '1' == choice:
        title = input('Введите название заметки: ')
        content = input('Введите описание заметки: ')
        note = Note(title, content)
        notebook.add_note(note)
        print('Заметка добавлена!')
    
    elif '2' == choice:
        print('\nВсе заметки:')
        notebook.show_notes()

    elif '3' == choice:
        note_for_delete = input('\nВведите номер заметки для удаления: ')
        notebook.delete_note(int(note_for_delete))

    elif '4' == choice:
        print('Выход...')
        break

    else:
        print('Неверный выбор, попробуйте снова.')
