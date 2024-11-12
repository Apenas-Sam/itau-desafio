from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer, DateTime
from src.sql.conn import engine
from datetime import datetime

Base = declarative_base()


class ResumeModel(Base):
    __tablename__ = "resumes"

    url = Column(String, primary_key=True, nullable=False, unique=True)
    resume = Column(String, nullable=False)
    char_amount = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now())

    def __init__(self, url, resume, char_amount):
        self.url = url
        self.resume = resume
        self.char_amount = char_amount

    def __repr__(self):
        return f"Resume:\n\
                        url={self.url}\n\
                        resume={self.resume}\n\
                        char_amount={self.char_amount}\n\
                        created_at={self.created_at}"


Base.metadata.create_all(bind=engine)
