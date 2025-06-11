#to create our sqlite database
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base() #base is a special class that helps SQLAlchemy to know how to connect python class
#to database table 

#defined a new table called restaurants in the database
#the class here is the model. SQLAlchemy treats this like a table 
class Restaurant(Base):
    
    __tablename__ = 'restaurants'
    
    id = Column(Integer, primary_key=True, index=True)
    cuisine = Column(String)
    name = Column(String)
    menu_items = Column(String)
    
#SQLAlchemy will use a SQLite database file called restaurant.db, located in the current folder (./).
#// means host-based connection (like with PostgreSQL or MySQL)
#/// means database is local file 
SQLALCHEMY_DATABASE_URL = "sqlite:///./restaurant.db"

#creates a connection to the engine
#check_same_thread = False is required for SQLlite when working with FASTAPI 
#SQLite, by default, only allows the same thread (i.e. a single flow of execution) that opened the database 
# to use the connection.
#But FastAPI runs code using multiple threads so if one thread opens a connection to the database and 
# #another tries to insert data using same connection, we dont want SQLite to throw error 

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine) #create table if dont exist in database
    
    
    