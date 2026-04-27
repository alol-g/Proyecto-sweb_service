from flask import Flask, jsonify

app = Flask(__name__)

# Base de datos simulada - Lab de Electrónica
ADEUDOS = {
    "2020001": {"adeudo": False, "detalle": "Sin pendientes"},
    "2020002": {"adeudo": True,  "detalle": "Kit de componentes SMD pendiente de devolución"},
    "2020003": {"adeudo": True,  "detalle": "Osciloscopio prestado sin devolver"},
    "2020004": {"adeudo": False, "detalle": "Limpio"},
    "2020005": {"adeudo": True,  "detalle": "Fuente de poder dañada sin reporte"},
    "2020006": {"adeudo": True,  "detalle": "Multa por entrega tardía de multímetro"},
    "2020007": {"adeudo": False, "detalle": "Sin adeudos vigentes"},
    "2020008": {"adeudo": True,  "detalle": "Cautín de estación Weller extraviado"},
    "2020009": {"adeudo": True,  "detalle": "Generador de funciones con cables faltantes"},
    "2020010": {"adeudo": False, "detalle": "Solvente tras revisión"},
    "2020011": {"adeudo": True,  "detalle": "Pendiente de entregar tarjeta FPGA"},
    "2020012": {"adeudo": True,  "detalle": "Manual de laboratorio maltratado"},
    "2020013": {"adeudo": False, "detalle": "Historial limpio"},
    "2020014": {"adeudo": True,  "detalle": "Analizador lógico no retornado"},
    "2020015": {"adeudo": False, "detalle": "Liberación de servicio completada"},
    "2020016": {"adeudo": True,  "detalle": "Puntas de prueba de osciloscopio rotas"},
    "2020017": {"adeudo": False, "detalle": "Entregado a tiempo"},
    "2020018": {"adeudo": True,  "detalle": "Caja de herramientas sin candado"},
    "2020019": {"adeudo": True,  "detalle": "Debe kit de robótica básico"},
    "2020020": {"adeudo": False, "detalle": "Sin observaciones"},
    "2020021": {"adeudo": True,  "detalle": "Microcontrolador quemado sin reposición"},
    "2020022": {"adeudo": False, "detalle": "Paz y salvo"},
    "2020023": {"adeudo": True,  "detalle": "Cable de alimentación faltante en fuente"},
    "2020024": {"adeudo": True,  "detalle": "Baterías de multímetro agotadas y no reemplazadas"},
    "2020025": {"adeudo": False, "detalle": "Material devuelto íntegramente"},
    "2020026": {"adeudo": True,  "detalle": "Protoboard con residuos de pegamento/quemaduras"},
    "2020027": {"adeudo": True,  "detalle": "Módulo Bluetooth no devuelto"},
    "2020028": {"adeudo": False, "detalle": "Verificado por encargado"},
    "2020029": {"adeudo": True,  "detalle": "Sensor de presión dañado en práctica"},
    "2020030": {"adeudo": False, "detalle": "Estatus OK"}
}

@app.route('/check/<matricula>', methods=['GET'])
def consultar(matricula):
    res = ADEUDOS.get(matricula, {"adeudo": False, "detalle": "Sin registro - Limpio"})
    return jsonify({
        "departamento": "Lab. Electronica",
        "adeudo": res["adeudo"],
        "mensaje": res["detalle"]
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "online", "departamento": "Lab. Electronica"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)