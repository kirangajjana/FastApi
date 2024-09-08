from fastapi import FastAPI
app=FastAPI()

data1=[{"name":"kiran gajjana","college":"nit sikkim","city":"hyderabad"},
      {"name":"teja gajjana","college":"andhra university","city":"hyderabad"}]
@app.get("/data/{bookdata}")
def data(bookdata):
    for i in data1:
         if i.get("name").casefold()==bookdata.casefold():
              return i


