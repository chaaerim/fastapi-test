from fastapi import FastAPI
from fastapi_test.apps.common.router import router as common_router

app=FastAPI()
app.include_router(common_router)
