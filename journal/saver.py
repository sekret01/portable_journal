import json
import time


class Saver:
    """ Объект для сохранения новых данных в файл """
    
    def __init__(self) -> None:
        self.save_data_path: str = "journal/storage/storage.json"
        
    def save_new_data(self, new_data: dict) -> None:
        """
        Обработка новых данных и сохранение
        
        Новые данные приходят в следующем формате:

        {
            date: <str>
            time: <time (int)>
            title: <str>
            message: <str>
        }
        
        Будет происходить запись нового сообщения в date если он уже есть,
        в противном случае будет создан новый date и сообщение будет записано туда.
        Будет проведена проверка на новый заголовок, при его наличие в файл storage.json новый 
        заголовок будет добавлен в общий список.
        Дата изменения будет перезаписана на time в сообщении.
        """
        
        with open(self.save_data_path, 'r', encoding='utf-8') as file:
            all_data = json.load(file)
        update_data = self._build_struct(new_data, all_data)
        if update_data:
            with open(self.save_data_path, 'w', encoding='utf-8') as file:
                json.dump(update_data, file)
            
    def _build_struct(self, new_data: dict, all_data: dict) -> dict:
        _title = new_data['title']
        _date = new_data['date']
        _time = new_data['time']
        _message = new_data['message']

        if not _title in all_data['all_titles']:
            all_data['all_titles'].append(_title)
        if _date not in all_data['journal']:
            all_data['journal'][_date] = []

        all_data['journal'][_date].append({'time': _time, 'title': _title, 'message': _message })
        all_data['last_changes'] = _time
        return all_data

    # def _title_is_new(self, title: str, all_titles: list[str]) -> bool:
    #     return not title in all_titles
        
        
