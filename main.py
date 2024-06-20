from fastapi import FastAPI
from app.routers import basicPathAndQueryParamsEg, parameter_validation, request_body

app = FastAPI()

app.include_router(basicPathAndQueryParamsEg.router)
app.include_router(parameter_validation.router)
app.include_router(request_body.router)
