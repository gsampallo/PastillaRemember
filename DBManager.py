import sqlite3
from sqlite3 import Error

from Parameters import Parameters

class DBManager:

    def __init__(self,config_file = '/home/pi/RPIGrowBot/config_database.json' ):
        # Cambiar luego el path correcto para el archivo de configuracion

        self.param = Parameters()
        self.param.set_file_config(config_file)
        self.param.load_parameters()

        self._database_file = self.param.parameters["database_file"]


    def sql_connection(self):
        try:
            self._con = sqlite3.connect(self._database_file)
        except Error:
            print(Error)


    def create_table(self,sql_create):
        if self._con:
            cursorObj = self._con.cursor()

            cursorObj.execute(sql_create)

            self._con.commit()

    def insert(self,sql_insert):
        try:
            cursor = self._con.cursor()
            cursor.execute(sql_insert)
            cursor.close()
            self._con.commit()
        except Error:
            print(Error)            

    def update(self,sql_update):
        try:
            cursor = self._con.cursor()
            cursor.execute(sql_update)
            cursor.close()
            self._con.commit()
        except sqlite3.OperationalError:
            print("Errores en la consulta")
        except Error:
            print(Error)            

    def query(self,sql_query):
        cursor = self._con.cursor()
        cursor.execute(sql_query)
        records = cursor.fetchall()
        cursor.close()
        return records

if __name__ == "__main__":

    dbManager = DBManager()
    dbManager.sql_connection()
    #dbManager.create_table("CREATE TABLE users(id integer PRIMARY KEY)");    