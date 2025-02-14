import json
import os

# Check available files in the "Json" directory
print("Files in current directory:", os.listdir('./Json'))

# Define the correct file path
json_file_path = "./Json/data.json"

# Ensure the file exists and is not empty
if not os.path.exists(json_file_path):
    print(f"❌ Error: '{json_file_path}' not found!")
elif os.path.getsize(json_file_path) == 0:
    print(f"⚠️ Error: '{json_file_path}' is empty!")
else:
    try:
        # Open and read JSON file
        with open(json_file_path, "r", encoding="utf-8") as file:
            json_data = file.read()  # Read the file content
        
        # Parse the JSON content
        parsed_data = json.loads(json_data)
        
        print("✅ Valid JSON!")
        print(json.dumps(parsed_data, indent=4))  # Pretty-print JSON
        
    except json.JSONDecodeError as e:
        print("❌ Invalid JSON:", e)
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")
