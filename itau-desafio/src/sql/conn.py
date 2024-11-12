import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@postgres:5432/{os.getenv('DB_NAME')}",
    echo=True,
)

Session = sessionmaker(bind=engine)
session = Session()
