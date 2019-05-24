from pymongo import MongoClient
from bson.son import SON
import pprint
# agregar cadena de conexion en mongoclient si es necesario
db = MongoClient().kpi_eventos
# lista todas las colecciones de la base de datos
print(db.list_collection_names())

# en caso de tener algun caracter que no te permita llamar a la collecion con (.) collection = db['test-collection']
collection_kpi_evento = db.kpi_evento
# definir variable con los papipelines correspondientes
pipeline = [
    {"$group": {
        "_id": "$estilo",
        "estilos": {"$push": "$evento"},
        "cantidadEstilos": {"$sum": 1}

    }},
    {"$limit": 1}
]

print(pipeline)

# pretty print te permite formatear de mejor manera con saltos de lineas y tabulaciones los distintos niveles del objectArray
pprint.pprint(list(collection_kpi_evento.aggregate(pipeline)))

# aqui puedes ver la lista sin ningun formato
# print(list(collection_kpi_evento.aggregate(pipeline)))

# lo que entrega es un puntero binario que debe ser procesado por una lista para ser visualizado
# este puntero nos permite recorrer con foreach si existen en python xD o especies de fetch conocidos en php
# print(collection_kpi_evento.aggregate(pipeline))

