from fastapi import FastAPI
from app.routes import event, health

app = FastAPI(title="EventForge")

app.include_router(health.router)
app.include_router(event.router)
