#source /home/moje3831/virtualenv/EIEC/Boondmanager/3.11/bin/activate && cd /home/moje3831/EIEC/Boondmanager
from flask import Flask
from dotenv import load_dotenv
import os
import boondmanager

load_dotenv()

#Connexion BDD
DB_IP=os.getenv('DB_IP')
DB_USER=os.getenv('DB_USER')
DB_PWD=os.getenv('DB_PWD')
DB_NAME=os.getenv('DB_NAME')

app = Flask(__name__)

@app.route('/')
def welcome():
    url = "https://ui.boondmanager.com/api/payments"
    df = boondmanager.get_boond_csv(url)
    print(df)
    return 'Hello World!'
    
if __name__ == "__main__":
    app.run()