from fastapi import FastAPI

from app.api.query import router as query_router


app = FastAPI()

app.include_router(query_router)


@app.get("/health")
def health_check():
	"""Simple health endpoint."""
	return {"status": "ok"}
