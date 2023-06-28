from fastapi import FastAPI
from api.routers import router

app = FastAPI(
    title="Rental App"
)

app.include_router(router)
