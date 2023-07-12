import datetime
import csv
import random
from time import sleep
from proyecto_metodologia_simulacion import simular_datos, almacenar_en_tabla, convertir_a_csv

def test_simular_datos():
    humedad, temperatura, intensidad, tiempo_muestreo = simular_datos()
    
    assert 40 <= humedad <= 70
    assert 10 <= temperatura <= 40
    assert 100 <= intensidad <= 600
    assert 1 <= tiempo_muestreo <= 5

def test_almacenar_en_tabla():
    tabla = []
    datos = [datetime.datetime.now(), 25, 60, 200]
    almacenar_en_tabla(tabla, datos)
    
    assert tabla == [datos]

def test_convertir_a_csv(tmp_path):
    tabla = [
        [datetime.datetime(2022, 1, 1, 12, 0), 25, 60, 200],
        [datetime.datetime(2022, 1, 1, 13, 0), 26, 65, 250]
    ]
    


    
    expected_content = "Tiempo (Fecha/hora);Temperatura(C°);Humedad_Relativa(%);Intensidad_Luminica(Lx)\n"
    expected_content += "2022-01-01 12:00:00;25;60;200\n"
    expected_content += "2022-01-01 13:00:00;26;65;250\n"
