import json
import time
import os


class Loader:
    """ Класс для загрузки данных из файла сохранения """
    
    def __init__(self) -> None:
        self.save_data_path: str = "journal/storage/storage.json"
        self.buff: dict[any] = self._check_storage()
    
    def _check_storage(self) -> dict:
        """ Проверка всего и вся на сохранность хранилища """
        error_message: str = "NoError"
        is_alright: bool = True
        
        if not os.path.exists(self.save_data_path):
            is_alright = False
            error_message = "FileNotFoundError"
        if not os.path.isfile(self.save_data_path): is_alright = False, "NotFileError"
        
        with open(self.save_data_path, 'r', encoding='utf-8') as file:
            if type(cheked_data := json.load(file)) != dict:
                is_alright = False
                error_message = "WrongTypeOfDataError"
            
        if list(cheked_data.keys()) != ['last_changes', 'all_titles', 'journal']:
            is_alright = False
            error_message = "KeysError"
        if type(cheked_data['last_changes']) != float:
            is_alright = False
            error_message = "DateTypeError"
        if type(cheked_data['all_titles']) != list:
            is_alright = False
            error_message = "TitleListTypeError"
        if len(cheked_data['all_titles']) > 0:
            if type (cheked_data['all_titles'][0]) != str:
                is_alright = False
                error_message = "WrongTypeOfTitlesError"
        if type(cheked_data['journal']) != dict:
            is_alright = False
            error_message = "JournalListTypeError"
            print(type(cheked_data['journal']))
        
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
    
    
    def update_storage_status(self) -> dict[any]:
        self.buff = self._check_storage()
        return self.buff
    
    def get_last_change(self) -> str:
        with open(self.save_data_path, 'r', encoding='utf-8') as file:
            last_changes = float(json.load(file)['last_changes'])
        return last_changes
    
    def get_titles(self):
        with open(self.save_data_path, 'r', encoding='utf-8') as file:
            titles = json.load(file)['all_titles']
        return titles
    
    def get_journal(self,
                    title: str | None = None,
                    date: str | None = None
                    ):
        with open(self.save_data_path, 'r', encoding='utf-8') as file:
            data = json.load(file)['journal']
        
        if title is None and date is None: return data
        if date:
            return data[date]
        if title:
            return {date_id: { _time: _data for _time, _data in message_data.items() if _data['title'] == title } for date_id, message_data in data.items()}
            
            
    