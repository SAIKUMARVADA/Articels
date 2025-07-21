from fastapi import FastAPI
from routes import router as atmservice_router

app = FastAPI(title="Atm Service API")

app.include_router(atmservice_router)