from fastapi import FastAPI ,Path 
from typing import Optional
from pydantic import BaseModel



app = FastAPI()
@app.get("/")
def test():
    return{"name":"AL_moutasem"}

students = {
    1:{
        "name" : "mohamad" ,
        "Age" : 17 ,
        "class" : "2 Years"
    }
}

@app.get("/student-information-by-id/{student_id}")
def get_student_information(student_id : int = Path(..., description="Enter Student_ID", gt=0,lt=3) ):
    if student_id not in students:
        return{"Error":"this student dose not exist"}
    
    return students[student_id]


@app.get("/student-information-by-name")
def get_student_information(student_name: str = Path(..., regex="^[A-Za-z0-9_ ]+$")):
    for id in students:
        if students [id]["name"] == student_name :
          return students[id]
    return{"Error":"this student dose not exist"}

@app.get("/student-information-by-name")
def get_student_information(student_name: Optional[str] = None):
    for id in students:
        if students [id]["name"] == student_name :
          return students[id]
    return{"Error":"this student dose not exist"}

class Student(BaseModel):
    name:str
    age:int
    year:str

@app.post("/create-student/{student_id}")
def create_student(student_id : int, student :Student):
    if student_id in students:
        return{"Error":"This student is exist"}
    students[student_id] = student.dict()
    return students[student_id]
    
class UbdateStu(BaseModel):
    name:Optional[str]
    age:Optional[int] = None
    year:Optional[str] = None


@app.put("/Edit-student{student_id}")
def edit_student(student_id : int, student :UbdateStu):
    if student_id not in students:
        return{"Error":"This student isn't exist"}
    if student.name != None:
        students[student_id]["name"] = student.name
    if student.age is not None:
        students[student_id]['age'] = student.age
    if student.year is not None:
        students[student_id]['class'] = student.year
    return students[student_id]
    

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"error": "This student does not exist"}
    del students[student_id]
    return {"message": "Student deleted successfully"}
    