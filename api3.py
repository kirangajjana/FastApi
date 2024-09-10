from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()
app=FastAPI()

#static calling
@app.get("/kiran")
def name():
    API_KEY=os.getenv("API_KEY")
    return API_KEY

#path parameters
@app.get("/book/{name}")
def pathpara(name: str):
    return "welcome "+ name
    