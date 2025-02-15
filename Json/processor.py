import json
import os
import pandas as pd

# Define the correct file path
json_data = "./Json/data.json"

# # Check if directory exists
# if not os.path.exists("./Json"):
#     print("Error: 'Json' directory does not exist!")

# # Ensure the file exists and is not empty
# elif not os.path.exists(json_data):
#     print(f"Error: '{json_data}' not found!")
# elif os.path.getsize(json_data) == 0:
#     print(f"Error: '{json_data}' is empty!")
# else:
#     try:
#         # Open and read JSON file
#         with open(json_data, "r", encoding="utf-8") as file:
#             json_data = file.read()  # Read the file content
        
#         # Parse the JSON content
#         parsed_data = json.loads(json_data)
#         print("Valid JSON!")
#         print(json.dumps(parsed_data, indent=4))  # Pretty-print JSON

#         # Convert JSON to DataFrame
#         try:
#             data_frame = pd.DataFrame(parsed_data)
#             print("DataFrame Created Successfully:")
#             print(data_frame.head())  # Print first 5 rows
#         except ValueError as e:
#             print("Error converting JSON to DataFrame:", e)

#     except json.JSONDecodeError as e:
#         print("Invalid JSON:", e)
#     except Exception as e:
#         print(f"Unexpected error: {e}")


# Parse JSON
data = json.loads(json_data)

# Traverse the JSON
print(f"Company: {data['company']}\n")

print("Employees:")
for emp in data["employees"]:
    print(f"  - {emp['name']} (ID: {emp['id']})")
    print(f"    Age: {emp['age']}, Department: {emp['department']}")
    print(f"    Skills: {', '.join(emp['skills'])}")
    
    print("    Projects:")
    for proj in emp["projects"]:
        print(f"      - {proj['name']} (Budget: ${proj['budget']}, Status: {proj['status']})")
    print()

# Traverse Financials
print("Financials:")
print(f"  Revenue: ${data['financials']['revenue']}")
print(f"  Expenses:")
for category, amount in data["financials"]["expenses"].items():
    print(f"    {category.capitalize()}: ${amount}")

# Traverse Headquarters Information
print("\nHeadquarters:")
hq = data["headquarters"]
print(f"  Location: {hq['city']}, {hq['country']}")
print(f"  Contact: {hq['contacts']['email']} | {hq['contacts']['phone']}")
