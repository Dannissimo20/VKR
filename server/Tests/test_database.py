from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

test_engine = create_engine('postgresql+psycopg2://postgres:denchik2702@localhost:5432/diplom_sto_test')

TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

Test_base = declarative_base()
