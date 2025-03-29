import json
from data import leer_datos, formatear_fecha

def leer_fechas():
    try:
        with open('data_fechas.json', 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
    except Exception:
        return []

def guardar_fechas(data):
    try:
        with open('data_fechas.json', 'w', encoding='utf-8') as archivo:
            return json.dump(data, archivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f'{e}')

def crear_diccionario():
    diccionario_fechas = {
    }
    return diccionario_fechas

def obtener_fechas():
    data = leer_datos()
    fechas = list(set([nota['fecha'] for nota in data]))
    fechas.sort(key=lambda x: x)
    return fechas

def buscar_nota_por_fecha(fecha):
    datos = leer_datos()
    fecha_formateada = formatear_fecha(fecha)
    if fecha_formateada is not None:
        nota = [item for item in datos if item['fecha'] == fecha_formateada]
        return nota
    print(f"No se encontraron notas con esa fecha: {fecha}")

def estructura():
    data_fechas = []
    diccionario_fechas = crear_diccionario()
    fechas = obtener_fechas()
    for fecha in fechas:
        diccionario_fechas[fecha] = buscar_nota_por_fecha(fecha)
    data_fechas.append(diccionario_fechas)
    guardar_fechas(data_fechas)
estructura()