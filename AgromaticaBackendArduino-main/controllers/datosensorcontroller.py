import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from models.datosensor import DatosSensorModel
from config.sqlhelper import Conecction

class DatosSensorController:
    def Create(self,params):
        sql_helper = Conecction()
        dataresponse = sql_helper.ExecuteQueryAsync("INSERT INTO  TBL_DATOS_SENSOR  VALUES (NULL,?,?,?,?,?)",params)
        return dataresponse
    def LoadData(self):
        sql_helper = Conecction()
        data = []
        dataresponse = sql_helper.ListQueryAsync("SELECT * from TBL_DATOS_SENSOR ORDER by FechaRegistro DESC LIMIT 10 ")
        for _ in dataresponse:
            json = DatosSensorModel(_[0],_[1],_[2],_[3],_[4],_[5]).__dict__
            data.append(json)
        return data
    def SearchData(self,date_from:str,date_to:str):
        sql_helper = Conecction()
        data = []
        dataresponse = sql_helper.ListQueryAsync(
            f"SELECT * from TBL_DATOS_SENSOR WHERE FechaRegistro BETWEEN '{date_from}' AND '{date_to}' LIMIT 10 "
        )
        for _ in dataresponse:
            json = DatosSensorModel(_[0],_[1],_[2],_[3],_[4],_[5]).__dict__
            data.append(json)
        return data
    def PaginationData(self,limit,offset,date_from:str,date_to:str):
        sql_helper = Conecction()
        data = []
        dataresponse = sql_helper.ListQueryAsync(
            f"""
                SELECT * from TBL_DATOS_SENSOR
                WHERE FechaRegistro BETWEEN '{date_from}' 
                AND '{date_to}'
                 LIMIT {limit} OFFSET {offset}
            """
        )
        for _ in dataresponse:
            json = DatosSensorModel(_[0],_[1],_[2],_[3],_[4],_[5]).__dict__
            data.append(json)
        return data
    def AvgData(self):
        sql_helper = Conecction()
        data = []
        dataresponse = sql_helper.ListQueryAsync("select avg(Temperatura) as 'Temperatura', avg(Humedad) as 'Humedad',  avg(Ph) as 'Ph', avg(Luz) as 'Luz'	from TBL_DATOS_SENSOR")
        for _ in dataresponse:
            json = DatosSensorModel('',_[0],_[1],_[2],_[3],'').__dict__
            data.append(json)
        return data[0]
    def CountData(self):
        sql_helper = Conecction()
        dataresponse = sql_helper.ListQueryAsync("select count(*) from TBL_DATOS_SENSOR")
        return dataresponse[0][0]

