from .sorter import Sorter
from .printing import Reader
from .printing import Writer
from .command_processing import Distributor
import os
import time


VERSION = "0.2.0"
AUTHOR = "Sekret"
ERRORS = {

}




class Console:
    """ Класс-интерфейс для взаимодействия пользователя с журналом """

    def __init__(self):
        self.distributor = Distributor()
        self.sorter = Sorter()
        self.reader = Reader()
        # self.writer = Writer()

    def start(self):
        start_status = self.welcome()
        while True:
            self.reader.cls()
            print("> запись - новая запись\n> журнал - вывод записей (возможна фильтрация)\n> выход - выход из программы\n")
            command = self.reader.read_command().lower()
            if command.lower() == "выход": break

            res_func: callable = self.distributor.set_command(command=command)
            # self.reader.cls()
            if res_func:
                res_func()


    def welcome(self) -> bool:
        """ Стартовое сообщение программы """
        print(f"JOURNAL\nВерсия: {VERSION}\nВладелец: {AUTHOR}")
        all_right, error_message = self.sorter.encryptor.load_buff.values()
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
