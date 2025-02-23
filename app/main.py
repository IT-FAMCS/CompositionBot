from fastapi import FastAPI, Request

app = FastAPI()

@app.get('/')
async def main(request: Request):
    return {'response' : "Hello"}