import json
import time
import os


class Loader:
    """ Класс для загрузки данных из файла сохранения """
    
    def __init__(self) -> None:
        self.save_data_path: str = "journal/storage/storage.json"
        self.buff: dict = self._check_storage()
    
    def _check_storage(self) -> dict:
        """ Проверка всего и вся на сохранность хранилища """
        error_message: str = "NoError"
        is_alright: bool = True
        
        if not os.path.exists(self.save_data_path):
            is_alright = False
            error_message = "FileNotFoundError"
        if not os.path.isfile(self.save_data_path): is_alright, error_message = False, "NotFileError"
        
        with open(self.save_data_path, 'r') as file:
            try:
                checked_data = json.load(file)
            except json.decoder.JSONDecodeError:
                self._create_new_storage()
                print({'is_alright': False, 'error_message': "EmptyFileError"})
                return {'is_alright': False, 'error_message': "EmptyFileError"}
            if type(checked_data) != dict:
                is_alright = False
                error_message = "WrongTypeOfDataError"
            
        if list(checked_data.keys()) != ['last_changes', 'all_titles', 'journal']:
            is_alright = False
            error_message = "KeysError"
        if type(checked_data['last_changes']) != int:
            is_alright = False
            error_message = "DateTypeError"
        if type(checked_data['all_titles']) != list:
            is_alright = False
            error_message = "TitleListTypeError"
        if len(checked_data['all_titles']) > 0:
            if type (checked_data['all_titles'][0]) != str:
                is_alright = False
                error_message = "WrongTypeOfTitlesError"
        if type(checked_data['journal']) != dict:
            is_alright = False
            error_message = "JournalListTypeError"
            print(type(checked_data['journal']))
        
        if not is_alright:
            self._create_new_storage()
        
        print({'is_alright': is_alright, 'error_message': error_message})
        return {'is_alright': is_alright, 'error_message': error_message}
        
    def _create_new_storage(self) -> None:
        with open(self.save_data_path, 'w', encoding='utf-8') as file:
            data = {
                    'last_changes': time.time(),
                    'all_titles': [],
                    'journal': {}
                   }
            json.dump(data, file)
    
    
    def update_storage_status(self) -> dict:
        self.buff = self._check_storage()
        return self.buff

    def get_all_data(self) -> dict:
        with open(self.save_data_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
