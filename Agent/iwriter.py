from abc import ABC


class IWriter(ABC):
    def send_data(data, machine_name) -> None:
        pass
