import os, json

json_filename = "db.json"
# Dump all the data in the database to JSON file
os.system(f"python manage.py dumpdata > {json_filename}")

# Read the data dump
with open(json_filename, 'r') as file:
    db_data = json.load(file)
# Delete the data dump
os.remove(json_filename)

final_data = {
    "users": [],
    "contacts": []
}

# Get data for users and contacts only
for entry in db_data:
    # Get the users in the database
    if entry["model"] == "auth.user":
        user = entry["fields"]
        user["id"] = entry["pk"]
        final_data["users"].append(user)

    # Get the contacts in the database
    if entry["model"] == "crudapp.contact":
        contact = entry["fields"]
        contact["id"] = entry["pk"]
        final_data["contacts"].append(contact)


output_file = "data.json"

with open(output_file, "w") as file:
    data = json.dumps(final_data, indent=4)
    print(data)
    file.write(data)
