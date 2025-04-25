from .sorter import Sorter
from .reader import Reader
from .writer import Writer
import os
import time

VERSION = "0.1.1"
AUTHOR = "Sekret"
ERRORS = {

}

def cls():
    os.system('cls')


class Console:
    """ Класс-интерфейс для взаимодействия пользователя с журналом """

    def __init__(self):
        self.sorter = Sorter()
        self.reader = Reader()
        self.writer = Writer()

    def start(self):
        start_status = self.welcome()
        while True:
            cls()
            print("> запись - новая запись\n> журнал - вывод записей (возможна фильтрация)\n> выход - выход из программы\n")
            command = self.reader.read_command().lower()

            if command == "выход":
                break

            if command == "запись":
                cls()
                if not (new_message := self.reader.read_record()) is None:
                    self.sorter.save_new(new_message)

            if command == "журнал":
                cls()
                self.writer.write_data()
                input()


    def welcome(self) -> bool:
        """ Стартовое сообщение программы """
        print(f"JOURNAL\nВерсия: {VERSION}\nВладелец: {AUTHOR}")
        all_right, error_message = self.sorter.loader.buff.values()
        print("\nЗагрузка данных")
        for i in range(50):
            print(f"\r[{'#'*(i+1):<50}]", end='')
            time.sleep(0.01)
        print()

        if all_right:
            print(f"Данне успешно загружены")
            input("...")
            return True

        print(f"При загрузке возникла ошибка: {error_message}")
        print("Данные были стерты")
        input("...")
        return False
