# Load .env file using:
from dotenv import load_dotenv
import os

load_dotenv()
Env = os.getenv("PYTHON_ENV")
app_port = os.getenv("PORT")
pg_dbname = os.getenv("DB_PG_DBNAME")
pg_user = os.getenv("DB_PG_USER")
pg_password = os.getenv("DB_PG_PASSWORD")
pg_host =os.getenv("DB_PG_HOST")
pg_ssl = os.getenv("DB_PG_SSL")
auth_user = os.getenv("AUTH_USERNAME")
auth_password= os.getenv("AUTH_PASSWORD")
bard_key=os.getenv("BARD_KEY")