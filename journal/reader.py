import time


_commands = []

class Reader:
    """ Обработка введенного текста и направление на запись в журнал """
    
    def __init__(self):
        ...
       
    def read_record(self) -> dict | None:
        title: str = input("тема: ")
        message: str = ""
        print("начало записи\n")
        while line := input(""):
            message += line
        print("\nконец записи")

        _delete: str = input("Для отмены введите [yes]: ")
        if _delete.lower() == "yes":
            return None
        
        title = title or "запись"
        date = time.time()
        
        return {'date': date, 'title': title, 'message': message}

    def read_command(self) -> str | None:
        command = input("> ").lower()
        if command in _commands:
            return command
        return None
        
