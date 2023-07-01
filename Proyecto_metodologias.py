import datetime
import csv
import grovepi
import grove_rgb_lcd
from time import sleep
from grovepi import *

#aaaa
# Pin para el sensor de humedad y temperatura
puerto_humedadyt= 7 #digital
dht_sensor_type=0   #analogo

# Pin para el sensor de intensidad luminosa
sensor_intensidad_luminosa = 1 #analogo

# Pin para el potenciómetro
pin_potenciometro = 2 #analogo


def leer_humedad_temperatura():
    [temperatura, humedad] = grovepi.dht(puerto_humedadyt, dht_sensor_type)
    
    return humedad, temperatura

def leer_intensidad_luminosa():
    intensidad = grovepi.analogRead(sensor_intensidad_luminosa)
    
    return intensidad

def obtener_tiempo_muestreo():
    valor_potenciometro = grovepi.analogRead(pin_potenciometro)
    tiempo_muestreo = int(1 + (valor_potenciometro / 1023) * 4)# Escala el valor a un rango entre 1 y 5 sg
    print(tiempo_muestreo, "Sg")
    return tiempo_muestreo#en seundos

def mostrar_en_lcd(humedad,temperatura,intensidad,tiempo_muestreo):
    grove_rgb_lcd.setRGB(255,255,0)
    grove_rgb_lcd.setText_norefresh("H:{}% T:{}C I:{}Lx Tpo:{}s".format(humedad,temperatura,intensidad,tiempo_muestreo))



def almacenar_en_tabla(tabla, datos):
    
    tabla.append(datos)

def convertir_a_csv(tabla):
    nombre_archivo = "datos_ambientales.csv"
    with open(nombre_archivo, mode='w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        escritor_csv.writerow(['Timestamp', 'Temperatura', 'Humedad_Relativa', 'Intensidad_Luminica'])
        escritor_csv.writerows(tabla)
    print("Archivo CSV generado con éxito.")

tabla_datos = []

while True:
    marca_tiempo = datetime.datetime.now()

    humedad, temperatura = leer_humedad_temperatura()
    intensidad = leer_intensidad_luminosa()
    tiempo_muestreo = obtener_tiempo_muestreo()

    mostrar_en_lcd(humedad,temperatura,intensidad,tiempo_muestreo)

    datos = [marca_tiempo, temperatura, humedad, intensidad]
    almacenar_en_tabla(tabla_datos, datos)

    

    sleep(tiempo_muestreo)

    # Cada cierto tiempo, convertir la tabla en un archivo CSV
    if len(tabla_datos) % 10 == 0:  # Por ejemplo, cada 10 muestras
        convertir_a_csv(tabla_datos)