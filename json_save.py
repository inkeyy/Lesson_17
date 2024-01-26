import json

person = {
    'name':'Max',
    'age':'10',
    'phones':['911']
}
person_2 = ["rffsd", "ffsd"]
result2 = json.dumps(person_2)
print(result2)
print(type(result2))
result = json.dumps(person)
print(result)
print(type(result))
