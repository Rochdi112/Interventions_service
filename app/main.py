from fastapi import FastAPI
from app.routes.interventions import router as interventions_router

app = FastAPI(
    title="Interventions Service",
    description="Microservice de gestion des interventions correctives et préventives",
    version="1.0.0",
)

app.include_router(interventions_router, prefix="/interventions", tags=["Interventions"])
