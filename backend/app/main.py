from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.api.query import router as query_router

app = FastAPI()

# API routes
app.include_router(query_router)

# Serve frontend static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def serve_frontend():
    return FileResponse("static/index.html")

@app.get("/health")
def health_check():
    return {"status": "ok"}
