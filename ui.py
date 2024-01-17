from add_notes import add_note
from change_notes import change_note
from del_notes import del_note
from print_notes import print_note_id
from print_notes import print_note_all
from print_notes import print_note_date
import Note

def create_note():
    title = input('Введите Название заметки: ')
    body = input('Введите Описание заметки: ')
    return Note.Note(title=title, body=body)

def start_menu():
    command = None
    while command != 7:
        command = int(input("Начало работы.Выберите опцию:\n"
                      "1. Добавить заметку\n"
                      "2. Удалить заметку\n"
                      "3. Изменить заметку\n"
                      "4. Показать заметку по id\n"
                      "5. Показать заметку по дате создания/изменения\n"
                      "6. Показать все заметки\n"
                      "7. Выход\n"
                      "Введите номер команды: "))
        if command == 1:
            add_note()
        elif command == 2:
            del_note()
        elif command == 3:
            change_note()
        elif command == 4:
            print_note_id()  
        elif command == 5:
            print_note_date()      
        elif command == 6:
            print_note_all()   
    print("Завершение работы.")