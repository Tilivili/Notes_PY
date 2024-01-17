import Note
import write_read_notes

def del_note():
    id = input('Введите id заметки: ')
    array = write_read_notes.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            array.remove(notes)
            print('Заметка удалена...')
    if logic == True:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    write_read_notes.write_file(array, 'a')        