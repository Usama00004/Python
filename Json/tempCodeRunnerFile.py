import json
import os

print("Files in current directory:", os.listdir('./Json'))

json_data = "./Json/data.json"
parsed_data = json.loads(json_data)

with open(json_data, "r", encoding="utf-8") as file:
        data = json.load(file)
        print("✅ JSON is valid and successfully loaded!")
        print(json.dumps(data, indent=4))  # Pretty print the JSON

# try:
#     parsed_data = json.loads(json_data)
#     print(json_data)
#     print("Valid JSON!")
# except json.JSONDecodeError as e:
#     print(json_data)
#     print("Invalid JSON:", e)