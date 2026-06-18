import json

with open("config.json", "r") as file:
    config = json.load(file)

print("Server name:", config["server_name"])
print("GPU count:", config["gpu_count"])
print("Status:", config["status"])
