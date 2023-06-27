from fastapi import FastAPI
from rental.router import routerApartment as router_apartment
from rental.router import routerGroup as router_group

app = FastAPI(
    title="Rental App"
)

app.include_router(router_apartment)
app.include_router(router_group)
