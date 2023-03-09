from fastapi import APIRouter, Depends, Form
from fastapi.responses import JSONResponse
from app.models.model_oracle import SearchSchema
from app.services.service_oracle import OracleService

router = APIRouter(
    prefix="/template",
    tags=["TEMPLATE"],
    responses={404: {"message": "Not found"}}
)

@router.get("/employees")
async def all_employees():
    return OracleService().all_employees()

@router.post("/person/search")
async def search_employees(data: SearchSchema = Depends(SearchSchema)):
    return OracleService().search_employees(data.department)