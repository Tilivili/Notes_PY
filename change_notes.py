import Note
import write_read_notes
import ui

def change_note():
    id = input('Введите id заметки: ')
    array = write_read_notes.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            note = ui.create_note()
            Note.Note.set_title(notes, note.get_title())
            Note.Note.set_body(notes, note.get_body())
            Note.Note.set_date(notes)
            print('Заметка изменена...')
    if logic == True:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    write_read_notes.write_file(array, 'a')
