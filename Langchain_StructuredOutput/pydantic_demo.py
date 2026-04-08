from pydantic import BaseModel, Field
from typing import Optional

class Student(BaseModel):
    name: str = "John Doe"
    age: Optional[int] = None
    cgpa: float = Field(..., gt=0.0, le=10.0, description="Cumulative Grade Point Average")

new_student = {'name': 'Alice', 'age': '20', 'cgpa': 9.0}
student = Student(**new_student)
print(student)
print(student.age)
student_dict = dict(student) #equalent to student.model_dump() in pydantic
print(student_dict['age'])

student_json = student.model_dump_json() 
print(student_json)