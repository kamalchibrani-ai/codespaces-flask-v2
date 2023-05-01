from sqlalchemy import text , create_engine

engine = create_engine("mysql+pymysql://q6lels719cbrqhrqinqt:pscale_pw_imXJaGPrLczyyt5yqGn0fBLK8T0pPgAnT4epzBgB1Gz@aws.connect.psdb.cloud/careers?charset=utf8mb4",
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
