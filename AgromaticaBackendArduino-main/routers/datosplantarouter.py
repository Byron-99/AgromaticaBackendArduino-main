import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from flask import Blueprint, jsonify, request,json
from controllers.datosplantacontroller import DatosPlantaController

datosplanta = Blueprint('datosplanta',__name__)


@datosplanta.route("/api/datosplanta/identificar",methods=['POST'])
def LoadData():
    res = request.data
    img = json.loads(res)
    respuesta = DatosPlantaController().IdentifyPlant(file_names=img)
    return jsonify({"data": respuesta})
