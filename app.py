#source /home/moje3831/virtualenv/EIEC/Boondmanager/3.11/bin/activate && cd /home/moje3831/EIEC/Boondmanager
from flask import Flask
from dotenv import load_dotenv
import os
import base64

load_dotenv()
mail = os.getenv('mail')
pwd = os.getenv('pwd')

app = Flask(__name__)

@app.route('/')
def welcome():
    get_boond()
    return 'Hello World!'

def get_boond():
    print(mail)
    print(pwd)
    token = base64.b64encode(b"{mail}:{pwd}")
    print(token)
    #conn_str = f"Basic {token}"
    return 0
    
if __name__ == "__main__":
    app.run()