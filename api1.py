from fastapi import Body,FastAPI
app=FastAPI()

data1=[{"name":"kiran gajjana","college":"nit sikkim","city":"hyderabad"},
      {"name":"teja gajjana","college":"andhra university","city":"hyderabad"}]

@app.get("/data/{bookdata}")
def data(bookdata):
    for i in data1:
         if i.get("name").casefold()==bookdata.casefold():
              return i
         

@app.get("/data/")
async def cato(city: str):
     data=[]
     for i in data1:
          if i.get("city").casefold()==city.casefold():
               data.append(i)
     return data    
#post request method               
@app.post("/data/create_data")
async def create_data(new_data=Body()):
     data1.append(new_data)
 #put request method    


