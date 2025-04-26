import time

from .file_manager import Loader, Saver
from .encryptor import Encryptor

class Sorter:
    """
    Класс, предназначенный для обработки и фильтрации получаемых из
    файла данных для просмотра,
    обработки дат и вставки новых данных для записи
    """

    def __init__(self):
        # self.loader = Loader()
        # self.saver = Saver()
        self.encryptor = Encryptor()

    def get_journal(self,
                    title: str | None = None,
                    date: str | None = None
                    ):
        """
        Получение записей.

        Возможны 3 варианта:
         - фильтр по дате (date) - имеет наивысший приоритет.
           Будут возвращены записи только этого дня (если он есть)
           >> get_journal(date="12.12.2020")

         - фильтр по заголовку (title) - возвращает записи со всех дат
           с заданным заголовком
           >> get_journal(title="SOME TEXT")

         - без фильтров - будут возвращены все записи
           >> >> get_journal()
        """
        data = self.encryptor.load()['journal']

        if title is None and date is None: return data
        if date:
            return {date: data[date]}
        if title:
            return {date_id: [_data for _data in messages_list if _data['title'] == title] for date_id, messages_list in
                    data.items()}

    def get_last_change(self) -> int:
        """ Получение даты последних изменений (в секундах) """
        last_changes = int(self.encryptor.load()['last_changes'])
        return last_changes

    def get_titles(self) -> list[str]:
        """ Получение всех возможных заголовков """
        titles = self.encryptor.load()['all_titles']
        return titles

    def save_new(self, new_data: dict) -> None:
        """
        Обработка новых данных перед сохранением

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

        all_data = self.encryptor.load()
        update_data = self._build_struct(new_data, all_data)
        self.encryptor.save(update_data)

    def _build_struct(self, new_data: dict, all_data: dict) -> dict:
        """ Построение новой структуры для записи """
        dd = time.localtime(new_data['time'])

        _title = new_data['title']
        _date = f"{dd.tm_mday}.{dd.tm_mon}.{dd.tm_year}"
        _time = new_data['time']
        _message = new_data['message']

        if not _title in all_data['all_titles']:
            all_data['all_titles'].append(_title)
        if _date not in all_data['journal']:
            all_data['journal'][_date] = []

        all_data['journal'][_date].append({'time': _time, 'title': _title, 'message': _message})
        all_data['last_changes'] = _time
        return all_data
