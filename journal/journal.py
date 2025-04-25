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
        
    def setup(self) -> None:
        ...
        
            
        
