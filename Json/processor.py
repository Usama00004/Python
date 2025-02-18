import json
import os
import pandas as pd

# Define the correct file path
json_file_path = "./Json/data.json"

# Ensure the file exists
if not os.path.exists(json_file_path):
    print(f"Error: '{json_file_path}' not found!")
elif os.path.getsize(json_file_path) == 0:
    print(f"Error: '{json_file_path}' is empty!")
else:
    try:
        # Open and read JSON file
        with open(json_file_path,"r",encoding="utf-8") as file:
            json_data = file.read()  # Read the file content
        
        # Parse the JSON content
        data = json.loads(json_data)
        print("Valid JSON!\n")

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

    except json.JSONDecodeError as e:
        print("Invalid JSON:", e)
    except Exception as e:
        print(f"Unexpected error: {e}")
