from .sorter import Sorter
from .printing import Reader, Writer



"""
стуркура записей в хранилище:
{
    all_titles: [<str>, ...],
    last_changes: <time>,
    journal:
    {
        date:
        [
        {
            time: <time>
            title: <str>
            message: <str>
        },
        ...
        ]
    }
}

фильтрация происходит по:
    - date (дата)
    - title (заголовок)
"""


class Journal:
    """
    Объект хранения части данных и последних записей.
    """
    
    def __init__(self) -> None:

        self.sorter = Sorter()
        self.reader = Reader()
        self.writer = Writer()

        self.dates: list[str] = []
        self.titles: list[str] = []
        self.ready_to_work = False
        self.sorter = Sorter()
        self._setup()
        
    def _setup(self) -> None:
        try:
            self.titles = self.sorter.get_titles()
            data = self.sorter.get_journal()
        except Exception as ex:
            self.ready_to_work = False
            return

        self.dates = [date for date in data.keys()]
        self.ready_to_work = True

    def write_message(self) -> None:
        self.reader.cls()
        if new_message := self.reader.read_record():
            self.sorter.save_new(new_message)

    def get_message(self) -> None:
        self.reader.cls()
        title, date = self.reader.read_filters().values()
        date = date if date in self.dates else None
        title = title if title in self.titles else None
        self.reader.cls()
        self.writer.write_data(title=title, date=date)
        input("...")

        
