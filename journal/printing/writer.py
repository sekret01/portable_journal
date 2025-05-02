from ..sorter import Sorter
from ..brush import Brush, brush_start
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
            if len(messages) == 0: continue
            print(f"ДАТА {Brush.blue(date)}")
            for mes in messages:
                dd = time.localtime(mes['time'])
                print()
                print(f"запись от {Brush.gray(f"{dd.tm_hour}:{dd.tm_min}:{dd.tm_sec}")}")
                print(f"[{Brush.yellow(mes['title'])}]")
                print(f"{mes['message']}")
            print("\n")