from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from src.model.settings.db_connection_handler import db_connection_handler
from src.views.pessoas_finder_view import PessoasFinderView

pessoas_routes = APIRouter()


@pessoas_routes.get("/pessoas")
async def get_pessoas(request: Request):
    pessoas_finder_view = PessoasFinderView()

    await db_connection_handler.connect_to_db()
    response = await pessoas_finder_view.handle_find_people(request)
    await db_connection_handler.disconnect_to_db()

    return JSONResponse(
        content=response["body"],
        status_code=response["status_code"],
    )
