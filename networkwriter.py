from datetime import time

import requests

from iwriter import IWriter

class NetworkWriter(IWriter):
    def __init__(self, url:str) -> None:
        self.url = url


    def send_data(self, data: str, machine_name: str = "shlomo_machine") -> None:
        if not isinstance(data, str):
            raise TypeError("data must be a string")

        payload = {
            "machine_name" : machine_name,
            # "time" : time.time(),
            "data": data
        }

        try:
            response = requests.post(self.url, json=payload)
            response.raise_for_status()
            print("data sent successfully")

        except requests.RequestException as e:
            print("not sent successfully")