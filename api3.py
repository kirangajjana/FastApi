from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()
app=FastAPI()

data=[{"name":"kiran gajjana","age":25,"college":"nit sikkim","city":"Hyderabad"},{"name":"saket kumar","age":27,"college":"nit sikkim","city":"hyderabad"},{"name":"abhishek kumar","age":25,"college":"nit sikkim","city":"hyderabad"}]

#static calling
@app.get("/kiran")
def name():
    API_KEY=os.getenv("API_KEY")
    return API_KEY

#path parameters
@app.get("/book/{name}")
def pathpara(name: str):
    return "welcome "+ name
 #query parameter
@app.get("/college/")
def college(college: str):
    campus=[]
    for i in data:
        if i.get("college").casefold()==college.casefold():
            campus.append(i)
    return campus           