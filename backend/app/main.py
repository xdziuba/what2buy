from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import root, search


app = FastAPI(title="What2Buy", version="0.1", description="API for an AI-powered product research assistant.")

# Configure CORS
origins = [
    "http://localhost:9000",
    "http://127.0.0.1:9000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(root.router)
app.include_router(search.router)