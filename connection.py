from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    # replace it with ur mysql user and password
    'mysql+pymysql://root:2677157Cr7@localhost/instituciones')


def create_session():
    global session
    session = sessionmaker(bind=engine)()
    return session


def close_session():
    session.close()
