from .sorter import Sorter
import time

class Writer:
    """
    Вывод информации из памяти журнала
    """
    
    def __init__(self):
        self.sorter = Sorter()

    def write_data(self, title: str | None = None, date: str | None = None) -> None:
        """ Выводит записи по фильтрам """
        data = self.sorter.get_journal(title=title, date=date)

        for date, messages in data.items():
            print(f"ДАТА {date}")
            for mes in messages:
                dd = time.localtime(mes['time'])
                print()
                print(f"запись от {dd.tm_hour}:{dd.tm_min}:{dd.tm_sec}")
                print(f"[{mes['title']}]")
                print(f"{mes['message']}")
            print("\n\n")