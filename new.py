from fastapi import FastAPI
app=FastAPI()

data=[{"name":"kiran gajjana","college":"nit sikkim","city":"hyderabad"}]
@app.get("/data")
def data():
    return data

