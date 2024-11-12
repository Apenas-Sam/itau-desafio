from fastapi import FastAPI
from src.router import resume, consult

app = FastAPI(
    title="Desafio Itaú",
    description="API para consulta e geração de resumos de páginas da Wikipedia",
    version="1.0.0",

)

app.include_router(consult.router)
app.include_router(resume.router)


@app.get("/")
async def home():
    return {"message": f"Desafio Itaú"}
