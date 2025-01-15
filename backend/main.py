from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    n=10
    n= [i+1 for i in range(n)]
    return {"message": f"Hello {n}"}
