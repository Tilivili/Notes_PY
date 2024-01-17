import Note
import write_read_notes
import ui

def add_note():
    note = ui.create_note()
    array = write_read_notes.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    write_read_notes.write_file(array, 'a')
    print('Заметка добавлена...')