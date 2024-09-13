#source /home/moje3831/virtualenv/EIEC/Boondmanager/3.11/bin/activate && cd /home/moje3831/EIEC/Boondmanager
from flask import Flask
from dotenv import load_dotenv
import pandas as pd
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import mysql.connector as MC


import boondmanager
import database as db

load_dotenv()
DB_IP=os.getenv('DB_IP')
DB_USER=os.getenv('DB_USER')
DB_PWD=os.getenv('DB_PWD')
DB_NAME=os.getenv('DB_NAME')

db_url = f"mysql+pymysql://{DB_USER}:{DB_PWD}@{DB_IP}:3306/{DB_NAME}"

engine = create_engine(db_url)


app = Flask(__name__)

@app.route('/')
def welcome():
    url = "https://ui.boondmanager.com/api/payments.csv?perimeterAgencies=2"
    df = boondmanager.get_boond_csv(url)
    ddl = pd.io.sql.get_schema(df, 'PAYMENTS', con=engine)

    conn = MC.connect(host = DB_IP, user = DB_USER, password = DB_PWD, database = DB_NAME)
    cursor = conn.cursor()

    cursor.execute('DROP TABLE IF EXISTS PAYMENTS;')
    cursor.execute(ddl)

    conn.commit()
    df.to_sql('PAYMENTS', con=engine, if_exists='replace')
    return 'Hello World!'
    
@app.route('/payments')
def sync_payments():
    url = "https://ui.boondmanager.com/api/payments"
    df = boondmanager.get_boond_csv(url)


    requete = db.requete_payments()

    data = []
    for index, row in df:
        data.append((row['id']))

    return 'Paiements mis à jour.'


if __name__ == "__main__":
    app.run()