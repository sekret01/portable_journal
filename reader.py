import time


class Reader:
    """ Обработка введенного текста и направление на запись в журнал """
    
    def __init__(self):
        ...
       
    def create_record(self) -> dict[] | None:
        title: str = input("тема: ")
        message: str = ""
        while (line := input("> "):
            message += line
        
        _delete: str = input("Для отмены введите [yes]: ")
        if _delete.lower() == "yes": return None
        
        title = title or "запись"
        date = time.time()
        
        return {'date': date, 'title': title, 'message': message}
        
