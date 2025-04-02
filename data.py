import json
import random
from datetime import date, datetime
import uuid


def generar_id():
    return str(uuid.uuid4())

def leer_datos():
    try:
        with open('data.json', 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def guardar_datos(data):
    try:
        with open('data.json', 'w', encoding='utf-8') as archivo:
            json.dump(data, archivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"{e}")

def input_nota(frase_ingles, frase_espanol):

    nota = {
        'id':generar_id(),
        'ingles':frase_ingles,
        'espanol':frase_espanol,
        'fecha': f'{date.today()}'
    }
    return nota

def agregar_nota(frase_ingles, frase_espanol):
    datos = leer_datos()
    datos.append(input_nota(frase_ingles, frase_espanol))
    guardar_datos(datos)
    print("Nota agregada exitosamente.")

def obtener_nota_aleatoria():
    datos = leer_datos()
    if datos:
        nota_aleatoria = random.choice(datos)
        return nota_aleatoria
    else:
        return None

def formatear_fecha(fecha):
    fecha = fecha.replace('/','-')
    try:
        fecha_formateada = datetime.strptime(fecha, '%Y-%m-%d')
        return fecha_formateada.strftime('%Y-%m-%d')
    except Exception as e:
        print(f"Fecha no valida. {e}")
        return None

def eliminar_nota_id(id):
    datos = leer_datos()
    notas = [nota for nota in datos if nota['id'] != id]
    guardar_datos(notas)
    return 'nota eliminada'

def buscar_nota_por_id(id):
    data = leer_datos()
    nota = next((nota for nota in data if nota['id'] == id), None)
    return nota

def actualizar_nota(nota_actualizada):
    data = leer_datos()
    for index, nota in enumerate(data):
        if nota['id'] ==  nota_actualizada['id']:
            data[index] = nota_actualizada
    guardar_datos(data)        
    return ''
