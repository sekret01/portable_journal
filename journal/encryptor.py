from .file_manager import Loader
from .file_manager import Saver


class Encryptor:
    """ Шифрование и расшифрование текста """

    def __init__(self):
        self.loader = Loader()
        self.saver = Saver()

    def load(self) -> dict:
        """ Загрузка и расшифровка данных из хранилища """
        data = self.loader.get_all_data()
        # расшифровка
        return data

    def save(self, update_data: dict) -> None:
        """ Шифрование обновленных данных и сохранение в хранилище """
        # шифрование
        self.saver.save_new_data(update_data)

    @property
    def load_buff(self) -> dict:
        """ Просмотр буфера состояния загрузки """
        return self.loader.buff


