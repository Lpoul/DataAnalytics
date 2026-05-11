# Name: Leon Poulson
# Date: 5/10/26
# Instructor: Deodat
# Manipulating dictionary's

contact_info = {
    "name": "John Fortnight",
    "address": "123 Epic Street",
    "city": "Tilted Towers",
    "state": "LA",
    "zip": "404404"
}

print(f"""
{contact_info['name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}
""")

contact_info.pop("name")

full_name = {
    "first name": "John",
    "last name": "Fortnight"
}

full_name.update({"honorific": "Mr."})

contact_info.update({"full_name": full_name})

print(f"""
{contact_info['full_name']['honorific']} {contact_info['full_name']['first name']} {contact_info['full_name']['last name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}
""")