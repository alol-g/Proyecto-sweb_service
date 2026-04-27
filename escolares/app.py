from flask import Flask, jsonify

app = Flask(__name__)

# Base de datos simulada para Escolares (30 registros)
ADEUDOS = {
    "2020001": {"adeudo": False, "detalle": "Documentación completa"},
    "2020002": {"adeudo": True, "detalle": "Falta certificado de bachillerato"},
    "2020003": {"adeudo": False, "detalle": "Sin adeudos"},
    "2020004": {"adeudo": True, "detalle": "Pendiente fotografías tamaño título"},
    "2020005": {"adeudo": True, "detalle": "Falta liberación de Servicio Social"},
    "2020006": {"adeudo": False, "detalle": "Todo en orden"},
    "2020007": {"adeudo": True, "detalle": "Adeudo de pago de reinscripción"},
    "2020008": {"adeudo": False, "detalle": "Documentación validada"},
    "2020009": {"adeudo": True, "detalle": "Falta liberación de prácticas profesionales"},
    "2020010": {"adeudo": False, "detalle": "Sin pendientes escolares"},
    "2020011": {"adeudo": True, "detalle": "Acta de nacimiento legible pendiente"},
    "2020012": {"adeudo": False, "detalle": "Estatus: Limpio"},
    "2020013": {"adeudo": True, "detalle": "Falta constancia de inglés"},
    "2020014": {"adeudo": False, "detalle": "Sin adeudos registrados"},
    "2020015": {"adeudo": True, "detalle": "CURP no actualizado"},
    "2020016": {"adeudo": False, "detalle": "Documentos completos"},
    "2020017": {"adeudo": True, "detalle": "Falta certificado médico"},
    "2020018": {"adeudo": False, "detalle": "Proceso administrativo concluido"},
    "2020019": {"adeudo": True, "detalle": "Pendiente firma de solicitud de egreso"},
    "2020020": {"adeudo": False, "detalle": "Sin pendientes"},
    "2020021": {"adeudo": True, "detalle": "Falta validación de identidad"},
    "2020022": {"adeudo": False, "detalle": "Limpio"},
    "2020023": {"adeudo": True, "detalle": "Adeudo de créditos complementarios"},
    "2020024": {"adeudo": False, "detalle": "Sin observaciones"},
    "2020025": {"adeudo": True, "detalle": "Trámite de equivalencia pendiente"},
    "2020026": {"adeudo": False, "detalle": "Documentación al 100%"},
    "2020027": {"adeudo": True, "detalle": "Falta dictamen de revalidación"},
    "2020028": {"adeudo": False, "detalle": "Estatus: Aprobado"},
    "2020029": {"adeudo": True, "detalle": "Seguro facultativo no vigente"},
    "2020030": {"adeudo": False, "detalle": "Sin deudas escolares"}
}

@app.route('/check/<matricula>', methods=['GET'])
def consultar(matricula):
    # El Orquestador usará este JSON para dar el veredicto final [cite: 52, 59]
    res = ADEUDOS.get(matricula, {"adeudo": False, "detalle": "No registrado / Sin adeudos"})
    
    return jsonify({
        "departamento": "Escolares",
        "adeudo": res["adeudo"],
        "mensaje": res["detalle"]
    })

if __name__ == '__main__':
    # Puerto 5002 asignado al microservicio de Escolares en la red LAN [cite: 45]
    app.run(host='0.0.0.0', port=5002)