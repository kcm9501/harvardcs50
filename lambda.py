people = [
    {"name": "Harry","house":"Gry"},
    {"name": "Cho","house":"Raven"},
    {"name":"Draco","house":"Slyt"},
]


people.sort(key=lambda person: person["name"])

print(people)