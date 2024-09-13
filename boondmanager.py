from dotenv import load_dotenv
import os
import base64
import requests
import io
import pandas as pd


load_dotenv()
# Données de connexion à Boondmanager
mail = os.getenv('mail')
pwd = os.getenv('pwd')
auth_str = f"{mail}:{pwd}"
token_boondmanager = base64.b64encode(auth_str.encode('ascii')).decode()


#Envoi une requête GET à Boond sur l'url précisée. Renvoi le dataframe pandas correspondant.
def get_boond_csv(url : str):

    headers = {
        "Authorization":f"Basic {token_boondmanager}"
    }

    res = requests.get(url, headers=headers)
    rawData = res.content

    data = io.StringIO(rawData.decode())
    print(data)
    df = pd.read_csv(data, delimiter=';')

    print(df.dtypes)
    return df

if __name__ == "__main__":
    url = "https://ui.boondmanager.com/api/payments"
    df = get_boond_csv(url)
    print(df)