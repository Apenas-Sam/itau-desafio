import os
import httpx
from bs4 import BeautifulSoup
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from langchain_openai import OpenAI
from typing import Union

from src.llm.prompts import prompt

from src.sql.models import ResumeModel
from src.sql.queries import search_resume

from src.router.models import Resume

llm = OpenAI(temperature=0.4, api_key=os.getenv("OPENAI_API_KEY"))

router = APIRouter()


async def scrape_url(url: str) -> str:
    """ "
    scrape_url é a função responsavel por pegar a url da wikipedia
    e retornar o conteúdo do artigo em formato string

    Parâmetros:
    url (str): a url da wikipedia

    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url=url)
            soup = BeautifulSoup(response.text, "html.parser")
            div = soup.find("div", id="bodyContent")
            ps = div.find_all("p")
            clean_ps = []
            for p in ps:
                clean_ps.append(
                    p.text.replace("\n", "").replace("\n\n", "").replace("\n\n\n", "")
                )
            return "\n".join(clean_ps[:12])
        except Exception as e:
            raise Exception("Ocorreu um erro durante o scraping", e)


@router.post("/resume"
             ,response_model=Resume
             ,name="Resume"
             ,description="Realiza a consulta a partir de uma url do Wikipedia, e quantidade de palavras (char_amount) retornando um response do tipo Resume que contém o resumo realizado pelo ChatGPT"
             ,)
async def resume(request: Resume):
    """ "
    Rota /resume

    Responsavel por receber os dados contendo
    a url e quantidade de caracteres para a criação do resumo
    bem como salvar o mesmo no banco de dados

    Parametros:

    request: Request - Recebe o corpo da requisição com os dados

    """
    try:
        search = search_resume(str(request.url))
        if search == None:
            try:
                srt_url = str(request.url)
                scrape = await scrape_url(srt_url)
            except Exception as e:
                print("/resume Exception scrape_url", e)
                return JSONResponse(
                    status_code=500,
                    content={
                        "message": "Houve um problema.",
                        "recebido": request.model_dump_json(),
                        "erro": str(e),
                    },
                )
            chain = prompt | llm
            result = chain.invoke(
                {
                    "content": scrape,
                    "char_amount": request.char_amount,
                }
            )
            request.resume = result
            request.insert_into_db()
            return request
        return search
    except Exception as e:
        print("/resume Exception:", e)
        return JSONResponse(
            status_code=500,
            content={
                "message": "Houve um problema. Verifique os dados enviados, urls incompletas e/ou numero de caracteres incorretos ",
                "recebido": request.model_dump_json(),
                "erro": str(e),
            },
        )
