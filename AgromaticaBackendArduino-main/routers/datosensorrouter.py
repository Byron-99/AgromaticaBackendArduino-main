import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from flask import Blueprint, jsonify
from controllers.datosensorcontroller import DatosSensorController

datosensor = Blueprint('datosensor',__name__)


@datosensor.route("/api/datosensor/dataload")
def LoadData():
    respuesta = DatosSensorController().LoadData()
    return jsonify({"data": respuesta})
@datosensor.route("/api/datosensor/searchdata/<date_from>/<date_to>")
def SearchData(date_from:str,date_to:str):
    respuesta = DatosSensorController().SearchData(date_from,date_to)
    return jsonify({"data": respuesta})
@datosensor.route("/api/datosensor/paginationdata/<limit>/<offset>/<date_from>/<date_to>")
def PaginationData(limit:int,offset:int,date_from:str,date_to:str):
    respuesta = DatosSensorController().PaginationData(limit,offset,date_from,date_to)
    return jsonify({"data": respuesta})
@datosensor.route("/api/datosensor/avgdata")
def AvgData():
    respuesta = DatosSensorController().AvgData()
    return jsonify({"data": respuesta})
@datosensor.route("/api/datosensor/countdata")
def CountData():
    respuesta = DatosSensorController().CountData()
    return jsonify({"data": respuesta})