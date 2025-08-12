from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1️⃣ MySQL database URL
DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/company_db"
# 2️⃣ Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# 3️⃣ Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4️⃣ Base class for ORM models
Base = declarative_base()

# 5️⃣ Dependency function for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


