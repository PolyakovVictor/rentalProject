from fastapi import FastAPI
from operations.router import router as router_operation

app = FastAPI(
    title="Rental App"
)

app.include_router(router_operation)
