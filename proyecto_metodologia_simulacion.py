import datetime
import csv
from time import sleep
import random

# Pin para el sensor de humedad y temperatura
puerto_humedadyt= 7 #digital
dht_sensor_type=0   #analogo

# Pin para el sensor de intensidad luminosa
sensor_intensidad_luminosa = 1 #analogo

# Pin para el potenciómetro
pin_potenciometro = 2 #analogo

def simular_datos(): #Decidimos hacerlos int ya que permitia visualizar mejor la tabla, se pierde un poco la precisión.
    humedad = int(random.uniform(40,70)) #Rango de humedad relativa.
    temperatura = int(random.uniform(10, 40)) #Rango de la temperatura ambiente de la ciudad.
    intensidad = int(random.uniform(100, 600)) #Rango de la intensidad luminica basandonos en estandar de oficina y habitaciones.
    tiempo_muestreo = random.randint(1, 5)
    
    return humedad, temperatura, intensidad, tiempo_muestreo

def mostrar(humedad,temperatura,intensidad,tiempo_muestreo): #Se modifica la función de mostrar en lcd para que sea visualizable en la consola.
    print("H:{}% T:{}C I:{}Lx Tpo:{}s".format(humedad,temperatura,intensidad,tiempo_muestreo))
    

def almacenar_en_tabla(tabla, datos):
    tabla.append(datos)

def convertir_a_csv(tabla): #Se agrega ; para separar las casillas y se visualice mejor la tabla.
    nombre_archivo = "datos_ambientales.csv"
    with open(nombre_archivo, mode='w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        escritor_csv.writerow(['Tiempo (Fecha/hora)', 'Temperatura(C°)', 'Humedad_Relativa(%)', 'Intensidad_Luminica(Lx)'])
        escritor_csv.writerows(tabla)
    print("Archivo CSV generado con éxito.")

tabla_datos = []

while True:
    marca_tiempo = datetime.datetime.now()

    humedad, temperatura, intensidad, tiempo_muestreo = simular_datos()

    mostrar(humedad, temperatura, intensidad, tiempo_muestreo) #se cambia por la función modificada.

    datos = [marca_tiempo, temperatura, humedad, intensidad]
    almacenar_en_tabla(tabla_datos, datos)

    sleep(tiempo_muestreo)

    # Cada cierto tiempo, convertir la tabla en un archivo CSV
    if len(tabla_datos) % 10 == 0:  # En este caso, cada 10 muestras, pero puedes ser modificado.
        convertir_a_csv(tabla_datos)
        break
        
        