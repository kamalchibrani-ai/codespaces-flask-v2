from sqlalchemy import text , create_engine
from dotenv import load_dotenv
import os
load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
DATABASE = os.getenv("DATABASE")



engine = create_engine(f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}?charset=utf8mb4",
                       connect_args = {
                           "ssl":{
                               "ssl_ca": "/etc/ssl/cert.pem"
                           }
                       })


def get_jobs_from_db():
    Jobss = []
    with engine.connect() as connection:
        result = connection.execute(text("select * from jobs"))
        for row in result.all():
            Jobss.append(row._asdict())
    return Jobss

def get_job_by_id(id):
    Job = None
    with engine.connect() as connection:
        result = connection.execute(text("select * from jobs where id = :val"),{"val": id})
        # print(result)
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            for row in rows:
                Job = row._asdict()
                print(Job)
            return Job
