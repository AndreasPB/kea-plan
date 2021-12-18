from app.db.psql_test_data import setup_psql_test_attendances
from app.db.psql_test_data import setup_psql_test_data
from app.db.psql_test_data import setup_psql_test_links
from app.db.psql_test_data import teardown_psql
from fastapi import APIRouter

router = APIRouter(
    prefix="/test",
    tags=["test"],
)


@router.post("/psql")
async def create_test_psql():
    setup_psql_test_data()
    setup_psql_test_attendances()
    setup_psql_test_links()


@router.delete("/psql")
async def delete_test_psql():
    teardown_psql()
