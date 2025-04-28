from typing import Union
from .journal import Journal




class Distributor:
    """ Класс для распределения команд """

    def __init__(self):
        self.journal = Journal()
        self.commands: dict[str, callable] = {
            "журнал": self.journal.get_message,
            "запись": self.journal.write_message
        }

    def set_command(self, command: str) -> Union[callable, None]:
        return self.commands.get(command, None)




