import Note
import write_read_notes

def print_note_id():
    id = input('Введите id заметки: ')
    array = write_read_notes.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            print(Note.Note.map_note(notes))
    if logic == True:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    write_read_notes.write_file(array, 'a')         

def print_note_all():
    logic = True
    array = write_read_notes.read_file()
    for notes in array:
        logic = False
        print(Note.Note.map_note(notes))
    if logic == True:
        print('Нет ни одной заметки...')

def print_note_date():
    logic = True
    array = write_read_notes.read_file()
    date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        logic = False
        if date in Note.Note.get_date(notes):
                print(Note.Note.map_note(notes))
    if logic == True:
        print('Нет ни одной заметки...')
