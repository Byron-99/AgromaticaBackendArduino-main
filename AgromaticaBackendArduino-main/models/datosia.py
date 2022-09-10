class DatosSensorModel:
    def __init__(self,id:int,temperatura: str,humedad:str,ph:str,luz:str,fecharegistro:str):
        self.id = id
        self.temperatura = temperatura
        self.humedad = humedad
        self.ph = ph
        self.luz = luz
        self.fecharegistro = fecharegistro