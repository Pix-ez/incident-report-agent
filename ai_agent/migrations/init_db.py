import sys

sys.path.append("/app")

from db.database import engine
from db.models import Base

print("Creating tables...")

Base.metadata.create_all(bind=engine)

print("Done.")