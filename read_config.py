import json

try:
    with open("config.json", "r") as file:
        config = json.load(file)
    print("Server name:", config["server_name"])
    print("GPU count:", config["gpu_count"])
    print("Status:", config["status"])
except FileNotFoundError:
    print("Error: config.json not found. Check the file path.")
except json.JSONDecodeError:
    print("Error: config.json exists but isn't valid JSON.")
