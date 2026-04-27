from flask import Flask, jsonify

app = Flask(__name__)

# Base de datos simulada
ADEUDOS = {
    "2020001": {"adeudo": False, "detalle": "Sin pendientes"},
    "2020002": {"adeudo": True, "detalle": "Multa por libro atrasado"},
    "2020003": {"adeudo": False, "detalle": "Devuelto recientemente"},
    "2020004": {"adeudo": False, "detalle": "Sin pendientes"},
    "2020005": {"adeudo": True, "detalle": "Libro no devuelto: Java para programadores"},
    "2020006": {"adeudo": True, "detalle": "Retraso en entrega de Sistemas Operativos"},
    "2020007": {"adeudo": False, "detalle": "Sin pendientes"},
    "2020008": {"adeudo": True, "detalle": "Daño en libro de Estructuras de Datos"},
    "2020009": {"adeudo": False, "detalle": "Sin pendientes"},
    "2020010": {"adeudo": True, "detalle": "Préstamo vencido de Sistemas Distribuidos"},
    "2020011": {"adeudo": False, "detalle": "Regularizado"},
    "2020012": {"adeudo": True, "detalle": "Multa pendiente por retraso"},
    "2020013": {"adeudo": True, "detalle": "Libro extraviado"},
    "2020014": {"adeudo": False, "detalle": "Sin pendientes"},
    "2020015": {"adeudo": True, "detalle": "Entrega incompleta de material"},
    "2020016": {"adeudo": False, "detalle": "Sin pendientes"},
    "2020017": {"adeudo": True, "detalle": "Adeudo por reposición de libro"},
    "2020018": {"adeudo": False, "detalle": "Sin pendientes"},
    "2020019": {"adeudo": True, "detalle": "Multa acumulada"},
    "2020020": {"adeudo": True, "detalle": "Retraso en devolución"},
    "2020021": {"adeudo": False, "detalle": "Sin pendientes"},
    "2020022": {"adeudo": True, "detalle": "Libro prestado no registrado como devuelto"},
    "2020023": {"adeudo": False, "detalle": "Sin pendientes"},
    "2020024": {"adeudo": True, "detalle": "Sanción por daño de material"},
    "2020025": {"adeudo": False, "detalle": "Sin pendientes"},
    "2020026": {"adeudo": True, "detalle": "Adeudo en biblioteca digital"},
    "2020027": {"adeudo": False, "detalle": "Sin pendientes"},
    "2020028": {"adeudo": True, "detalle": "Préstamo vencido"},
    "2020029": {"adeudo": False, "detalle": "Sin pendientes"},
    "2020030": {"adeudo": True, "detalle": "Pendiente de pago de multa"}
}
@app.route('/check/<matricula>', methods=['GET'])

def consultar(matricula):
    res = ADEUDOS.get(matricula, {"adeudo": False, "detalle": "Limpio"
        })
    return jsonify({
        "departamento": "Biblioteca",
        "adeudo": res["adeudo"],
        "mensaje": res["detalle"]
    })
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)