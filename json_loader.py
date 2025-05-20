import json

# Open the file and load the content into a Python dictionary
with open("data.json", "r") as file:
	data = json.load(file)

print("Loaded data: ", data)

#Accessing specific items
print("Name:", data["name"])
print("skills:", ", ".join(data["skills"]))
