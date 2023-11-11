from flask import Flask, Response
import json
import random

app = Flask(__name__)


# Lista de Pokeneas
pokeneas = [
    {"id": 1, "nombre": "neasork", "altura": "60cm", "habilidad": "mudar gorra", "imagen": "https://storage.googleapis.com/pokeneas_bucket/neasople.png", "frase filosofica": "si gorra no tienes, neasork no te conviene"},
    {"id": 2, "nombre": "puchinea", "altura": "180cm", "habilidad": "golpear con cadenas", "imagen": "https://storage.googleapis.com/pokeneas_bucket/oversizenea.png", "frase filosofica": "si mas alto que puchinea eres, golpe con cadena tienes"},
    {"id": 3, "nombre": "neasople", "altura": "40cm", "habilidad": "soplar", "imagen": "https://storage.googleapis.com/pokeneas_bucket/neasople.png", "frase filosofica": "si encenderlo necesitas, neasople te lo facilita"},
    {"id": 4, "nombre": "oversizenea", "altura": "150cm", "habilidad": "comprar ropa oversize", "imagen": "https://storage.googleapis.com/pokeneas_bucket/oversizenea.png", "frase filosofica": "si tu pantalon se te cae, oversizenea te regala el maquillaje"},
    {"id": 5, "nombre": "nearmas", "altura": "100cm", "habilidad": "vender armas", "imagen": "https://storage.googleapis.com/pokeneas_bucket/neafarra.png", "frase filosofica": "si arma para protegerte deseas, nearmas te vende la que sea"},
    {"id": 6, "nombre": "neafarra", "altura": "80cm", "habilidad": "bailar", "imagen": "https://storage.googleapis.com/pokeneas_bucket/neafarra.png", "frase filosofica": "si del techno disfrutas, neafarra contigo se enchula"},
    {"id": 7, "nombre": "boconea", "altura": "100cm", "habilidad": "contar chismes", "imagen": "https://storage.googleapis.com/pokeneas_bucket/boconea.png", "frase filosofica": "si contando chisme estas, boconea a tu lado veras"}
]

@app.route('/pokenea_json')
def pokenea_json():
    pokenea_aleatorio = random.choice(pokeneas)
    pokenea_info = {
        "Pokenea": {
            "id": pokenea_aleatorio["id"],
            "nombre": pokenea_aleatorio["nombre"],
            "altura": pokenea_aleatorio["altura"],
            "habilidad": pokenea_aleatorio["habilidad"]
        },
        "id_contenedor": "generico por el momento"
    }
    response = Response(json.dumps(pokenea_info), content_type='application/json')
    return response

@app.route('/pokenea_imagen')
def pokenea_imagen():
    pokenea_aleatorio = random.choice(pokeneas)
    html_content = f"<h1>Frase Filosofica: {pokenea_aleatorio['frase filosofica']}</h1><h2>ID del contenedor: obtener container</h2><img src='{pokenea_aleatorio['imagen']}' alt='Imagen'>"
    response = Response(json.dumps(html_content), content_type='text/html')
    return response

if __name__ == '__main__':
    app.run(debug=True)
