from datetime import datetime
import os

class FileWriter():
    def __init__(self, output: str = "logs"):
        self.output = output
        if not os.path.exists(self.output):
            os.makedirs(self.output, exist_ok=True)

    def send_data(self, data: str, machine_name: str) -> None:
        filename = os.path.join(self.output, f"{machine_name}_log.txt")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line_to_write = f"[{timestamp}] {data}"
        try:
            with open(filename, "a", encoding="utf-8") as f:
                f.write(line_to_write + "\n")

            print(f"The data that was written is: '{line_to_write}' for machine: {machine_name}")
            print(f"The data was written to {filename} successfully.\n")
        except OSError as e:
            print(f"[fileWriter] Error writing to {filename}: {e}")

if __name__ == "__main__":
    Writer = FileWriter()
    Writer.send_data("hello world", "pc1")




# if __name__ == "__main__":
#     Writer = FileWriter()
#     data = "hello world"
#     machine_name = "pc1"
#     Writer.send_data(data, machine_name)
#     print(f"the data that was written is: '{data}' for pc: {machine_name}")
#     print("The data was written to logs/PC1_log.txt successfully.")





