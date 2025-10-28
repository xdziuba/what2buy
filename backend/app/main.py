from fastapi import FastAPI
from app.routes import root, search


app = FastAPI(title="What2Buy", version="0.1", description="An AI-powered product research assistant.")

app.include_router(root.router)
app.include_router(search.router)