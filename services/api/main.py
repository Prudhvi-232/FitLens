from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

app = FastAPI()

# CORS origins for frontend (React, etc.)
origins = [
    "http://localhost",
    "http://localhost:3000",
]

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/", tags=["Root"])
async def read_root() -> dict:
    return {"message": "Hello, World"}

# Item endpoint
@app.get("/items/{item_id}", tags=["Items"])
async def read_item(item_id: int, q: Optional[str] = None) -> dict:
    return {"item_id": item_id, "query": q}
