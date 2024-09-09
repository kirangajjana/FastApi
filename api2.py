from fastapi import FastAPI,Body

app=FastAPI()


college=[{"name":"abhishek","college":"nit sikkim","state":"bihar"},{"name":"deepak","college":"nit sikkim","state":"punjab"},{"name":"saket","college":"nit sikkim","state":"bihar"},{"name":"yetendra","college":"nitsikkim","state":"up"}]

#get request using path parameter

@app.get("/college")
async def collegepapa():
    return college


#query parameter
@app.get("/college/")
async def collegenew(state):
    data=[]
    for i in college:
        if i.get("state").casefold()==state.casefold():
            data.append(i)
    return data       