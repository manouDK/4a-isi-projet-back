from fastapi import FastAPI

from app.routers import system

app = FastAPI(
    title="Pol-eat-heck API",
    version="0.1.0",
    description="API du projet Pol-eat-heck : menus et réservations",
)


app.include_router(system.router, prefix="/api")