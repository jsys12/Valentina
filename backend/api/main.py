from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
@app.get("/index")
def index():
    return FileResponse("../frontend/index.html")