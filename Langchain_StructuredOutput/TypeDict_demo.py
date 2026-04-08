from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person1: Person = {"name": "Ali", "age": 30}
new_person2: Person = {"name": "Ali", "age": "30"}

print(new_person2)