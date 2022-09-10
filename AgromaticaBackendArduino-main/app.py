import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from flask import Flask,render_template,jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
from flask_serial import Serial
import random
# microservices
from routers.datosensorrouter import datosensor
from routers.datosplantarouter import datosplanta
from eventlet import monkey_patch


monkey_patch()

# config app
app = Flask(__name__)
app.config['SERIAL_TIMEOUT'] = 0.2
app.config['SERIAL_PORT'] = 'COM2'
app.config['SERIAL_BAUDRATE'] = 9600
app.config['SERIAL_BYTESIZE'] = 8
app.config['SERIAL_PARITY'] = 'N'
app.config['SERIAL_STOPBITS'] = 1
app.config['SECRET_KEY'] = 'secret!'
CORS(app)
ser =Serial(app)
socketio = SocketIO(app,cors_allowed_origins="*")


@app.route('/')
def index(): 
    return render_template('index.html')

app.register_blueprint(datosensor)
app.register_blueprint(datosplanta)

@socketio.on('signal')
def handle_json(signal):
    
    print('received json: ' + str(signal))

@ser.on_message()
def handle_message(medida):
    medida = medida.decode().replace('\r','').replace('\n','')
    # print("miraa",medida)
    # insetando datos
    temperatura = float(medida) if len(str(medida).strip()) > 0 else 0
    humedad = random.randint(66,70)
    ph = random.randint(7,9)
    luz = random.randint(450,550)
    
    # sql = Conecction()
    # sql.Insert(
    #     "INSERT INTO  TBL_DATOS_SENSOR  VALUES (NULL,?,?,?,?,?)",
    #     (temperatura,humedad,ph,luz,datetime.now())
    # )
    datos = f'{medida},{humedad},{ph},{luz} '
    socketio.emit('data',str(datos))

if __name__ == '__main__':
    socketio.run(app,debug = False)