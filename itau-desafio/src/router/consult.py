from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from src.sql.queries import search_resume
from src.router.models import Search,Resume

router = APIRouter()


@router.post("/consult",
             response_model=Resume
             ,name="Consult"
             ,description="Realiza a consulta a partir de uma url do Wikipedia e retorna o Resumo, caso esteja presente no banco de dados"
             ,)
async def consult_url(request: Search):
    """"
    Rota responsável por realizar a busca do resumo a partir da URL

    parameters:
    request: Search - Recebe o corpo da requisição com a URL

    """
    try:
        resume = search_resume(str(request.url))
        if resume == None:
            return JSONResponse(
                status_code=404,
                content={
                    "message": "Resumo não encontrado. Para inserir novos resumos, utilizar a rota /resume",
                    "recebido": request.model_dump_json(),
                },
            )
        return resume
    except Exception as e:
        print("/consult/ Exception:", e)
        return JSONResponse(
            status_code=500,
            content={
                "message": "Houve um problema ao encontrar o resumo.",
                "recebido": request.model_dump_json(),
                "erro": str(e),
            },
        )
