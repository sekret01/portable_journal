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
            message += line + '\n'
        print("\nконец записи")

        _delete: str = input("Для отмены введите [yes]: ")
        if _delete.lower() == "yes":
            return None
        
        title = title or "запись"
        _time = int(time.time())
        
        return {'time': _time, 'title': title, 'message': message}

    def read_command(self) -> str | None:
        command = input("> ").lower()
        return command

        # if command in _commands:
        #     return command
        # return None
