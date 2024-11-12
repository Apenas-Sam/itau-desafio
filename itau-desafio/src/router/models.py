from datetime import datetime
from pydantic import BaseModel, HttpUrl, field_validator,Field
from typing import Optional
from src.sql.conn import session
from src.sql.models import ResumeModel


class Resume(BaseModel):
    url: HttpUrl
    char_amount: int = Field(None,ge=100,le=1000)
    resume: Optional[str] = ""
    created_at: datetime = datetime.now()

    @field_validator("char_amount")
    def validate_char_amount(cls, v):
        if v < 100 or v > 2000:
            raise ValueError("Inserir Valores entre 100 a 1000 caracteres.")
        return v

    def insert_into_db(self):
        resume_model = ResumeModel(
            url=str(self.url), resume=self.resume, char_amount=self.char_amount
        )
        session.add(resume_model)
        session.commit()


class Search(BaseModel):
    url: HttpUrl
