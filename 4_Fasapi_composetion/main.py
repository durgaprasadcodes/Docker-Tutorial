from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message":"Docker-FastAPI Message Is Running Successfully"}