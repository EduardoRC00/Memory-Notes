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
    # frase_ingles = input("Ingresa la frase en inglés: ").lower()
    # frase_espanol = input("Ingresa la frase en español: ").lower()

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


def input_respuesta_nota(nota):
    oportunidades = 3
    puntaje = 10
    while oportunidades > 0:
        respuesta_usuario = input(f"¿Cuál es la traducción de '{nota["ingles"]}'?: ").lower()
        if respuesta_usuario != nota['espanol']:
            oportunidades -= 1
            puntaje -=4
            print(f"Incorrecto. Intentos restantes {oportunidades}")
        else:
            print(f"Obtuviste {puntaje} estrellas\nLa frase '{nota['ingles']}'\n significa '{nota['espanol']}'")
            break
        if oportunidades == 0:
            opcion = input("¿Intentar nuevamente? (s/n): ").lower()
            if opcion == "s":
                oportunidades = 3
                puntaje = 10
            else:
                print(f"La frase '{nota['ingles']}'\n significa '{nota['espanol']}'")
                break

def obtener_nota_aleatoria():
    datos = leer_datos()
    if datos:
        nota_aleatoria = random.choice(datos)
    # input_respuesta_nota(nota_aleatoria)
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

def buscar_coincidencias_por_palabra(palabra):
    datos = leer_datos()
    coincidencias = [item for item in datos if palabra in item['ingles'] or palabra in item['espanol']]
    if not coincidencias:
        print('No se encontraron coincidencias. ')
    else:
        for nota in coincidencias:
            print(f'{nota['ingles']}: {nota['espanol']}')

def ordenar_por_fecha(ascendente_descendente):
    datos = leer_datos()
    if ascendente_descendente == 'd':
        datos.sort(key=lambda x: x.get('fecha'), reverse=True)
    for dato in datos:
        print(dato)

def ordenar_alfabeticamente(ascendente_descendente,idioma):
    datos = leer_datos()
    if idioma =='i':
        if ascendente_descendente == 'd':
            datos.sort(key=lambda x: x.get('ingles'),reverse=True)
        elif ascendente_descendente == 'a':
            datos.sort(key=lambda x: x.get('ingles'))
        else:
            print('Opción invalida. ')
    elif idioma == 'e':
        if ascendente_descendente == 'd':
            datos.sort(key=lambda x: x.get('espanol'),reverse=True)
        elif ascendente_descendente == 'a':
            datos.sort(key=lambda x: x.get('espanol'))
            print('Opción invalida. ')
    else:
        print('Idioma no integrado. ')

    for dato in datos:
        print(dato)

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

# def menu():
#     bandera = True
#     while bandera:
#         print("**********************")
#         print("** Menú de opciones **")
#         print("**********************")
#         print("1.- Agregar nueva nota")
#         print("2.- Repasar nota aleatoria")
#         print("3.- Buscar nota por fecha")
#         print("4.- Buscar coincidencias por palabra")
#         print("5.- Ordenar por fecha")
#         print("6.- Ordenar alfabeticamente")
#         print("7.- Salir")

#         try:
#             opcion = int(input("Selecciona una opción: "))
#         except ValueError:
#             print("Por favor, ingresa un número válido.")
#             continue

#         match opcion:
#             case 1:
#                 agregar_nota()
#             case 2:
#                 obtener_nota_aleatoria()
#             case 3:
#                 fecha = input("Ingresa la fecha (YYYY-MM-DD): ")
#                 buscar_nota_por_fecha(fecha)
#             case 4:
#                 palabra_a_buscar = input('Ingresa la palabra para hallar coincidencias: ')
#                 buscar_coincidencias_por_palabra(palabra_a_buscar)
#             case 5:
#                 ascendente_descendente = input('¿Quiere ordenar de forma ascendente o descendente? a/d: ').lower()
#                 ordenar_por_fecha(ascendente_descendente)
#             case 6:
#                 idioma = input('Ordenar diccionario ingles o español. i/e:').lower()
#                 ascendente_descendente = input('¿Quiere ordenar de forma ascendente o descendente? a/d: ').lower()
#                 ordenar_alfabeticamente(ascendente_descendente,idioma)
#             case 7:
#                 bandera = False
#                 print("Saliendo del programa. ¡Adiós!")
#             case _:
#                 print("Opción no válida. Por favor, intenta de nuevo.")


# if __name__ == '__main__':
#     menu()