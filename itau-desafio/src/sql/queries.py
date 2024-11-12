from src.sql.models import ResumeModel
from src.sql.conn import session


def search_resume(url):
    try:
        return session.query(ResumeModel).filter_by(url=str(url)).first()
    except Exception as e:
        print(f"Error while searching resume: {e}")
        return None


def remove_resume(url):
    try:
        resume = search_resume(url)
        if resume:
            session.delete(resume)
            session.commit()
            return True
        else:
            return False
    except Exception as e:
        print(f"Error while removing resume: {e}")
        return False
