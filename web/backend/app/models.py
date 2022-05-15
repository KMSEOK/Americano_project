from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from app.dummy_data import dummy_users, dummy_jobs, dummy_transactions
from sqlalchemy.orm import Session, sessionmaker
import enum
from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

# DB_URL = "postgresql://postgres:pass@db:5432/app"

DB_URL = "postgresql+psycopg2://postgres:pass@db:5432/app"
engine = create_engine(DB_URL)
Base = declarative_base()

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# def get_db():
#     db = session_local()
#     try:
#         yield db
#     finally:
#         db.close()

class GradeType(str, enum.Enum):
    beginner = "beginner"
    normal = "normal"
    advance = "advance"

class Users(Base):
    
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    grade = Column(Enum(GradeType))
    introduction = Column(String)
    jobs = relationship("Jobs")

class PlaceType(str, enum.Enum):
    honkan = "honkan"
    wonagan = "wonagan"
    pogonkan = "pogonkan"
    inmunkan = "inmunkan"
    chayonkan = "chayonkan"
    konhakkan = "konhakkan"

class StatusType(str, enum.Enum):
    done = "done"
    preparing = "preparing"
    inprogress = "inprogress"

class Jobs(Base):

    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("users.id"))
    title = Column(String)
    description = Column(String)
    place = Column(Enum(PlaceType))
    reawrd_money = Column(Integer)
    reward_item = Column(String)
    status = Column(Enum(StatusType))
    time_required = Column(Integer, comment="min")

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    send_user = Column(ForeignKey("users.id"))
    receive_user = Column(ForeignKey("users.id"))


def init_db():

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    s = Session(bind=engine, autocommit=False, autoflush=False)
    s.bulk_insert_mappings(Users, dummy_users)
    s.commit()
    s.bulk_insert_mappings(Jobs, dummy_jobs)
    s.commit()
    s.bulk_insert_mappings(Transaction, dummy_transactions)
    s.commit()
