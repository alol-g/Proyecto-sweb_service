from flask import Flask, jsonify

app = Flask(__name__)

# Base de datos simulada (Laboratorio de Redes)
ADEUDOS = {
    "2020001": {"adeudo": True, "detalle": "Cable de red no devuelto"},
    "2020002": {"adeudo": False, "detalle": "Equipo entregado correctamente"},
    "2020003": {"adeudo": True, "detalle": "Router asignado pendiente de entrega"},
    "2020004": {"adeudo": False, "detalle": "Sin pendientes"},
    "2020005": {"adeudo": True, "detalle": "Daño en switch del laboratorio"},
    "2020006": {"adeudo": False, "detalle": "Sin pendientes"},
    "2020007": {"adeudo": True, "detalle": "Cable coaxial no devuelto"},
    "2020008": {"adeudo": True, "detalle": "Router con configuración alterada"},
    "2020009": {"adeudo": False, "detalle": "Equipo entregado correctamente"},
    "2020010": {"adeudo": True, "detalle": "Switch extraviado"},
    "2020011": {"adeudo": False, "detalle": "Sin pendientes"},
    "2020012": {"adeudo": True, "detalle": "Patch cord dañado"},
    "2020013": {"adeudo": True, "detalle": "Adaptador USB de red no entregado"},
    "2020014": {"adeudo": False, "detalle": "Sin pendientes"},
    "2020015": {"adeudo": True, "detalle": "Equipo entregado incompleto"},
    "2020016": {"adeudo": False, "detalle": "Préstamo cerrado sin adeudos"},
    "2020017": {"adeudo": True, "detalle": "Router asignado no localizado"},
    "2020018": {"adeudo": False, "detalle": "Sin pendientes"},
    "2020019": {"adeudo": True, "detalle": "Daño en tarjeta de red"},
    "2020020": {"adeudo": True, "detalle": "Cable UTP categoría 6 extraviado"},
    "2020021": {"adeudo": False, "detalle": "Equipo revisado y aprobado"},
    "2020022": {"adeudo": True, "detalle": "Retraso en entrega de switch"},
    "2020023": {"adeudo": False, "detalle": "Sin pendientes"},
    "2020024": {"adeudo": True, "detalle": "Falta de entrega de accesorios"},
    "2020025": {"adeudo": False, "detalle": "Equipo devuelto completo"},
    "2020026": {"adeudo": True, "detalle": "Puerto de red dañado"},
    "2020027": {"adeudo": False, "detalle": "Sin pendientes"},
    "2020028": {"adeudo": True, "detalle": "Equipo prestado no registrado como devuelto"},
    "2020029": {"adeudo": False, "detalle": "Sin pendientes"},
    "2020030": {"adeudo": True, "detalle": "Multa por uso indebido del equipo"}
}

@app.route('/check/<matricula>', methods=['GET'])
def consultar(matricula):
    res = ADEUDOS.get(matricula, {
        "adeudo": False,
        "detalle": "Sin adeudos en laboratorio de redes"
    })

    return jsonify({
        "departamento": "Lab. Redes",
        "adeudo": res["adeudo"],
        "mensaje": res["detalle"]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)