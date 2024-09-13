from dotenv import load_dotenv
import os
import mysql.connector as MC

load_dotenv()

#Connexion BDD
DB_IP=os.getenv('DB_IP')
DB_USER=os.getenv('DB_USER')
DB_PWD=os.getenv('DB_PWD')
DB_NAME=os.getenv('DB_NAME')

#Initialise la BDD.
def init_database():
    request = open('config.sql', 'r').read()

    conn = MC.connect(host = DB_IP, user = DB_USER, password = DB_PWD, database = DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute(request, multi=True)
    conn.commit()
    return 0

def requete_payments():
    requete = "INSERT INTO PAYMENTS (ID_PAYMENT, ID_PURCHASE, PMT_NUM, PMT_HT, PMT_TTC) \
        VALUES (%s, %s, %s, %s, %s) \
        ON DUPLICATE KEY UPDATE ID_PAYMENT = ID_PAYMENT"
    return requete

if __name__ == "__main__":
    init_database()