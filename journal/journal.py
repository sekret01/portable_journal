from sorter import Sorter


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


        
            
        
