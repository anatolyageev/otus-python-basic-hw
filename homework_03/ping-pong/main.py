from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
def get_pong():
    return {
        "message": "pong"
    }

