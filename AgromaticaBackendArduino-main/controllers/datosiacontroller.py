import sys
import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from models.datosensor import DatosSensorModel
from config.sqlhelper import Conecction

class DatosIaController:
    def LoadData(self):
        sql_helper = Conecction()
        dataresponse = sql_helper.ListQueryAsync("SELECT PH,FECHAREGISTRO from TBL_DATOS_SENSOR ORDER by FechaRegistro DESC LIMIT 10 ")
        ph=[]
        lista=[]
        for row in dataresponse:
            ph.append(row[0])
            lista.append(row[1][6:10].replace('-','.'))
        ph_final=np.array(ph,dtype=int)
        lista_final=np.array(lista,dtype=float)
        capa1=tf.keras.layers.Dense(units=3,input_shape=[1])
        capa2=tf.keras.layers.Dense(units=3)
        salida=tf.keras.layers.Dense(units=1)
        modelo=tf.keras.Sequential([capa1,capa2,salida])
        modelo.compile(
            optimizer=tf.keras.optimizers.Adam(0.001),
            loss='mean_squared_error'
        )
        historial=modelo.fit(lista_final,ph_final, epochs=30, verbose=False)
        resultado= round(float(modelo.predict([10.06])), 3) ## MES Y DIA
        print(resultado)
        plt.xlabel("# Epoca")
        plt.ylabel("Magnitud de perdida")
        plt.plot(historial.history['loss'])
        plt.show()


DatosIaController().LoadData()
   

