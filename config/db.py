from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_uYK5Oroy0wcRrJYtFOc@mysql-3299278f-utxicotepec-623d.h.aivencloud.com:11209/defaultdb"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base= declarative_base()




