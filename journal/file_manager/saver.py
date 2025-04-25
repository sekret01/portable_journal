import json
import time


class Saver:
    """ Объект для сохранения новых данных в файл """
    
    def __init__(self) -> None:
        self.save_data_path: str = "journal/storage/storage.json"
        
    def save_new_data(self, new_data: dict) -> None:
        """

        """
        
        with open(self.save_data_path, 'w', encoding='utf-8') as file:
            json.dump(new_data, file)
            
    # def _build_struct(self, new_data: dict, all_data: dict) -> dict:
    #     _title = new_data['title']
    #     _date = new_data['date']
    #     _time = new_data['time']
    #     _message = new_data['message']
    #
    #     if not _title in all_data['all_titles']:
    #         all_data['all_titles'].append(_title)
    #     if _date not in all_data['journal']:
    #         all_data['journal'][_date] = []
    #
    #     all_data['journal'][_date].append({'time': _time, 'title': _title, 'message': _message })
    #     all_data['last_changes'] = _time
    #     return all_data

    # def _title_is_new(self, title: str, all_titles: list[str]) -> bool:
    #     return not title in all_titles
        
        
